import socket
import numpy as np
import queue as queue
import threading
import pickle


#thread operations
def worker(rowA, matrixB, resQueue):
        res1 = rowA.dot(matrixB[:,0])
        res2 = rowA.dot(matrixB[:,1])
        res3 = rowA.dot(matrixB[:,2])
        rowRes = np.array([[res1,res2,res3]])
        resQueue.put(rowRes)

#
def threads(matrixA, matrixB):
        size = 3
        resQueue = queue.Queue()
        threads = list()
        #run threads
        for i in range(size):
            t = threading.Thread(target=worker, args=(matrixA[i],matrixB,resQueue))
            threads.append(t)
            t.start()
        #join threads
        for i in range(size):
                threads[i].join()
        #get values
        for i in range(size):
                if(i == 0):
                        matrixRes = np.array(resQueue.get(0))
                else:
                        matrixRes = np.append(matrixRes, resQueue.get(i), axis = 0)
        return matrixRes


def server_socket():
        HOST = '127.0.0.1'
        PORT = 8000
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((HOST, PORT))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        recvd_data = pickle.loads(data)
                        matrices = threads(recvd_data[0],recvd_data[1])
                        new_data = pickle.dumps(matrices)
                        conn.sendall(new_data)

server_socket()