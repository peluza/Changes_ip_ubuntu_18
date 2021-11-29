 #!/usr/bin/env python3

import os
import shutil
import subprocess

ipaddres = "192.168.3.65"
netmask = '255.255.255.0'
gateway = '192.168.3.1'
dns_prymary = '8.8.8.8'
dns_secundary = '8.8.4.4'
dhcp = False
restart_network = '/etc/init.d/networking restart'
file_interfaces = '/etc/network/interfaces'
file_name = 'interfaces'
route_first_file = './interfaces'


if dhcp == False:
    data = ' \
auto eth1\
iface eth1 inet static\n \
        address {}\n \
        netmask {}\n \
        gateway {}\n \
        dns-nameserver {} \n \
        dns-nameserver {}\n \
'.format(
    ipaddres,
    netmask,
    gateway,
    dns_prymary,
    dns_secundary
)
else:
    data = ' \
auto eth1\
iface eth0 inet dhcp\n \
'

print(data)

with open(file_name, 'x') as f:
    f.write(data)

if os.path.isfile(file_interfaces):
    os.remove(file_interfaces)

shutil.move(route_first_file, file_interfaces)

subprocess.run(restart_network ,shell=True)
