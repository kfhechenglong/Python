import socket
ip_port = ("127.0.0.1", 8899)
sk = socket.socket()
sk.connect(ip_port)

while 1:
  data = input(">>>")
  sk.send(data.encode())
  print(1)
  res = sk.recv(1024)
  print(2)
  print("serve: %s"%res.decode())