import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = '127.0.0.1'

target_ip = socket.gethostbyname(target)
print('Starting scan on host:', target_ip)

def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False

start = time.time()

for port in range(5):
    if port_scan(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is closed')

end = time.time()
print(f'Time taken {end-start:.2f} seconds')