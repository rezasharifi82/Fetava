import socket
import time

def discover_neighbors():
    # Create a raw socket
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.IPPROTO_RAW)

    # Set the destination MAC address to broadcast
    dst_mac = b'\xff\xff\xff\xff\xff\xff'

    # Set the Ethernet type to ARP
    eth_type = 0x0806

    # Build the ARP packet
    arp_packet = b''.join([
        dst_mac, # Destination MAC address
        b'\x00\x00\x00\x00\x00\x00', # Source MAC address
        eth_type.to_bytes(2, 'big'), # Ethernet type
        b'\x08\x00', # IP version and header length
        b'\x06', # Hardware type (Ethernet)
        b'\x00', # Protocol type (IPv4)
        b'\x06', # Hardware address length (6 bytes)
        b'\x04', # Protocol address length (4 bytes)
        b'\x00\x00\x00\x00', # Sender MAC address
        socket.inet_aton('0.0.0.0'), # Sender IP address
        dst_mac, # Target MAC address
        socket.inet_aton('255.255.255.255'), # Target IP address
    ])

    # Send the ARP packet
    for i in range(10):
        try:
            sock.send(arp_packet)
            time.sleep(1)

            # Receive all ARP responses
            while True:
                data, addr = sock.recvfrom(60)
                if len(data) == 42:
                    src_mac, src_ip = parse_arp_packet(data)
                    print(src_ip)
                    break
        except socket.error as e:
            print(f"Error sending/receiving ARP packet: {e}")
            break

def parse_arp_packet(data):
    opcode = data[6]
    src_mac = data[8:14]
    src_ip = data[24:28]

    return src_mac, src_ip

if __name__ == '__main__':
    discover_neighbors()
