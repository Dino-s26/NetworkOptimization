##Task Capture Performance##
import os
import paramiko
import time
import datetime

##Import List IP to be SSH
##Using __init__.py in hosts_ folder, update related file in __init__.py
import hosts_

##Import Command to be Gather
##Using __init__.py in command_ folder, update related file in __init__.py
import commands_

##Import Credential for SSH
##Using __init__.py in credentials_ folder, update related file in __init__.py
import credentials_


#Define date & time
#For the output file will be save to the folder
dt = str(datetime.datetime.now().strftime("%d-%m-%y--%H-%M-%M"))

#This line will iterate through host that we define in host_data file
#With list of list_ip
for ip in hosts_.host_data_dummy.list_ip:
	#From here we define that host will be equal to ip, as ip are list_ip in host_data file
	host = ip
	
	#This will ping the target host and check if the host is available or not, 
	#If firewall not permit ping the script will skip the host
	if os.system("ping -n 1 " + ip) is 0:
	
		#Define Connection Session
		#This will be using for the Paramiko method, as the credentials for the username and password
		#Will be changeable in creadential file with list of usern and passwd, be sure to change to your related username & passowrd
		pre_conn = paramiko.SSHClient()
		pre_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		pre_conn.connect(ip, port=22, username=credentials_.credential.usern, password=credentials_.credential.passwd, allow_agent=False)
		#Change this line with your custom word
		print ("Establishing SSH Connection... "+host)
		conn = pre_conn.invoke_shell()

		#Define file name
	
		#uncomment this line to define custom hostname 
		#hostname = 'your-device-hostname'

		#comment this 4 line, if you intent to custom the hostname above
		#start here
		conn.send('show run | i hostname \n')
		time.sleep(3)
		hostname = conn.recv(65000)
		hostname = hostname.decode('utf-8').split('\r\n')[-2].split('#')[0]
		#end here

		log_name = hostname + '--' + dt + '.txt'
		
		#Iterate command that will be gather
		for command in 	commands_.command_gather_data_dummy.command_order:
			conn.send(command)
			time.sleep(5)
			buff = conn.recv(65000)
			print (command + " done.")
    
    		#Change the path to your specified path folder to save the output log
			output_file = open(os.path.join('path/to/your/save/log/output',log_name), 'ab+')
			output_file.write(buff)
			output_file.close
	
		#Close the connection of SSH Session and the program
		conn.close()
	
	#This will give error message for possible cause why the host not reachable, you could change the error message in error_message 
	else:
		print("Error : host "+ ip +" is unreachacble Connection to host Abort !\n")
		error_log = "error-"+ ip + "-" + ddt + ".txt"
		output_file = open(os.path.join('C:/capture',error_log), 'a+')
		error_message = "Host " + ip + " may not reachable, please check the following : \n1. Firewall Rule already allow to the target host\n 2. Host IP is correct\n 3. Host device still active\n 4. Your Computer / Server have valid IP"
		output_file.write(error_message)
		output_file.close
	
	#Nothing to do after this line, the program already end !#
