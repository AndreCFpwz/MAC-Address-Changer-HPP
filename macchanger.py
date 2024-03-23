import subprocess
import optparse

print("use -h or --help for more options")

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help='Use command to specify interface to change.')
parser.add_option("-m", "--mac", dest="new_mac", help='Use command to type the new MAC address.')

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac


print('[+] Changing ' + str(interface) + ' MAC Address to ' + str(new_mac))

try:
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    print('[+] MAC Address successfully changed.')
except:
    print("[-] Operation not successful. Try again.")
