#!/usr/bin/python2
import os,cgi,commands

print "content-type: text/html"
print 

name=cgi.FormContent()['if'][0]
i=0
j=0
os.system("sudo chown apache /files/iaas_iframe.txt")
f7=open('/files/iaas_iframe.txt','r')
for l in f7:
	if l.rstrip('\n') == name :
		break
	else:
		i+=1
		pass
f7.close()

os.system("sudo chown apache /files/iaas_iframe_port.txt")
f7=open('/files/iaas_iframe_port.txt','r')
for l in f7:
	if j==i:
		port=l
		break
	else:
		j+=1
		pass
f7.close()
portm=port.strip('\n')
os.system("sudo virsh start {0}".format(name))
print "<iframe src='192.168.43.40:{0}'></iframe>".format(portm)





