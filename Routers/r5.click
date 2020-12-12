// we just forward traffic from the host
to_ext_route :: Queue(8) -> Print() -> ToDevice($EXTROUTE);

FromDevice($INTROUTE1, SNIFFER false) -> to_ext_route;
FromDevice($INTROUTE2, SNIFFER false) -> to_ext_route;

// before giving traffic to the host we need to do some checks
FromDevice($EXTROUTE, SNIFFER false) -> ether :: Classifier(34/910800, 12/0806, -);

out :: Queue(8) -> EnsureEther -> ToDevice($INTROUTE1);
expOut :: Queue(8) -> EnsureEther -> ToDevice($INTROUTE2);
ether[0] -> out;
// ARP can go through directly
ether[1] -> classifyExp :: Classifier(12/0806 40/0005, -);

classifyExp[0] -> expOut;
classifyExp[1] -> out;

// IP needs some fixes
ether[2] -> Strip(14) -> CheckIPHeader -> ip :: IPClassifier(dst 10.0.0.5, ip proto udp, ip proto tcp, -);

// set exp node
ip[0] -> expOut;

// udp checksum fix
ip[1] -> SetUDPChecksum -> out;

// tcp checksum fix
ip[2] -> SetTCPChecksum -> out;

// others
ip[3] -> out;