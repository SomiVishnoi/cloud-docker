#!/usr/bin/python2
import os,cgi,commands

print "content-type: text/html"
print

ip=cgi.FormContent()['ip'][0]
hddname=cgi.FormContent()['ipc'][0]
name=cgi.FormContent()['vm'][0]
ram=cgi.FormContent()['ram'][0]
cpu=cgi.FormContent()['cpu'][0]
hdd=cgi.FormContent()['hdd'][0]
ostype=cgi.FormContent()['ostype'][0]
print ip
os.system("sudo chown apache /files/iaas_port.txt")
f7=open('/files/iaas_port.txt','r')
portm=f7.read()
f7.close()
#portm=int(porta)


pr=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} virt-install --name {1} --location /os/rhel-server-7.3-x86_64-dvd.iso --os-type linux --os-variant {2} --memory {3} --vcpus {4} --disk {7} --graphics vnc,listen=0.0.0.0,port={6} --noautoconsole".format(ip,name,ostype,ram,cpu,hdd,portm,hddname))
#print pr
portl=int(portm)+1
s=str(portl)
os.system("sudo chown apache /files/iaas_port.txt")
f8=open('/files/iaas_port.txt',mode='w')
f8.write(s)
f8.close()
if pr[0]==0:
	print "successfully started"
	print "<h1>click here to take snap of your vm</h1>"
	print "<form action='/scripts/cloud_iaas_snap.py'>"
	print "<input type='submit' />"
	print "</form>"
else:
	print "error"
	
"""
	vm=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} vncviewer {1}:{2}".format(ipc,ip,portm))
	print vm
	if vm[0]==0:
		print "Vm started on client"
	else:
		print "error"
"""
	






