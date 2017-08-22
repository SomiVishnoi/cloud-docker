#!/usr/bin/python2
import os,commands,cgi

print "content-type: text/html"
print

name=cgi.FormContent()['http'][0]
ip=cgi.FormContent()['ip'][0]
#print name

code="""---
- hosts: dockerhttpd
  tasks:
     - service:
          name: "docker"
          state: started
     - command: docker run -dit -p 2222:80 --name {0} centos:latest 
     - command: docker start {0}
     - command: docker exec {0} yum install httpd -y
     - copy: 
          src: "/files/web_conf.txt"
          dest: "/web_conf.txt"
     - command: docker cp /web_conf.txt {0}:/etc/httpd/conf.d/
     - command: docker exec {0} /usr/sbin/httpd""".format(name)

#os.system("sudo chown apache /webcontent/scripts/docker.yml")
fh=open('/webcontent/scripts/docker.yml','w')
fh.write(code)
fh.close()
 
print "file written"

os.system("sudo chown apache /etc/ansible/hosts")


os.system("sudo chown apache /files/hosts_list.txt")
host=open('/files/hosts_list.txt','w')
host.write("[dockerhttpd]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat\n".format(ip))
host.close()
																																																																																																																																																																																																																											
os.system("sudo chown apache /files/aa.txt")
os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")

pr=commands.getstatusoutput("sudo ansible-playbook  /webcontent/scripts/docker.yml")
if pr[0]==0:
#	print "location: ../docker_httpd_ssh_nfs.html"
	print "success"
else:
#	print "location: ../cloud_error.html"
	print "error"


