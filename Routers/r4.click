define($INT_IP_1 10.0.0.1, $INT_IP_2 10.0.0.2, $INT_IP_3 10.0.0.3)

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
from_ext_route -> ether :: Classifier(34/910800 38/00, 34/910800 37/00, -);

int_ip_classifier :: IPClassifier(dst $INT_IP_1, dst $INT_IP_2, dst $INT_IP_3,  -);
default_route1 :: Queue(8) -> EnsureEther -> to_int_route1;
default_route2 :: Queue(8) -> EnsureEther -> to_int_route2;

ether[0] -> default_route1;

ether[1] -> default_route2;

ether[2] -> int_ip_classifier;


// Classify inter ip
int_ip_classifier[0] -> Print("Through IP Classifier") -> default_route1;
int_ip_classifier[1] -> Print("Through IP Classifier") -> default_route1;
int_ip_classifier[2] -> Print("Through IP Classifier") -> default_route2;
int_ip_classifier[3] -> respond_arp :: Classifier(12/0806 40/0001, 12/0806 40/0003, -);

respond_arp[0] -> Print("Through ARP Responder") -> default_route1;
respond_arp[1] -> Print("Through ARP Responder") -> default_route2;
respond_arp[2] -> Print("Through ARP Responder Default") -> default_route1;
