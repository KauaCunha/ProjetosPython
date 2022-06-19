from httplib2 import AllHosts
import nmap

destino = '192.168.118/24'
port = '80'

nm = nmap.PortScanner()
nm.scan(hosts=destino, ports=port)


if nm.all_hosts():
    print('Host encontrado')
    for host in nm.all_hosts():
        host_ip = host
        host_state = nm[host_ip].state()
        port_state = nm[host_ip]['tcp'][int(port)]['state']
        print(f'{host_ip}  - {host_state} - {port_state}')
else:
    print('Host não encontrado')