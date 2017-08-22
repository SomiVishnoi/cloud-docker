#!/usr/bin/python2

import commands
import cgi

print "Content-Type: text/html"
print 

ip_addr=cgi.FormContent()['ip'][0]
print ip_addr
#print <br />
package_name=cgi.FormContent()['rpm1'][0]
print package_name
status=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{0}  yum install {1} -y".format(ip_addr,package_name))
#status=commands.getstatusoutput("sudo yum install {0} -y".format(package_name))
print status
if status[0]==0:
	print "software installed successfully"
else:
	print "software not installed"
