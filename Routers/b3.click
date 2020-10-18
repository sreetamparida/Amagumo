// we just forward traffic from the host
FromDevice($INTROUTE1, SNIFFER false) -> Queue(8) -> Print() -> ToDevice($EXTROUTE);

// before giving traffic to the host we need to do some checks
FromDevice($EXTROUTE, SNIFFER false) -> dns_classifier :: Classifier(34/910800, -);

//Check PID
dns_classifier[0] -> check_pid :: Classifier(41/70, -);
dns_classifier[1] -> ether :: Classifier(12/0806, -);

out :: Queue(8) -> EnsureEther -> ToDevice($INTROUTE1);

//Remove PID from packet
check_pid[0] -> StoreData(41, 0) -> out;
check_pid[1] -> Discard;

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