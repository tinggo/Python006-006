import socket

HOST = '127.0.0.1'
PORT = 5008
FILENAME = 'data.txt'

def main(fileName):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.send(b'upload upload.txt')
	response = s.recv(1024)
	if response.decode() == 'confirmed':
		with open(fileName, 'rb') as f:
			while True:
				data = f.read(1024)
				if not data:
					break
				s.send(data)
			s.close()

if __name__ == '__main__':
	main(FILENAME)