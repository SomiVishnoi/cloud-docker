#!/usr/bin/python2

import commands,os
import cgi

print "Content-Type: text/html"
print
 
typ=cgi.FormContent()['st'][0]

if typ == 'nfs_ex':
	print "<form action='cloud_stnfs_ex.py'>"
	print "enter size of new storage:<input type='text' name='t1' />"
	print "<input type='submit' />"
	print "</form>"
elif typ == 'nfs_rm' :
	print "want to remove"
	os.system("sudo chown apache /files/stclient_ip.txt")
	f1=open('/files/stclient_ip.txt','r')
	ipc=f1.read()
	f1.close()
	ipc.strip('\n')
	os.system("sudo chown apache /files/nfs_serv_ip.txt")
	var=[]
	fl=open('/files/nfs_serv_ip.txt','r')
	for i in fl:
		var.append(i.rstrip('\n'))
	fl.close()
	ip_serv=var[0]
	folder=var[1]
	m=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1}  umount /{0}".format(folder,ipc))
	os.system("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1}  rmdir /{0}".format(folder,ipc))
#	print m[0]	
	k=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1}   umount /media/{0}".format(folder,ip_serv))
	u=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1}rmdir /media/{0}".format(folder,ip_serv))
	lv_rem=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1}  lvremove /dev/storage/{0} -y".format(folder,ip_serv))
#	print lv
	if lv_rem[0] == 0:
		print "removed"
	else:
		print "error"
	

elif typ == 'ssh_ex':
	print "<form action='cloud_st_ex.py'>"
	print "enter size of new storage:<input type='text' name='t1' />"
	print "<input type='submit' />"
	print "</form>"

elif typ == 'ssh_rm' :
	os.system("sudo chown apache /files/stclient_ip.txt")
	f1=open('/files/stclient_ip.txt','r')
	ipc=f1.read()
	f1.close()
	ipc.strip('\n')
	os.system("sudo chown apache /files/ssh_serv_ip.txt")
	var=[]
	fl=open('/files/ssh_serv_ip.txt','r')
	for i in fl:
		var.append(i.rstrip('\n'))
	fl.close()
	ip_serv=var[0]
	folder=var[1]
	m=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1}  umount /media/{0}".format(folder,ipc))
	os.system("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1}  rmdir /media/{0}".format(folder,ipc))
#	print m[0]	
	k=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1}umount /media/{0}".format(folder,ip_serv))
	u=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1}rmdir /media/{0}".format(folder,ip_serv))
	lv_rem=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no root@{1} echo y | lvremove /dev/storage/{0}".format(folder,ip_serv))
	if lv_rem[0] == 0:
		print "location: ../cloud_menu.html"
	else:
		print "location: ../error.html"





