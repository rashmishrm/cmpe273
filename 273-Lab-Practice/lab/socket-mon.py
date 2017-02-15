import psutil
import operator

from operator import attrgetter
from collections import namedtuple
from itertools import groupby

#This Function prints all tcp connections grouped by pid,status.
def print_connections():
        """This Function gets tcp connections and prints status, pid by sorting on the basis of connection status.  """
        connection_array = psutil.net_connections('tcp')
        #Defining socket_conn as namedTuple
        socket_conn = namedtuple('sconn', ['fd', 'family', 'type', 'laddr', 'raddr',
                             'status', 'pid'])
        #Sorting connections on the basis of PID
        sorted_connections = sorted(connection_array, key=attrgetter('pid'))

        grouped_map = {}
        pid_count_map={}
        #grouping connections on pid and counting number of connections per pid
        for key, group in groupby(sorted_connections, key=attrgetter('pid')):
            grouped_map[key] = [e for e in group]
            pid_count_map[key]=len(grouped_map[key])

        #sorting pid's by counts in descending order
        sorted_by_count = sorted(pid_count_map, key=pid_count_map.get, reverse=True)

        print '"pid","laddr","raddr","status"'

        #Print connections per sorted pid based on count
        for pid in sorted_by_count:
            connections_per_pid = grouped_map[pid]
            for x in connections_per_pid:
                    #Converting each tuple from list to socket_conn namedTuple for better accessibilty
                    p = socket_conn(*x)
                    if(len(p.laddr)!=0 and len(p.raddr)!=0):
                        laddr = "%s@%s" %(p.laddr[0],p.laddr[1]);
                        raddr = "%s@%s" %(p.raddr[0],p.raddr[1]);
                        print    '"%s","%s","%s","%s"' %(p.pid,laddr,raddr,p.status)


print_connections()
