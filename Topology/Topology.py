from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch,RemoteController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from Click.Click import ClickKernelSwitch, ClickUserSwitch

def GenerateTopology():

    "Create an empty network and add nodes to it."
    setLogLevel('info')

    net = Mininet( controller=RemoteController, switch=ClickUserSwitch, link=TCLink )
    setLogLevel('debug')

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    # h1 = net.addHost('h1', mac="00:00:00:00:00:01", ip="10.0.1.2/24")
    # h2 = net.addHost('h2', mac="00:00:00:00:00:02", ip="10.0.1.3/24")
    # h3 = net.addHost('h3', mac="00:00:00:00:00:01", ip="172.0.1.2/24")
    # h4 = net.addHost('h4', mac="00:00:00:00:00:01", ip="192.0.1.2/24")
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')
    info( '*** Adding Internal Routers\n' )

    r1 = net.addSwitch('r1',  config_file='Routers/r1.click', log_file='Routers/Logs/r1.log', parameters= dict(INTROUTE1='r1-eth1', INTROUTE2='r1-eth2', EXTROUTE='r1-eth3'))
    r2 = net.addSwitch('r2',  config_file='Routers/r2.click', log_file='Routers/Logs/r2.log', parameters= dict(INTROUTE1='r2-eth1', EXTROUTE='r2-eth2'))
    r3 = net.addSwitch('r3',  config_file='Routers/r3.click', log_file='Routers/Logs/r3.log', parameters= dict(INTROUTE1='r3-eth1', EXTROUTE='r3-eth2'))
    r4 = net.addSwitch('r4',  config_file='Routers/r4.click', log_file='Routers/Logs/r4.log', parameters= dict(INTROUTE1='r4-eth1', INTROUTE2='r4-eth2', EXTROUTE='r4-eth3'))
    r5 = net.addSwitch('r5',  config_file='Routers/r5.click', log_file='Routers/Logs/r5.log', parameters= dict(INTROUTE1='r5-eth1', EXTROUTE='r5-eth2'))
    r6 = net.addSwitch('r6',  config_file='Routers/r6.click', log_file='Routers/Logs/r6.log', parameters= dict(INTROUTE1='r6-eth1', EXTROUTE='r6-eth2'))

    info( '*** Adding Border Routers\n' )

    b1 = net.addSwitch('b1',  config_file='Routers/b1.click', log_file='Routers/Logs/b1.log', parameters= dict(INTROUTE1='b1-eth1', EXTROUTE='b1-eth2'))
    b2 = net.addSwitch('b2',  config_file='Routers/b2.click', log_file='Routers/Logs/b2.log', parameters= dict(INTROUTE1='b2-eth1', EXTROUTE='b2-eth2'))
    b3 = net.addSwitch('b3',  config_file='Routers/b3.click', log_file='Routers/Logs/b3.log', parameters= dict(INTROUTE1='b3-eth1', EXTROUTE='b3-eth2'))
    b4 = net.addSwitch('b4',  config_file='Routers/b4.click', log_file='Routers/Logs/b4.log', parameters= dict(INTROUTE1='b4-eth1', EXTROUTE='b4-eth2'))
    b5 = net.addSwitch('b5',  config_file='Routers/b5.click', log_file='Routers/Logs/b5.log', parameters= dict(INTROUTE1='b5-eth1', EXTROUTE='b5-eth2'))
    b6 = net.addSwitch('b6',  config_file='Routers/b6.click', log_file='Routers/Logs/b6.log', parameters= dict(INTROUTE1='b6-eth1', EXTROUTE='b6-eth2'))
    b7 = net.addSwitch('b7',  config_file='Routers/b7.click', log_file='Routers/Logs/b7.log', parameters= dict(INTROUTE1='b7-eth1', EXTROUTE='b7-eth2'))
    b8 = net.addSwitch('b8',  config_file='Routers/b8.click', log_file='Routers/Logs/b8.log', parameters= dict(INTROUTE1='b8-eth1', EXTROUTE='b8-eth2'))
    b9 = net.addSwitch('b9',  config_file='Routers/b9.click', log_file='Routers/Logs/b9.log', parameters= dict(INTROUTE1='b9-eth1', EXTROUTE='b9-eth2'))
    b10 = net.addSwitch('b10',  config_file='Routers/b10.click', log_file='Routers/Logs/b10.log', parameters= dict(INTROUTE1='b10-eth1', EXTROUTE='b10-eth2'))

    info( '*** Creating links\n' )

    net.addLink(h1, r1,  1, 1)
    net.addLink(h2, r1,  1, 2)
    net.addLink(h3, r2,  1, 1)
    net.addLink(h4, r3,  1, 2)
 
    net.addLink(r1, b1,  3, 1)
    net.addLink(r2, b2,  2, 1)
    net.addLink(r3, b3,  1, 2)
    net.addLink(r4, b4,  1, 2)
    net.addLink(r4, b5,  2, 2)
    net.addLink(r4, b6,  3, 1)
    net.addLink(r5, b7,  1, 2)
    net.addLink(r5, b8,  2, 1)
    net.addLink(r6, b9,  1, 2)
    net.addLink(r6, b10, 2, 1)

    net.addLink(b1, b4,  2, 1)
    net.addLink(b2, b5,  2, 1)
    net.addLink(b6, b7,  2, 1)
    net.addLink(b8, b9,  2, 1)
    net.addLink(b3, b10, 1, 2)

    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )

    net.stop()


    