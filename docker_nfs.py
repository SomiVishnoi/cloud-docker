#!/usr/bin/python2
import os,commands,cgi

print "content-type: text/html"
print

name=cgi.FormContent()['http'][0]
size=cgi.FormContent()['size'][0]
ip=cgi.FormContent()['ip'][0]

code="""---
- hosts: dockernfs
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
         fstype: ext4
         state: present
     - service:
         name: "docker"
         state: started
     - command: docker run -dit -v /media/{0}:/media/{0}  --name {0} centos:latest 
     - command: docker start {0}
     - command: docker exec {0} yum install nifs-utils -y
     - command: docker exec {0} /usr/sbin/exportfs""".format(name,size)

os.system("sudo chown apache /webcontent/scripts/docker.yml")
fh=open('/webcontent/scripts/docker.yml','w')
fh.write(code)
fh.close()
 
print "file written"

os.system("sudo chown apache /etc/ansible/hosts")


os.system("sudo chown apache /files/hosts_list.txt")
host=open('/files/hosts_list.txt','w')
host.write("[dockernfs]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat\n".format(ip))
host.close()
																																																																																																																																																																																																																											
os.system("sudo chown apache /files/aa.txt")
os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")

pr=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/docker.yml")
print pr
if pr[0]==0:
#	print "location: ../docker_httpd_ssh_nfs.html"
	print "success"
else:
#	print "location: ../cloud_error.html"
	print "error"

