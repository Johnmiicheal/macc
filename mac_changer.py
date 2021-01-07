import subprocess
import optparse
import re

def get_arguments():
    pass

def change_mac(interface, new_mac):
    pass

def get_current_mac(interface):
    ifconfig_result = subprocess.check_out(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address...")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was succesfully changed to " + current_mac)
else:
    print("[-] MAC address could not change!!!.")


