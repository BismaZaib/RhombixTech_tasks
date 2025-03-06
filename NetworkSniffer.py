import socket
from struct import unpack

def main():

    conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    conn.bind(("192.168.0.108", 0))

    conn.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

    print("Listening for Packets")
    while True:
        packet,addr = conn.recvfrom(65535)

        ip_header =packet[:20]
        iph= unpack('!BBHHHBBH4s4s ',ip_header)
        src_ip= socket.inet_ntoa(iph[8])
        dest_ip= socket.inet_ntoa(iph[9])
        print(f"Source IP: {src_ip}, Destination IP: {dest_ip}")
if __name__=="__main__" : # type: ignore
         main()
