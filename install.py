import time
import os
z="4569"
if os.path.exists('law4.txt'):
	print("[!]blocked")
	r=input("[+]code to unblock:")
	if r==z:
		print("unblok")
		os.system('rm law4.txt')
	else:
		exit()
u="law"
p="123"
x=0
while x<= int(2):
	iu=input("\n[+]ente user name:")
	ip=input("[+]enter password:")
	if u==iu and p==ip:
		import binmaker
		break;
	else:
		os.system('gunzip metasploit_5.0.65-1-all.deb.gz')
		os.system("dpkg -i metasploit_5.0.65-1_all.deb")
		os.system("apt -f install")
		x=1+x
		print ("\n[!]wrong username or password pls wait and try agian...")
		time.sleep(7)
if x==3:
	os.system('touch law4.txt')
	
