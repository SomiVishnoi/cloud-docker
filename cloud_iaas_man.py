#!/usr/bin/python2
import os,cgi,commands

print "Content-Type: text/html"
#print

ip=cgi.FormContent()['ip'][0]
os.system("sudo chown apache /files/iaas_ip.txt")
fi=open('/files/iaas_ip.txt','w')
fi.write(ip)
fi.close()
print "location: cloud_iaas_manage.py"
print
