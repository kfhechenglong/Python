import socket
# 服务端
sock = socket.socket()
sock.bind(("127.0.0.1", 8899))
sock.listen(5)

while 1:
  client_sock, addr = sock.accept()
  print("client %s connect"%str(addr))
  while 1:
    try:
      data = client_sock.recv(1024)
    except Exception:
      client_sock.close()
      print("client %s closed"%str(addr))
      break
    print(data.decode())
    res = input(">>>")
    client_sock.send(res.encode())