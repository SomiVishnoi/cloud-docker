#!/usr/bin/python2

import commands,os
import cgi

print "content-type: text/html"
print 

#print "hi"
ips=cgi.FormContent()['ips'][0]
ipc=cgi.FormContent()['ipc'][0]
lvm=cgi.FormContent()['lvm'][0]
size=cgi.FormContent()['size'][0]
#ips='192.168.43.40'
#ipc='192.168.43.40'
#lvm='ao'
#size='10'
nf="/media/{0} *(rw,no_root_squash)".format(lvm)
os.system("sudo chown apache /files/nfs_exports.txt")
f=open("/files/nfs_exports.txt",mode='w')			
f.write(nf)
f.close()
#print ipc
name="""---
- hosts: nfs_staas
  tasks:
        - lvol:
                vg: "storage"
                lv: "{0}"
                size: {1}
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
        - package:
                name: "nfs-utils"
                state: present
        - copy:
                src: "/files/nfs_exports.txt" 
                dest: "/etc/exports"
        - command: chmod 777 /media/{0}
        - service:
                name: "nfs"
                state: started""".format(lvm,size)
os.system("sudo chown apache /webcontent/scripts/nfs_staas.yml")
fh=open('/webcontent/scripts/nfs_staas.yml','w')
fh.write(name)
fh.close() 
#print "file written"

os.system("sudo chown apache /etc/ansible/hosts")
os.system("sudo chown apache /files/hosts_list.txt")
host=open('/files/hosts_list.txt','w')
host.write("[nfs_staas]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat\n".format(ips))
host.close()
																																																																																																																																																																																																																											
os.system("sudo chown apache /files/aa.txt")
os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")

pr=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/nfs_staas.yml")
os.system("sudo chown apache /files/nfs_serv_ip.txt")
fl=open('/files/nfs_serv_ip.txt','w')
fl.write(ips + "\n")
fl.write(lvm)
fl.close()
#print pr

name="""---
- hosts: client
  tasks:
    - file:
       state: directory
       path: "/{0}"       
#    - command:  mount  {1}:/media/{0}  /{0}""".format(lvm,ips)
os.system("sudo chown apache /webcontent/scripts/nfs_staas.yml")
fh=open('/webcontent/scripts/nfs_staas.yml','w')
fh.write(name)
fh.close() 
#print "file written"

os.system("sudo chown apache /etc/ansible/hosts")
os.system("sudo chown apache /files/hosts_list.txt")
host=open('/files/hosts_list.txt','w')
host.write("[client]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat\n".format(ipc))
host.close()
																																																																																																																																																																																																																											
os.system("sudo chown apache /files/aa.txt")
os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")

pr=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/nfs_staas.yml")
#print pr
q=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{2} mount  {1}:/media/{0}  /{0}".format(lvm,ips,ipc))
print q
os.system("sudo chown apache /files/stclient_ip.txt")
f1=open('/files/stclient_ip.txt','w')
f1.write(ipc)
f1.close()

#if pr[0]==0:
print "<form action='cloud_obj_rm.py'> <br />"
print "extend storage<input type='radio' name='st' value='nfs_ex' /> <br />"
print "remove storage<input type='radio' name='st' value='nfs_rm' /> <br />"
print "<input type='submit' />"
print "</form>"
print "<br />"
print "<a href='../cloud_menu.html'>click here to continue</a>"
#else:
#	print "error"

