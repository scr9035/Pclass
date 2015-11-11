from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(("",9000))
s.listen(5)

while True:
	c,a = s.accept()
	data = c.recv(1024).strip()
	print "{} wrote: ".format(a[0]),
	print data
	c.send(data.upper())
	c.close()