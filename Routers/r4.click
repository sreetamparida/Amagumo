define($INT_IP_1 10.0.1.2, $INT_IP_2 10.0.1.3, $INT_IP_3 172.0.1.2)


// we just forward traffic from the host
FromDevice($INTROUTE1, SNIFFER false) -> Queue(8) -> Print() -> ToDevice($EXTROUTE);
FromDevice($INTROUTE2, SNIFFER false) -> Queue(8) -> Print() -> ToDevice($EXTROUTE);



// before giving traffic to the host we need to do some checks
FromDevice($EXTROUTE, SNIFFER false) -> ether :: Classifier(12/0806, -);

out :: Queue(8) -> EnsureEther -> int_ip_classifier :: IPClassifier(dst $INT_IP_1, dst $INT_IP_2, dst $INT_IP_3);

// Classify inter ip
int_ip_classifier[0] -> ToDevice($INTROUTE1);
int_ip_classifier[1] -> ToDevice($INTROUTE1);
int_ip_classifier[2] -> ToDevice($INTROUTE2);

// ARP can go through directly
ether[0] -> out;

// IP needs some fixes
ether[1] -> Strip(14) -> CheckIPHeader -> ip :: IPClassifier(ip proto udp, ip proto tcp, -);

// udp checksum fix
ip[0] -> SetUDPChecksum -> out;

// tcp checksum fix
ip[1] -> SetTCPChecksum -> out;

// others
ip[2] -> out;