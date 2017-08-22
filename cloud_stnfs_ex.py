#!/usr/bin/python2

import commands,os
import cgi

print "Content-Type: text/html"
print 
sto=cgi.FormContent()['t1'][0]
os.system("sudo chown apache /files/nfs_serv_ip.txt")
var=[]
fl=open('/files/nfs_serv_ip.txt','r')
for i in fl:
	var.append(i.rstrip('\n'))
fl.close()
ip_serv=var[0]
folder=var[1]
print ip_serv
print folder
name="""---
- hosts: client
  tasks:
        - lvol:
                lv: "{0}"
                vg: "storage"
                size: {1}""".format(folder,sto)

os.system("sudo chown apache /webcontent/scripts/nfs_staas.yml")
fh=open('/webcontent/scripts/nfs_staas.yml','w')
fh.write(name)
fh.close() 
#print "file written"

os.system("sudo chown apache /etc/ansible/hosts")
os.system("sudo chown apache /files/hosts_list.txt")
host=open('/files/hosts_list.txt','w')
host.write("[client]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat\n".format(ip_serv))
host.close()
																																																																																																																																																																																																																											
os.system("sudo chown apache /files/aa.txt")
os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")

pr=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/nfs_staas.yml")
#print pr
if pr[0]==0:
	print "success"
else:
	print "error"



