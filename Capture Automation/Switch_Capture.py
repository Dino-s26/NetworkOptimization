##Task Capture Performance##
import os
import paramiko
import time
import getpass
import datetime

##Import List IP to be SSH
from host import list_ip

##Import Command to be Gather
from command_gather import command_order

##Import Credential for SSH
from credential import usern,passwd


#Define date & time
ddt = str(datetime.datetime.now().strftime("%d-%m-%y--%H-%M-%M"))

#Do loop for hostname / ip we need to do captures
for ip in list_ip:
	host = ip

	#Define Connection Session
	pre_conn = paramiko.SSHClient()
	pre_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	pre_conn.connect(ip, port=22, username=usern, password=passwd, allow_agent=False)
	print ("Establishing SSH Connection... "+host)
	conn = pre_conn.invoke_shell()

	#Define file name
	conn.send('show run | i hostname \n')
	time.sleep(1)
	hostname = conn.recv(65000)
	hostname = hostname.decode('utf-8').split('\r\n')[-2].split('#')[0]
	log_name = hostname + '--' + ddt + '.txt'
		
	#Do loop for command will be gather
	for command in command_order:
		conn.send(command)
		time.sleep(1)
		buff = conn.recv(65000)
		print (command + " done.")
    
		output_file = open(os.path.join('C:/Capture CatTools/Router/',log_name), 'ab+')		
		output_file.write(buff)
		output_file.close
	
	#Close connection to  SSH Session
	conn.close()