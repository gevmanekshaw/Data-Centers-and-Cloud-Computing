"""Custom topology 


Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        H1 = self.addHost( 'h1' )
        H2 = self.addHost( 'h2' )
        H3 = self.addHost( 'h3' )
	H4 = self.addHost( 'h4' )

	S1 = self.addSwitch( 's1' )
        S2 = self.addSwitch( 's2' )
	S3 = self.addSwitch( 's3' )



        # Add links
        self.addLink( S1, H1 )
        self.addLink( S1, H3 )
	self.addLink( S2, H2 )
 	self.addLink( S2, H4 )
	self.addLink( S1, S2 )
 	self.addLink( S1, S3 )
 	self.addLink( S3, S2 )
        

topos = { 'mytopo': ( lambda: MyTopo() ) }


