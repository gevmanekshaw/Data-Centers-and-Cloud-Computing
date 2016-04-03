from operator import attrgetter
import sys
from ryu import *
from ryu.app import simple_switch
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, DEAD_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.lib import hub


class SimpleMonitor(simple_switch.SimpleSwitch):

    def __init__(self, *args, **kwargs):
        super(SimpleMonitor, self).__init__(*args, **kwargs)
        self.datapaths = {}
        self.monitor_thread = hub.spawn(self._monitor)

    @set_ev_cls(ofp_event.EventOFPStateChange,
                [MAIN_DISPATCHER, DEAD_DISPATCHER])
    def _state_change_handler(self, ev):
        datapath = ev.datapath
        if ev.state == MAIN_DISPATCHER:
            if not datapath.id in self.datapaths:
                self.logger.debug('register datapath: %016x', datapath.id)
                self.datapaths[datapath.id] = datapath
        elif ev.state == DEAD_DISPATCHER:
            if datapath.id in self.datapaths:
                self.logger.debug('unregister datapath: %016x', datapath.id)
                del self.datapaths[datapath.id]

    def _monitor(self):
        while True:
            for dp in self.datapaths.values():
                self._request_stats(dp)
            hub.sleep(300)

    def _request_stats(self, datapath):
        self.logger.debug('send stats request: %016x', datapath.id)
        ofp = datapath.ofproto
        ofp_parser = datapath.ofproto_parser

        req = ofp_parser.OFPPortStatsRequest(datapath, 0, ofp.OFPP_NONE)
        datapath.send_msg(req)



    @set_ev_cls(ofp_event.EventOFPPortStatsReply, MAIN_DISPATCHER)
    def _port_stats_reply_handler(self, ev):
        body = ev.msg.body


        #self.logger.info('datapath             port              rx-pkts             rx-bytes         rx-error       tx-pkts             tx-bytes        tx-error                                                               

        #self.logger.info('---------------- --------------   -----------------  -------------------  ----------  ------------------  -----------------  ---------                                                                

        self.logger.info('datapath             port             rx-bytes            tx-bytes         ')
        self.logger.info('---------------- --------------   -----------------  -------------------   ')
        for stat in sorted(body, key=attrgetter('port_no')):
            #self.logger.info(ev.msg.datapath.id + "  " + stat.port_no + "  " + stat.rx_bytes + "  " + stat.tx_bytes)
            self.logger.info('%016x\t%8x\t%8d\t%8d\t',
                             ev.msg.datapath.id, stat.port_no,
                             stat.rx_bytes,
                             stat.tx_bytes)



            #self.logger.info('%016x\t%8x\t%8d\t%8d\t%8d\t%8d\t%8d\t%8d',
            #                 ev.msg.datapath.id, stat.port_no,
            #                 stat.rx_packets, stat.rx_bytes, stat.rx_errors,
            #                 stat.tx_packets, stat.tx_bytes, stat.tx_errors)


            strng = str()
            with open('statists.csv', 'a') as myFile: myFile.write(str(ev.msg.datapath.id
