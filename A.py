import socket
import rsa
###test

###test

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


# send("Hello World!")
# input()
# send("Hello Everyone!")
# input()

#### Sample variables ####
(pubKeys,privKey)= rsa.newkeys(512)

def formatMsg(msg):
    msg = msg.replace("PublicKey", "")
    return msg

####with dict

certificate = {
  "Key": pubKeys,
  "Identity": "A"
}
####

msg = formatMsg(str(certificate))
send(msg)

input()

input()
send(DISCONNECT_MESSAGE)