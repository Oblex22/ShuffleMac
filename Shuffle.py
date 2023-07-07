import subprocess
import time
import sys
import random


# List of MAC addresses to cycle through
def generate_mac_addresses():
    mac = [random.randint(0x00, 0xff) for _ in range (6)]
    return ":".join("{:02x}".format(octet) for octet in mac)

mac_addresses = [generate_mac_addresses() for _ in range(9)]

# Function to change the MAC address using subprocess
def change_mac_address(interface, mac_address):
    # Check the platform (Linux/macOS or Windows)
    if 'linux' in sys.platform or 'darwin' in sys.platform:
        subprocess.call(['ifconfig', interface, 'down'])
        subprocess.call(['ifconfig', interface, 'hw', 'ether', mac_address])
        subprocess.call(['ifconfig', interface, 'up'])
    elif 'win' in sys.platform:
        subprocess.call(['ipconfig', '/release'])
        subprocess.call(['ipconfig', '/flushdns'])
        subprocess.call(['ipconfig', '/renew'])
        subprocess.call(['ipconfig', '/registerdns'])

# Get the network interface name
# Replace 'eth0' with your actual interface name (e.g., 'en0' for macOS, 'Wi-Fi' for Windows)
interface = 'eth0'

while True:
    for mac_address in mac_addresses:
        change_mac_address(interface, mac_address)
        print(f"Changed MAC address to: {mac_address}")
        time.sleep(180)  # Wait for 3 mins