import socket
import numpy as np
import pickle

#creating the matrices
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrices = list()
matrices.append(A)
matrices.append(B)
data = pickle.dumps(matrices)

#creating the client socket
s = socket.socket()
s.connect(('127.0.0.1', 8000))

#sending data
#while True:
s.sendall(data)
new_data = s.recv(1024)
matrices = pickle.loads(new_data)
print(matrices)