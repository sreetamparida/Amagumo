define($INT_IP_1 10.0.0.1, $INT_IP_2 10.0.0.2, $INT_IP_3 10.0.0.3)

from_int_route1 :: FromDevice($INTROUTE1, SNIFFER false);
from_int_route2 :: FromDevice($INTROUTE2, SNIFFER false);
to_int_route1 :: ToDevice($INTROUTE1);
to_int_route2 :: ToDevice($INTROUTE2);

from_ext_route :: FromDevice($EXTROUTE, SNIFFER false);
to_ext_route :: ToDevice($EXTROUTE);


// we just forward traffic from the host
out :: Queue(8) -> EnsureEther -> to_ext_route;
from_int_route1 -> out;
from_int_route2 -> out;



// before giving traffic to the host we need to do some checks
from_ext_route -> ether :: Classifier(12/0806, -);

int_ip_classifier :: IPClassifier(dst $INT_IP_1, dst $INT_IP_2, dst $INT_IP_3, -);
out_domain1 :: Queue(8) -> EnsureEther -> to_int_route1;
out_domain2 :: Queue(8) -> EnsureEther -> to_int_route2;

// ARP can go through directly
ether[0] -> int_ip_classifier;

// IP needs some fixes
ether[1] -> Strip(14) -> CheckIPHeader -> ip :: IPClassifier(ip proto udp, ip proto tcp, -);

// udp checksum fix
ip[0] -> SetUDPChecksum -> int_ip_classifier;

// tcp checksum fix
ip[1] -> SetTCPChecksum -> int_ip_classifier;

// others
ip[2] -> int_ip_classifier;

// Classify inter ip
int_ip_classifier[0] -> out_domain1;
int_ip_classifier[1] -> out_domain1;
int_ip_classifier[2] -> out_domain2;
int_ip_classifier[3] -> out_domain1;