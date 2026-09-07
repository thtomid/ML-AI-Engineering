import socket
import threading

HOST = "0.0.0.0"
PORT = 5000


def receive_messages(conn):
    while True:
        try:
            data = conn.recv(1024)

            if not data:
                print("Client disconnected.")
                break

            print(f"\nClient: {data.decode()}")

        except:
            break

    conn.close()


def send_messages(conn):
    while True:
        try:
            message = "from Omid: " + input()
            conn.send(message.encode())
        except:
            break

    conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server listening on {HOST}:{PORT}")

conn, addr = server.accept()

print(f"Connected by {addr}")

threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()
threading.Thread(target=send_messages, args=(conn,), daemon=True).start()

while True:
    pass