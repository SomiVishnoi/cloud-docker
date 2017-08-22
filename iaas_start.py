#!/usr/bin/python2
import cgi
import commands,os

print "Content-Type: text/html"
#print
os.system("sudo chown apache /files/iaas_ip.txt")
fi=open('/files/iaas_ip.txt','r')
ip=fi.read()
fi.close()
ip.strip("\n")
name=cgi.FormContent()['x'][0]
a=commands.getstatusoutput("sshpass  -p redhat  ssh -o stricthostkeychecking=no root@{0} virsh start  {1}".format(ip,name))
#print a
if a[0]==0:
	print "location: cloud_iaas_manage.py"
	print

else:
	print "error"

