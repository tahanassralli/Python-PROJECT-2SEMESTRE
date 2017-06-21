import socket
host = ''
port = 8000
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((host, port))
    serversocket.listen(5)
    print "Server Started.."
except socket.error as e:
    print(str(e))
def threaded_client(conn):
    
    while True:
        data = conn.recv(1024)
        reply="Wrong command! Please try again.."
        if data.upper()=="DONE" or data =="":
            break
        elif data.upper()=="HTTPSTATUS":
            import agent.Services.httpd as httpd
            http = httpd.webserver()
            reply=http()
        elif data.upper()=="IPTABLESTATUS":
            import agent.Services.iptables as iptables
            ipt = iptables.iptables()
            reply=ipt()
        print data
        conn.sendall(reply)
        
    conn.close()
while True:
    #serversocket.accept()
    conn,addr = serversocket.accept()
    print "Connected to "+str(addr[0])+":"+str(addr[1])
    conn.send("Welcome, enter your command:")
    threaded_client(conn);
