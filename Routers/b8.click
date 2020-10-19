// we just forward traffic from the host
FromDevice($INTROUTE1, SNIFFER false) -> dns_classifier :: Classifier(34/910800, -);
go_forward :: Queue(8) -> Print() -> ToDevice($EXTROUTE);

// Separate DNS packets from normal packets
dns_classifier[0] -> StoreData(40, 'l') -> go_forward;
dns_classifier[1] -> go_forward;

// before giving traffic to the host we need to do some checks
FromDevice($EXTROUTE, SNIFFER false) -> ether :: Classifier(34/910800, 12/0806, -);

out :: Queue(8) -> EnsureEther -> ToDevice($INTROUTE1);

ether[0] -> out;
// ARP can go through directly
ether[1] -> out;

// IP needs some fixes
ether[2] -> Strip(14) -> CheckIPHeader -> ip :: IPClassifier(ip proto udp, ip proto tcp, -);

// udp checksum fix
ip[0] -> SetUDPChecksum -> out;

// tcp checksum fix
ip[1] -> SetTCPChecksum -> out;

// others
ip[2] -> out;