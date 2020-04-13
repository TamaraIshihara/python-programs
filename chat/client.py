import socket
import threading

def read_socket():
	while 1:
		data = sock.recv(1024)
		print(data.decode('utf-8'))
	
server = '127.0.0.1', 3000 
print("Введите ник:")
alias = input() #ввод ника
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0)) #задаем сокет как клиент 
sock.sendto((alias + ': Connect to server\n').encode('utf-8'), server)
thread = threading.Thread(target = read_socket)
thread.start()
while 1:
	msg = input()
	sock.sendto((alias+ ':' +msg + '').encode('utf-8'), server)
