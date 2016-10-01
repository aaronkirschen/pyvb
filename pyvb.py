#! python3

#pyvb.py - Start, stop, and restart virtualbox machines

paths = { \
	'VBoxManage'	: r'C:\Program Files\Oracle\VirtualBox\VBoxManage' \
		}

import subprocess

def start(name):
	''' Start virtualbox machine name '''
	
	cmd = [ paths['VBoxManage'], 'startvm', name ] 
	subprocess.call(cmd)
	
	
