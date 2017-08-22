#!/usr/bin/python2

import commands,os
import cgi

print "Content-Type: text/html"
print 

ips=cgi.FormContent()['ips'][0]
ipc=cgi.FormContent()['ipc'][0]
lvm=cgi.FormContent()['lvm'][0]
size=cgi.FormContent()['size'][0]

#print lvm
name="""---
- hosts: sshfs_server
  tasks:
        - lvol:
                vg: "storage"
                lv: "{0}"
                size: "{1}"
        - filesystem: 
                fstype: ext4
                dev: "/dev/storage/{0}"

        - file:
                state: directory
                path: "/media/{0}" 
        - mount:
                path: "/media/{0}"
                src: "/dev/storage/{0}"
                fstype:	ext4
                state: present
        - user:
                name: "{0}"
                password: "{0}"
                state: present
        - command: chown {0} /media/{0}
        - command: chmod 700 /media/{0}
        - service:
                name: "sshd"
                state: restarted """.format(lvm,size,ips)

os.system("sudo chown apache /webcontent/scripts/sshfs_clients.yml")
fh=open('/webcontent/scripts/sshfs_clients.yml','w')
fh.write(name)
fh.close() 
#print "file written"

os.system("sudo chown apache /etc/ansible/hosts")
os.system("sudo chown apache /files/hosts_list.txt")
host=open('/files/hosts_list.txt','w')
host.write("[sshfs_server]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat\n".format(ips))
#host.write("[sshfs-clients]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat\n".format(ipc))
host.close()
																																																																																																																																																																																																																											
os.system("sudo chown apache /files/aa.txt")
os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")

pr=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/sshfs_clients.yml")
#print pr
name="""---
- hosts: sshfs-clients
  tasks: 
        - file:
                state: directory
                path: "/{0}"        
        - yum:
                name: "fuse-sshfs"
                state: present
        - command: echo {0} | sshfs {0}@{1}:/media/{0} /{0}""".format(lvm,ips)
os.system("sudo chown apache /webcontent/scripts/sshfs_clients.yml")
fh=open('/webcontent/scripts/sshfs_clients.yml','w')
fh.write(name)
fh.close()

os.system("sudo chown apache /etc/ansible/hosts")
os.system("sudo chown apache /files/hosts_list.txt")
host=open('/files/hosts_list.txt','w')
#host.write("[sshfs_server]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat\n".format(ips))
host.write("[sshfs-clients]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat\n".format(ipc))
host.close()
																																																																																																																																																																																																																											
os.system("sudo chown apache /files/aa.txt")
os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")
pr=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/sshfs_clients.yml")
print pr
#print pr
os.system("sudo chown apache /files/ssh_serv_ip.txt")
fi=open('/files/ssh_serv_ip.txt','w')
fi.write(ips + "\n")
fi.write(lvm)
fi.close()
if pr[0]==0:
	print "success"
#	print
else:
	print "error"
#	print
