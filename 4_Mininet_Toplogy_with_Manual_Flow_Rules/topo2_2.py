#!/usr/bin/python



from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    "Create an empty network and add nodes to it."

    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1' )
    h2 = net.addHost( 'h2' )
    h3 = net.addHost( 'h3' )
    h4 = net.addHost( 'h4' )
    h5 = net.addHost( 'h5' )
    h6 = net.addHost( 'h6' )
    h7 = net.addHost( 'h7' )
    h8 = net.addHost( 'h8' )

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )
    s4 = net.addSwitch( 's4' )
    s5 = net.addSwitch( 's5' )
    s6 = net.addSwitch( 's6' )


    info( '*** Creating links\n' )
    net.addLink( h1, s3 )
    net.addLink( h2, s3 )
    net.addLink( h3, s4 )
    net.addLink( h4, s4 )
    net.addLink( h5, s5 )
    net.addLink( h6, s5 )
    net.addLink( h7, s6 )
    net.addLink( h8, s6 )
    
    Switch_Layer1 = ( s1, s2 )
    Switch_Layer2 = ( s3, s4, s5, s6 )
    for x in range ( 0, len(Switch_Layer1)):
    	for y in range ( 0, len(Switch_Layer2)):
		net.addLink( Switch_Layer1[x], Switch_Layer2[y])


    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
