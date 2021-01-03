import socket
import os.path

class Server:
	def __init__(self, host, port):
		self.host = host
		self.port = port

	def __enter__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind((self.host, self.port))
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.socket.close()
		return True

	def start(self):
		self.socket.listen(1)
		self.conn, self.addr = self.socket.accept()
		command = self.conn.recv(1024)
		str = command.decode()
		operation = str.split(' ')[0]
		fileName = str.split(' ')[1]
		if operation == 'upload':
			self.upload(fileName)
		elif operation == 'download':
			self.download(fileName)

	def upload(self, fileName):
		self.conn.send(b'confirmed')
		with open(fileName, 'wb') as f:
			while True:
				data = self.conn.recv(1024)
				if not data:
					break
				f.write(data)

	def download(self, fileName):
		# TODO implement later
		pass

def serverMain():
	server = Server('', 5008)
	with server as s:
		s.start()


if __name__ == '__main__':
	serverMain()