# Network Gathering Tool
> This Repository are made to share my Network Optimization, especially Automation using Python script.

### Notes :
Before using any coding in this repo, 
you should already have understanding about Python coding (mostly using Python 3 for the coding) and Paramiko (Module for SSH).


## Requirement :
1. Python 3.6.x / 2.7.x.
2. Paramiko module.
3. Basic Understading about Paramiko & Python coding, *you just need to understand how the coding work :).
4. [Optional] Microsoft Visual C++ 2015 for running the exe program once you compile it, if not then no need to use :).


## Table of Content :
//on progress writing the steps
1. [Install required module (Paramiko, pyinstaller, pathlib2).](#1-install-required-module)
2. Change the template file ('host_', 'credentials_', 'commands_').
3. Change `__init__.py` in each of folder ('host_', 'credentials_', 'commands)') with the related file you will be use in the core coding. 
4. (Windows Use Only) Compile the code into '**.exe**' file if you will use it for task scheduler on windows or 


## 1 Install Required module
This section will help you to install the required module, I hope that you already have python installed, so proceed with below commands to install the required modules :

1. Windows on Powershell / Command Prompt :
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
2. MacOS & Linux :
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
