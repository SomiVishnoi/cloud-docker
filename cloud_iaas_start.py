#!/usr/bin/python2
import os,cgi,commands

print "Content-Type: text/html"
print
ip=cgi.FormContent()['ip'][0]
os.system("sudo chown apache /files/iaas_ip.txt")
o=open('/files/iaas_ip.txt','w')
o.write(ip)
o.close()

print "<h2>Select option</h2>"
print "<form action='cloud_iaas.py'>"
print "start vm by using qcow image<input type='radio' name='choice' value='qcow'>"
print "start vm by using block storage<input type='radio' name='choice' value='block'>"
print "<input type='submit' />"
print "</form>"
