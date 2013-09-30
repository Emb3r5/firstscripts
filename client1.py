import socket

af,type,proto,name,conn = socket.getaddrinfo("www.google.com", 80,0,0,
socket.SOL_TCP)[0]

s = socket.socket(af,type,proto)
s.connect(conn)


snddata = "GET / HTTP/1.0\nHost: www.google.com\n\n"
s.send(snddata.encode())

page = ""

#while 1:
data = ''
while len(data) < 1024:
    chunk = s.recv(1024-len(data))
    if chunk == '':
      raise RuntimeError("socket connection broken")
    data = data+chunk.decode('ascii')
    #data = s.recv(1024)
	#if data == '':
#		break
	#page = page + data

s.close()

print(data)