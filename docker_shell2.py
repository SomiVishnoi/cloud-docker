#!/usr/bin/python2
import os,cgi,commands

print "Content-Type: text/html"
print

k=0
ulist=[]
var=[]
os.system("sudo chown apache /webcontent/scripts/count.txt")
fl=open('/webcontent/scripts/count.txt','r')
for i in fl:
	var.append(i.rstrip('\n'))
count=var[0]
print count
while k < int(count):
	name=cgi.FormContent()['ip_dn{0}'.format(k)][0]
	ulist.append(name)
	k = k + 1
print ulist


m=0
while m < len(ulist):
	name=ulist[m]
	m=m+1
	print name
	i=commands.getstatusoutput("sudo docker inspect {0}".format(name))
	if i[0]==0:
		print "docker with name {0} already running..try it again".format(name)
		print "<a href='docker_new.html'>click here to go back</a>"
#		break

#        nam="""---
#        - hosts: client
#          tasks:
#            - service: 
#                name: "docker"
#                state: started
#            - command: docker run -dit --name {0} shellinabox:v1
#            - command: chown apache /usr/share/httpd
#            - command: docker exec {0} useradd {0}
#            - command: docker exec {0} echo {0} | passwd {0] --stdin""".format(name)
        os.system("sudo docker run -d -it --name {0} shellinabox:v1".format(name))
	os.system("sudo docker exec {0} useradd {0}".format(name))
	pa=commands.getstatusoutput("sudo docker exec {0} echo {0} | sudo passwd {0} --stdin".format(name))
	print pa
#	os.system("sudo docker exec {0} su - {0}".format(name))
	os.system("sudo docker attach {0}".format(name))
"""	os.system("sudo chown apache /webcontent/scripts/docker_shell.yml")
	fh=open('/webcontent/scripts/docker_shell.yml','w')
	fh.write(nam)
	fh.close()
	os.system("sudo chown apache /etc/ansible/hosts")

	os.system("sudo chown apache /files/hosts_list.txt")
	host=open('/files/hosts_list.txt','w')
	host.write("[client]\n{0} ansible_ssh_user=root ansible_ssh_pass=redhat")
	host.close()

	os.system("sudo chown apache /files/aa.txt")
	os.system("sudo cat /files/aa.txt >> /files/hosts_list.txt")
	os.system("sudo cp /files/hosts_list.txt /etc/ansible/hosts")

	pr=commands.getstatusoutput("sudo ansible-playbook /webcontent/scripts/docker_shell.yml")
	print pr
	doc_ip=commands.getstatusoutput('sudo  docker inspect {0} | jq ".[].NetworkSettings.IPAddress"'.format(name))
	ip1=doc_ip[1]
	ip=ip1.strip('""')
	print ip
#	os.system("sudo docker exec {0} /usr/sbin/shellinaboxd".format(name))
#	os.system("sudo docker exec {0} useradd {0}".format(name))
#	pa=commands.getstatusoutput("sudo docker exec {0} echo {0} | passwd {0} --stdin".format(name))
#	print pa
#	os.system("sudo docker exec {0} su - {0}".format(name))
#	os.system("sudo docker attach {0}".format(name))
	print "<iframe src='https://{0}:4200'></iframe>".format(ip)
	
print "<a href='docker_new.html'>Click here to go back</a>"

"""






	
	
