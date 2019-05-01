# :computer: Network Gathering Tool
> This Repository are made to share my Network Gathering Tool code, especially Automation using Python script. As this project still in improvement, there will be major update in master branch, if you are going to make your own version / help the coding to be more efficient, kindly make new branch and I will review the code.

### :blue_book: Notes :
Before using any coding in this repo, 
you should already have understanding about Python coding (mostly using Python 3 for the coding) and Paramiko (Module for SSH).


## :white_check_mark: Requirement :
1. Python 3.6.x / 2.7.x.
2. Paramiko module.
3. Basic Understading about Paramiko & Python coding. *you just need to understand how the coding work.*
4. **__[Optional]__** Microsoft Visual C++ 2015 for running the `.exe` program once you compile it. *if not then no need to use.*


## :clipboard: Table of Content :

1. [Install required module (Paramiko, pyinstaller, pathlib2).](#install-required-module)
2. [Change the template file ('host_', 'credentials_', 'commands_').](#change-template-file)
3. [Change `__init__.py` in each of folder ('host_', 'credentials_', 'commands)') with the related file you will be use in the core coding.](#change-init-file)
4. [(Windows Use Only) Compile the code into '**.exe**' file if you will use it for task scheduler on windows or schedule job on windows](#compile-to-executable)

## Structure of project

Below are the Structure of the Project Folder that I use for this project, as I intent to make this project as clean as possible for public use, and for the coding purpose on the related files in this project.

- Project Folder
  - `data_collection_template.py`
    - `hosts_` folder
      - `__init__.py` file
      - `host_data_dummy.py` file
     - `credentials_` folder
       - `__init__.py` file
       - `credential.py` file
     - `commands_` folder
       - `__init__.py` file
       - `command_gather_data_dummy.py` file

1. #### Install Required module
This section will help you to install the required module, I hope that you already have python installed, so proceed with below commands to install the required modules :

1.1. Windows on Powershell / Command Prompt :
```
# Powershell #
pip install paramiko
pip install pyinstaller
pip install pathlib2

# Command Prompt #
python -m pip install paramiko
python -m pip install pyinstaller 
python -m pip install pathlib2
```
1.2. MacOS & Linux :
```
sudo pip install paramiko
sudo pip install pyinstaller //only use this if you intended to compile the code into .exe program
sudo pip install pathlib2

if above command not working you can use below command :

sudo python -m pip install paramiko
sudo python -m pip install pyinstaller //only use this if you intended to compile the code into .exe program
sudo python -m pip install pathlib2
```
If you find problem when installing required module, google and forums (stackoverflow, reddit, etc) are your best friend to find the answers to the related error code when installing required module.

2. #### Change Template File
As the file only template, kindly change the template file to your need.
There are 4 file (`data_collection_template`, `host_data_dummy`, `command_gather_data_dummy` and `credential`), below are the coding that you need to change :

2.1. **data_collection_template.**

Open the `data_collection_template` file, and you will find the following lines :
```
for ip in hosts_.host_data_dummy.list_ip:
```
Change the `host_data_dummy` to your host file that you copy from template in `hosts_` folder. The `host_data_dummy` is the template file, you can copy the file and name it with following format `<your>_<filename>.py` and also dont forget to add the file name to the `__init__.py` in the `hosts_` folder, below are the example of the `__init__.py` in `hosts_` folder :
```
from .host_data_dummy import *
```
Change the `.host_data_dummy` with your host file that you already copy and rename it. You should update this file whenever you create new `host` file for your other template you creating for gathering data.

*Next line is :*

```
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
```
Above line are the file name for the output, as the hostname could be get by run the `'show run | i hotname'`, this only available for Cisco devices. For other devices you should define the custome hostname, or using list method just like the ip we use to ssh but nested in the ssh method. Since I'm using Cisco devices for the test, You could change this with your prefer command that your device could handle.

*Next Line is :*

```
output_file = open(os.path.join('path/to/your/save/log/output',log_name), 'ab+')
```
Change the `'path/to/your/save/log/output'` to your folder to save the output file after running the command.


2.2. **host_data_dummy.**

Open the `host_data_dummy` file, and you will find the following lines :
```
list_ip = [
           '127.0.0.1' #Change this ip to your server / network device ip, add ',' / comma for multiple ip 
          ]
```
Change the IP (in this list are `'127.0.0.1'`) to your host that will be SSH. As you could also insert multiple IP because this method here are list, so you could do that. Just remember that if the IP are unreachable it won't skip to the next IP in this list, but will stop the program. I still looking the solution to this problem, temporarily you could remove the unreachable IP and re-run / re-compile the core coding.

Also don't forget to update `__init__.py` file in the folder of `hosts_` if you are copy the `host_data_dummy` and make your own template host file, just like I explain in **data_collection_template** section.

2.3. **command_gather_data_dummy.**

Open the `command_gather_data_dummy` file, and you will find the following lines :
```
command_order = ['term le 0\n',
		 'show version\n',
		 'show inventory\n',
		 'show chassis\n',
		 'term le 30\n',
		 'exit\n'
		]
```
This file are same as `host_data_dummy` the different is that this execute the command that you will be gathering. Above command are `'show version'`, `'show inventory'`, and `'show chassis'`. You could change to the appropriate command you wanted to execute or you could just copy the file and customize it. 

Also don't forget to update `__init__.py` file in the folder of `commands_` if you are copy the `command_gather_data_dummy` and make your own template command file, just like I explain in **data_collection_template** section.


3. #### Change init File

Congratulation now you could create the custom capture tools, but before you run the code you sould edit the `__init__.py` file within the each of folder of this code. I've already explain it in **data_collection_template** section, but let's break it down in this section so you could understand my code. 

As you could see in **_Structure of project_** section **[here](#structure-of-project)**, you could see there are `__init__.py` in each of folder of `hosts_`, `credentials_`, and `commands_`. This `__init__.py` are the file I use to link the each file consisted in the each of those 3 folder I mention. So what is in those `__init__.py` ?, let's break it down :

Now open the `data_collection_template.py` file. There are 3 line defined after import required library for the coding which is :
```
import hosts_
import credentials_
import commands_
```

Those 3 line are call the `__init__.py` file in each of the folder, now I will explain what is in each of this file on each of the folder.

3.1. `__init__.py` in `hosts_` :

This file consist of following line :

```
from .host_data_dummy import *
```

Which will call the `host_data_dummy.py` file and call any method I've defined there, in this case is `list_ip` that consisting list of the host IP that will be SSH for the code as exlained in the section **[here](#change-template-file)**.

3.2. `__init__.py` in `credentials_` :

This file consist of following line :

```
from .credential import *
```

Which will call the `credential.py` file that have the following line of code :

```
usern = 'your username'
passwd = 'your ssh password'
```

Remember to edit the **_Username_** & **_Password_** before compile / run the code.

3.3. `__init__.py` in `commands_` :

This file consist of following line :

```
from .command_gather_data_dummy import *
```

Which will call the `command_gather_data_dummy.py` file that will execute the command will be run for the code as exlained in the section **[here](#change-template-file)**.

Okay now you're done, if you do not intent to compile the file into `.exe` file you are ready to go, but if you intent to compile it into `.exe` you should continue to the next step.

4. #### Compile to Executable

Before proceeding with this step, make sure you have the **_Microsoft Visual C++ 2015_**. This step could be done in 2 way, compile it into `.exe` with the whole file (which will need the related file to run the code, I'm not recommend this default method) or compile it into 1 file only which is cleaner in my opinion. Below are the steps for 1 file only method :

4.1. Open Powershell to the project folder.

4.2. Make sure pyinstaller already install by run this command `pyinstaller --version` to check the installed version.

4.3. Run this code to compile into 1 file only `pyinstaller --onefile <name>_<of_the_code>.py` for example `pyinstaller --onefile data_collection_template.py` wait until the process is done.

4.4. There you go, you will have the `.exe` file of your coding in newly created folder name `dist`, you could check it there and test the program.

Notes: _To do debuging of the `.exe` file, you could run the program in CMD from the project folder, as this will tell you the error if the executable file forced close without giving the output file._

And That's it, You are now could customize and compile it to `.exe` executable file for Task Scheduler in Windows.

**-- End Of Readme --**
