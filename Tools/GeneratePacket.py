from scapy.all import *

def generatePacket():
    print('GENERATING PACKET')
    dnsPacket = IP(dst="10.0.0.4")
    dnsPacket.options = "\x91\x08\x00\x00\x00\x00\x00\x00"
    dnsPacket = dnsPacket/UDP()
    dnsPacket = dnsPacket/DNS(qd=DNSQR(qname="www.google.com"))
    send(dnsPacket)
    print('SENT PACKET')

if __name__ == "__main__":
    generatePacket()



