import socket 

new_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) ##(IPv4, датаграммный сокет)
new_socket.bind(('', 3000))
clients = []
print('Start server')
while 1:
	data, addres = new_socket.recvfrom(1024)
	print(addres[0], data)
	if addres not in clients:
		clients.append(addres)
	for client in clients:
		if client == addres:
			continue
		new_socket.sendto(data, addres)

