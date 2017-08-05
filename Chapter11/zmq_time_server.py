import zmq
from datetime import datetime

host = '127.0.0.1'
port = 6789

context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://%s:%s" % (host,port))
print('Server started at', datetime.utcnow())
while True:
	# wait client'S request
	message = server.recv()
	if message == b'time':
		now = datetime.utcnow()
		reply = str(now).encode('utf-8')
		server.send(reply)
		print('Server sent', reply)

