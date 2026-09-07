import tkinter as tk

class OMessenger:

    def __init__(self, root):
        self.root = root
        self.root.title("OMessenger")
        self.root.geometry("500x500")
        tk.Button(
            root,
            text="Client",
            command=self.start_client
        ).pack()
        tk.Button(
            root,
            text="Server",
            command=self.start_server
        ).pack()


    def start_server(self):

        tk.Label(root, text="Port").pack()

        port_entry = tk.Entry(root)
        port_entry.pack()

        port = port_entry.get().strip()
        print(port)
        tk.Button(
            root,
            text="connect",
            command=lambda: self.connect(int(port)),
        ).pack()

    def start_client(self):
        tk.Label(root, text="IP").pack()

        ip_entry = tk.Entry(root)
        ip_entry.pack()

        tk.Label(root, text="Port").pack()

        port_entry = tk.Entry(root)
        port_entry.pack()

        ip = ip_entry.get().strip()
        port = port_entry.get().strip()

        if not ip:
            print("IP is required")
            return

        if not port.isdigit():
            print("Port must be a number")
            return

        port = int(port)

        print(ip, port)
        self.connect(port,ip)

    def connect(self, port:int,ip="0.0.0.0"):
        if not ip:
            print("IP is required")
            return

        if not port:
            print("Port must be a number")
            return




root = tk.Tk()

OMessenger(root)

root.mainloop()