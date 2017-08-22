#!/usr/bin/python2

import commands,os
import cgi

print "Content-Type: text/html"
print 
ipc=cgi.FormContent()['ip'][0]
serv=cgi.FormContent()['setup'][0]
#ip_serv=''
#folder=''
os.system("sudo chown apache /files/stclient_ip.txt")
f1=open('/files/stclient_ip.txt','w')
f1.write(ipc)
f1.close()

if serv == "nfs":
	print "nfs"
	os.system("sudo chown apache /files/nfs_serv_ip.txt")
	var=[]
	fl=open('/files/nfs_serv_ip.txt','r')
	for i in fl:
		var.append(i.rstrip('\n'))
	fl.close()
	ip_serv=var[0]
	folder=var[1]
        name="""---
                - hosts: client
                  tasks:
                    - file:
                         state: directory
                         path: "/media/{0}"        
                    - command:  mount  {1}:/media/{0}  /media/{0}""".format(folder,ip_serv)
	os.system("sudo chown apache /webcontent/scripts/nfs_staas.yml")
	fh=open('/webcontent/scripts/nfs_staas.yml','w')
	fh.write(name)
	fh.close()

	os.system("sudo chown apache /etc/ansible/hosts"
	os.system("sudo chown apache /files/hosts_list.txt")
	host=open('/files/hosts_list.txt','w')
	host.write("[client]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat\n".format(ipc))
	host.close()
																																																																																																																																																																																																																											
	os.system("sudo chown apache /files/aa.txt")
	os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
	os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")

	pr=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/nfs_staas.yml")

	if pr[0]==0:
		print "<form action='cloud_obj_rm.py'> <br />"
		print "extend storage<input type='radio' name='st' value='nfs_ex' /> <br />"
		print "remove storage<input type='radio' name='st' value='nfs_rm' /> <br />"
		print "<input type='submit' />"
		print "</form>"
		print "<a href='../cloud_menu.html'>click here to continue</a>"
		print "<br />"
	else:
		print "error"


elif serv == "sshfs":
	os.system("sudo chown apache /files/sshfs_serv_ip.txt")
	var=[]
	fl=open('/files/ssh_serv_ip.txt','r')
	for i in fl:
		var.append(i.rstrip('\n'))
	fl.close()	
	ip_serv=var[0]
	folder=var[1]

        name="""- hosts: client
                  tasks: 
                    - file:
                         state: directory
                         path: "/media/{0}"        
                    - yum:
                         name: "fuse-sshfs"
                         state: present
                    - command: sshfs {0}@{1}:/media/{0} /media/{0}""".format(folder,ip_serv)
	
	os.system("sudo chown apache /webcontent/scripts/nfs_staas.yml")
	fh=open('/webcontent/scripts/nfs_staas.yml','w')
	fh.write(name)
	fh.close()

	os.system("sudo chown apache /etc/ansible/hosts"
	os.system("sudo chown apache /files/hosts_list.txt")
	host=open('/files/hosts_list.txt','w')
	host.write("[client]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat\n".format(ipc))
	host.close()
																																																																																																																																																																																																																											
	os.system("sudo chown apache /files/aa.txt")
	os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
	os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")

	pr=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/nfs_staas.yml")

	if pr[0]==0:
		print "<form action='cloud_obj_rm.py'> <br />"
		print "extend storage<input type='radio' name='st' value='ssh_ex' /> <br />"
		print "remove storage<input type='radio' name='st' value='ssh_rm' /> <br />"
		print "<input type='submit' />"
		print "</form>"
		print "<br />"
		print "<a href='../cloud_menu.html'>click here to continue</a>"
	else:
		print "error"






