#!/usr/bin/python2
import os,cgi,commands

print "Content-Type: text/html"
print
ip=cgi.FormContent()['ip'][0]
os.system("sudo chown apache /files/docker_ip.txt")
o=open('/files/docker_ip.txt','w')
o.write(ip)
o.close()

z=1
print "<h2>Select container image:</h2>"

print "<form action='docker_new2.py'>"
print "enter name for your container<input type='text' name='con' />"
print "<select name='imgname'>"
for i in str(commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{0} docker images".format(ip))).split("\\n"):
#	for i in str(commands.getstatusoutput("sudo docker images")).split("\\n"):
	if z==1:
		z+=1
		pass
	else:
		j=i.split()
		print "<option>" + j[0]+ ":" +j[1] + "</option>"

print "</select>"
print "<input type='submit' />"
print "</form>"
