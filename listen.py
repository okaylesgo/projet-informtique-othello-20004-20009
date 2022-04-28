import socket
import asyncio
import json
port=int(1234)
Addressplayer = ('0.0.0.0', port)
serveraddress=('localhost',3000)
def listen(): 
    with socket.socket() as s:
        s.settimeout(0.1)
        s.bind(Addressplayer)
        s.listen()
        while True:
            try: 
                client, address = s.accept()
                with client:
                    message = client.recv(2048).decode() 
                    requete=json.loads(message)                 
                    if requete["request"]== "ping": 
                        #fonction qui renvoie pong
                        print(requete)
                    elif requete["request"]=='play':
                        #future fonction pour jouer un coup 
                        print(requete)
            except socket.timeout:
                pass