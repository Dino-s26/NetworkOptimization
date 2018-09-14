### SCRIPT TASK CAPTURE ###

import os
import paramiko
import time
import getpass
import datetime

# IMPORT IP FOR SSH
## This is to access the host.py file that we define the list of IP address
## That are going to be accessed via SSH
from host import list_ip

# IMPORT COMMAND TO RUN
## This is to run Cisco CLI Command that we need to capture on command_gather.py file
from command_gather import command_order

# IMPORT CREDENTIAL FOR SSH
## This is to use credential for login via SSH, as we define on credential.py file
from credential import usern,passwd


# DEFINE DATE & TIME
## Get Current Date & Time, You may change this as it suit your needs :) 
ddt = str(datetime.datetime.now().strftime("%d-%m-%y--%H-%M-%M"))

#DO LOOP FOR IP ADDRESS OF DEVICES
## This is to loop to other IP Address until no IP address to be accessed via SSH
for ip in list_ip:
	## This is to call the IP address of the devices :)
	host = ip

	# DEFINE CONNECTION WITH PARAMIKO
	## This is standart parameter of paramiko API
	pre_conn = paramiko.SSHClient()
	pre_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	pre_conn.connect(ip, port=22, username=usern, password=passwd, allow_agent=False)
	
	## You can change the print text,
	## So you know the indication of what devices are being access
	## 'host' in here are the IP address of the device
	print ("Establishing SSH Connection... "+host)
	conn = pre_conn.invoke_shell()

	# DEFINE FILE NAME
	
	## Prompt command 'enable' for Cisco ASA
	## Line Begin Define File
	conn.send('en\n')
	time.sleep(1)
	
	## As Cisco ASA using enable to authenticate to level 15, change the 'xxxx'
	## Change it with your Cisco ASA Enable Password
	conn.send('xxxx\n') 
	time.sleep(1)
	
	## If your Cisco ASA used as Multicontext Firewall, I recommend you do this command 
	## If not using Multicontext Firewall you don't need this
	conn.send('changeto sys\n')
	time.sleep(1)
	
	## This command just to get your hostname of the Cisco ASA that you are using
	## If you don't want to use Device hostname as the filename 
	## You may need to give comment (#) from Line 'Begin Define File' to 'End of Define File'
	conn.send('show run | i your-device-hostname \n')
	time.sleep(1)
	
	## This Function use to do buffer on the SSH Session, so we can read the line
	hostname = conn.recv(65000)
	## This Function for decode the buffer we received from the devices and convert it to utf-8 character encoding
	hostname = hostname.decode('utf-8').split('\r\n\r')[-1].split('#')[0]
	## Line End of Define File
	
	## This Function for log file name that will be ganerated after the script finished running
	log_name = hostname + '--' + host + '--' + ddt + '.txt'
	
	# DO LOOP FOR COMMAND
	## This is to run command in loop for 1 IP Address, until it finished
	for command in command_order:
		conn.send(command)
		time.sleep(1)
		
		## This Function are the same as before, to do buffer in order to received the output :) 
		buff = conn.recv(65000)
		
		## This print to indicate what command has been done running,
		## You can change this, but remember, you also need to change the command_gather.py 
		## Because it related each other
		print (command + " done.")
    
		## This Funtion is to write the output into File that we define in 'DEFINE FILE NAME' section
		## Change the 'C:/Capture/' to folder where you want the output to be saved at
		output_file = open(os.path.join('C:/Capture/',log_name), 'ab+')		
		output_file.write(buff)
		output_file.close
	
	# CLOSE CONNECTION
	conn.close()