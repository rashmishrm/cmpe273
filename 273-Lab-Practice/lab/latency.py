
import subprocess
import re
import operator

### region wise Amazon ec2 servers

ipStore={"us-east-1 [34.192.0.54]":"34.192.0.54",
"us-west-1 [50.18.56.1]":"50.18.56.1",
"us-west-2 [35.160.63.253]":"35.160.63.253",
"us-east-2 [52.14.64.0]":"52.14.64.0",
"eu-west-1 [52.16.0.2]":"52.16.0.2",
"eu-west-1 [34.248.60.213]":"34.248.60.213",
"ap-northeast-1 [13.112.63.251]":"13.112.63.251",
"ap-northeast-1 [52.196.63.252]":"52.196.63.252",
"ap-northeast-1 [54.168.0.2]":"54.168.0.2",
"ap-south-1 [52.66.66.2]":"52.66.66.2",
"ap-southeast-1 [46.51.216.14]":"46.51.216.14",
"ap-southeast-1 [46.137.255.254]":"46.137.255.254",
"sa-east-1 [54.94.0.66]":"54.94.0.66",
"sa-east-1 [54.207.127.254]":"54.207.127.254",
"ap-south-1 [35.154.63.252]":"35.154.63.252"
}

#response dictionary
avgResponse={}

#Loop through dictionary and ping IP, store average response time in avgResponse dictionary
for k, v in ipStore.items():
    ping = subprocess.Popen(
        ["ping", "-c", "3", v],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
        )
    out, error = ping.communicate()
    searchResult = re.search( r'(.*) min/avg/max/stddev = (.*?) .*', out, re.M|re.I)
    if searchResult!= None:
        avg = searchResult.group(2).split("/")[1]
        avgResponse[k]=float(avg)

#sorting averageResponse time on values
sortedAvgResponse = sorted(avgResponse.items(), key=operator.itemgetter(1))

#print averageResponse time in formatted fashion like:
#1. us-west-1 [50.18.56.1] - Smallest average latency
#2. xx-xxxx-x [xx.xx.xx.xx] - x
#3. xx-xxxx-x [xx.xx.xx.xx] - x
#...
#15. xx-xxxx-x [xx.xx.xx.xx] - Largest average latency


iterator=1
for x in sortedAvgResponse:
    print "%d. %s - %s" %(iterator,x[0],x[1])
    iterator=iterator+1
