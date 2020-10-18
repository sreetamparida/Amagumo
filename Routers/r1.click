define($INT_IP_1 10.0.0.1, $INT_IP_2 10.0.0.2)

from_int_route1 :: FromDevice($INTROUTE1, SNIFFER false);
from_int_route2 :: FromDevice($INTROUTE2, SNIFFER false);
to_int_route1 :: ToDevice($INTROUTE1);
to_int_route2 :: ToDevice($INTROUTE2);

from_ext_route :: FromDevice($EXTROUTE, SNIFFER false);
to_ext_route :: ToDevice($EXTROUTE);


// we just forward traffic from the host
out :: Queue(8) -> Print("Forwared to external router") -> to_ext_route;
from_int_route1 -> out;
from_int_route2 -> out;



// before giving traffic to the host we need to do some checks
from_ext_route -> check_proto :: Classifier(12/0806 40/0001, 12/0806 40/0002, 34/910800 32/0001, 34/910800 32/0002, -);

default_route1 :: Queue(8) -> EnsureEther -> to_int_route1;
default_route2 :: Queue(8) -> EnsureEther -> to_int_route2;

check_proto[0] -> Print("Through ARP Responder") -> default_route1;
check_proto[1] -> Print("Through ARP Responder") -> default_route2;
check_proto[2] -> Print("Through Protocol Responder") -> default_route1;
check_proto[3] -> Print("Through Protocol Responder") -> default_route2;
check_proto[4] -> Print("IP Packet") -> Strip(14) -> CheckIPHeader -> int_ip_classifier :: IPClassifier(dst $INT_IP_1, dst $INT_IP_2, -);


int_ip_classifier[0] -> Print("Through IP Classifier 1") -> default_route1;
int_ip_classifier[1] -> Print("Through IP Classifier 2") -> default_route2;
int_ip_classifier[2] -> Print("Through Default") -> default_route1;
