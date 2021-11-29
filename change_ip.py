 #!/usr/bin/env python3

import os
import shutil
import subprocess

ipaddres = "192.168.3.127"
netmask = '255.255.255.0'
gateway = '192.168.3.1'
dns_prymary = '8.8.8.8'
dns_secundary = '8.8.4.4'
dhcp = True
restart_network = 'sudo /etc/init.d/networking restart'
file_interfaces = '/etc/network/interfaces'
file_name = 'interfaces'
route_first_file = './interfaces'
networking = 'enp0s3'


if dhcp == False:
    data = '\
auto {networking}\n\
iface {networking} inet static\n\
  address {ipaddres}\n\
  netmask {netmask}\n\
  gateway {gateway}\n\
  dns-nameserver {dns_prymary} {dns_secundary}\n\
'.format(
    networking=networking,
    ipaddres=ipaddres,
    netmask=netmask,
    gateway=gateway,
    dns_prymary=dns_prymary,
    dns_secundary=dns_secundary
)
else:
    data = '\
auto {networking}\n\
iface {networking} inet dhcp\n\
'.format(networking=networking)

print(data)

with open(file_name, 'x') as f:
    f.write(data)

if os.path.isfile(file_interfaces):
    os.remove(file_interfaces)

shutil.move(route_first_file, file_interfaces)

subprocess.run(restart_network ,shell=True)
