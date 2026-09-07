import socket
import threading

HOST = "127.0.0.1"      # Replace with server IP
PORT = 5000


def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)

            if not data:
                print("Server disconnected.")
                break

            print(f"\n{data.decode()}")

        except:
            break

    sock.close()


def send_messages(sock):
    while True:
        try:
            message = " " + input()
            sock.send(message.encode())
        except:
            break

    sock.close()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to server.")

threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
threading.Thread(target=send_messages, args=(client,), daemon=True).start()

while True:
    pass