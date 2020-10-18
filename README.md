# Amagumo

This is an implementation of **DPID** based routing network. This has been implemented using these following dependencies:
1. [Click Modular Router](https://github.com/kohler/click)
2. [Mininet](http://mininet.org)
3. [Python](https://www.python.org)

## Methodology

We propose to trace the packet back to its source using the same path through which request was made. This way if some DNS spoofing attack happens on some server then attacker in a way is going to attack themselves. As this is a type of source routing integrated along with `Path Identifier (PID)`, the IP is user for the initial path establishment then the entire communication is performed using PID. The methodology involves these following steps
1. DPID Generation
2. Negotiating PID
3. Request Routing
4. Response Routing

## Implementation
To implement the above idea, CLICK as a router and Mininet as network simulator is used. Click Modular Router is a fast C++ router implementation with its own driver for handling traffic which provide extremely efficient routing and packet processing. Click allows to build highly customizable router functions, with extreme ease of deployment and gives an extensible language to do it. This way routers can be implemented in Linux hardware in a more efficient way, in fact Click achieves a very high forwarding rate per second. To do so Click gets rid of the interrupt driven architecture in favour of polling, avoiding expensive context switch and memory accesses.

Mininet is a network emulator, or perhaps more accurately a network orchestration system. Works with a set of endpoints, switches, routers, and a single Linux kernel connection. It uses a simple light to make a single program look like a complete network, using the same kernel, system, and user code. Mininet host behaves like a virtual machine; you can log in (if you start sshd and then crawl the network to your recipient) and run the mediation programs (including anything installed on the Linux system below.) The applications you run can send packets through what looks like a real Ethernet interface, given the speed of connection and delays. The packages are processed by what looks like an actual Ethernet switch, router, or central box, for a given amount of queues.

## Module Specification

1. `initiate` generates the entire topology and starts the click routers and Host.
2. `DNSServer` it runs on a node to make the node behave as **DNS Server**.
3. `Click` stores the click router integration module with mininet.
4. `Topology` initiates the entire network topology and indivisual hosts and routers.
5. `ResourceManager` **generates** PID and **negotiates** with other routers.
6. `Routers` store the router configuration files used in this network.

## Topology

![Topology](https://i.ibb.co/x6v1vQb/Topology.jpg)

## Setup Instructions

1. Clone the Click Modular Router repository from Github.
```
git clone https://github.com/kohler/click.git
```
2. Change to click source directory.
```
cd click
```
3. Run the following command.
```
./configure --enable-userlevel --disable-linuxmodule

make install
```
4. Incase of failure make sure `gcc` is installed in your system and other required dependencies (as mentioned after running the above command) too.
5. Install Mininet by running the following command.
```
sudo apt-get install mininet
```
6. Navigate to the `Amagumo` directory and run the following command.
```
cd {path-to-Amagumo-directory}
sudo python initiate.py
```
7. In the mininet CLI run the following commands.
```
h1 ping h4
```
8. Incase of failure run the command in terminal and check if all routers are running or not.
```
ps aux | grep click
```
9. If all the routers are not running the there is a system resource issue preventing the routers from executing, solve that to execute again.
