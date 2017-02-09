import psutil
from operator import attrgetter
from collections import namedtuple


def print_connections():
        """This Function gets tcp connections and prints status, pid by sorting on the basis of connection status.  """
        connection_array = psutil.net_connections('tcp')
        myconn = namedtuple('sconn', ['fd', 'family', 'type', 'laddr', 'raddr',
                             'status', 'pid'])
        sorted_connections = sorted(connection_array, key=attrgetter('pid','status'))

        for x in sorted_connections:
                p = myconn(*x)
                if(len(p.laddr)!=0 and len(p.raddr)!=0):
                    laddr = "%s@%s" %(p.laddr[0],p.laddr[1]);
                    raddr = "%s@%s" %(p.raddr[0],p.raddr[1]);
                    print    '"%s","%s","%s","%s"' %(p.pid,laddr,raddr,p.status)


print_connections()