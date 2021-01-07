# MACCHANGER SCRIPT

## How it works 
* Execute and read ```ifconfig```
* Read the mac address from output
* check if MAC in ```ifconfig``` is what the user requested
* Print appropriate message


### How to use
FOR USE ON LINUX MACHINES ONLY

* ```python macc.py -i [interface] -m [new mac address]```


### Possible troubleshoot 

* ifconfig not working: ```sudo apt-get install net-tools```
* module not found: Install python



