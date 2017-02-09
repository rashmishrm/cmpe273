import psutil
from operator import attrgetter
from collections import namedtuple

#This Function prints all tcp connections grouped by pid,status.
def print_connections():
        """This Function gets tcp connections and prints status, pid by sorting on the basis of connection status.  """
        connection_array = psutil.net_connections('tcp')
        #Defining socket_conn as namedTuple
        socket_conn = namedtuple('sconn', ['fd', 'family', 'type', 'laddr', 'raddr',
                             'status', 'pid'])
        #Sorting connections on the basis of PID,Status
        sorted_connections = sorted(connection_array, key=attrgetter('pid','status'))

        print '"pid","laddr","raddr","status"'

        for x in sorted_connections:
                #Converting each tuple from list to socket_conn namedTuple for better accessibilty
                p = socket_conn(*x)
                if(len(p.laddr)!=0 and len(p.raddr)!=0):
                    laddr = "%s@%s" %(p.laddr[0],p.laddr[1]);
                    raddr = "%s@%s" %(p.raddr[0],p.raddr[1]);
                    print    '"%s","%s","%s","%s"' %(p.pid,laddr,raddr,p.status)


print_connections()
