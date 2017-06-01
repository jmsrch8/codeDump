import socket

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host,port))

    message = input('->')

    while message != 'q':
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print('receved from server: '+host+' Data is: '+ data )
        message = input('->')
    s.close
    input('press enter to exit')

if __name__ == '__main__':
    main()
