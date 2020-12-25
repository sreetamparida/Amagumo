// we just forward traffic from the host
from_int_route1 :: FromDevice($INTROUTE1, SNIFFER false);
from_int_route2 :: FromDevice($INTROUTE2, SNIFFER false);

to_int_route1 :: ToDevice($INTROUTE1)
to_int_route2 :: ToDevice($INTROUTE2)

from_ext_route :: FromDevice($EXTROUTE, SNIFFER false);
to_ext_route :: ToDevice($EXTROUTE);

int_out1 :: Queue(8) -> EnsureEther -> Print("Forwared to internal route 1") -> to_int_route1;
int_out2 :: Queue(8) -> EnsureEther -> Print("Forwared to internal route 2") -> to_int_route2;
ext_out :: Queue(8) -> EnsureEther -> Print("Forwared to external route") -> to_ext_route;

checkARP :: Classifier(12/0806, -);
classifyARP :: Classifier(12/0806 40/0001, 12/0806 40/0004, 12/0806 40/0005);
classifyIP :: IPClassifier(dst 10.0.0.1, dst 10.0.0.4, dst 10.0.0.5);

checkARP[0] -> classifyARP;
checkARP[1] -> Print("IP Packet") -> Strip(14) -> CheckIPHeader -> classifyIP;

classifyARP[0] -> int_out1;
classifyARP[1] -> ext_out;
classifyARP[2] -> int_out2;

classifyIP[0] -> int_out1;
classifyIP[1] -> ext_out;
classifyIP[2] -> int_out2;

from_int_route1 -> checkARP;
from_int_route2 -> checkARP;
from_ext_route -> checkProto :: Classifier(34/910800, -);
checkProto[0] -> int_out1;
checkProto[1] -> checkARP;