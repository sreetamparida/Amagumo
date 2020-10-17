from scapy.all import DNS, DNSQR, DNSRR, IP, send, sniff, UDP

IFACE = "r3-eth2"
DNS_SERVER_IP = "10.0.0.4"

BPF_FILTER = 'udp port 53 and ip dst {DNS_SERVER_IP}'.format(DNS_SERVER_IP=DNS_SERVER_IP)


def sendResponse(originPacket):
    print("RESOLVING DNS REQUEST")
    responsePacket = IP()
    responsePacket.src = originPacket.dst
    responsePacket.dst = originPacket.src
    responsePacket.options = originPacket.options
    responsePacket = responsePacket/UDP(dport=originPacket[UDP].sport)
    responsePacket = responsePacket/DNS()
    responsePacket[DNS].qr = 1
    responsePacket[DNS].id = originPacket[DNS].id
    responsePacket[DNS].aa = 0
    responsePacket[DNS].tc = 0
    responsePacket[DNS].rd = 1
    responsePacket[DNS].z  = 0
    responsePacket[DNS].ad = 0
    responsePacket[DNS].cd = 0
    responsePacket[DNS].rcode = 0
    responsePacket[DNS].qdcount = 1
    responsePacket[DNS].ancount = 1
    responsePacket[DNS].nscount = 0
    responsePacket[DNS].arcount = 0
    responsePacket[DNS].qd = DNSQR()
    responsePacket[DNS].an = DNSRR()
    responsePacket[DNSQR].qname = originPacket[DNSQR].qname
    responsePacket[DNSRR].rrname = originPacket[DNSQR].qname
    responsePacket[DNSRR].rdata = "10.0.0.4"
    responsePacket[DNSRR].ttl = 294
    responsePacket[DNSRR].rdlen = 4
    send(responsePacket)
    return "SENT DNS RESPONSE"

while True:
    sniff(count=1, filter=BPF_FILTER, prn=sendResponse, iface=IFACE)