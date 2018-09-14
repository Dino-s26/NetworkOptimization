## 										Command Gather 												  ##
## -------------------------------------------------------------------------------------------------- ##
## This file are for the list of command that need to run / capture for Cisco Devices 				  ##
## command_order are the array list of command from cisco devices used to capture the output,		  ##
## below are the example of the command are used to generate the output of the data I need to collect.##
## Please change the command that suit what you need												  ##

command_order = ['term le 0\n',
				'show version\n',
				'show process cpu history\n',
				'show process cpu sorted\n',
				'show process memory sorted\n',
				'show processes memory detailed process iosd sort\n',
				'show environment\n',
				'show inv\n',
				'show int desc\n',
				'show authen ses\n',
				'show cdp n\n',
				'show ip int br\n',
				'show run\n',
				'show run all\n',
				'show mod\n',
				'show ip arp\n',
				'show aaa server\n',
				'show vlan br\n',
				'show mac add\n',
				'show logg\n',
				'term le 30\n',
				'exit\n'
				]