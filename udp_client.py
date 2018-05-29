# UDP client
import socket
import logging
import sys
import time

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 10000
adresa = '0.0.0.0'
server_address = (adresa, port)
mesaj = sys.argv[0]

try:

    for element in range (0,10000):
        mesaj = str(element)
      
        ACK= " "
        logging.info('Trimit mesajul "%s" catre %s', mesaj, adresa)
        sent = sock.sendto(mesaj, server_address)
        logging.info('Astept raspuns...')
        ACK, server = sock.recvfrom(4096)
        logging.info('Continut: "%s"', ACK)
        future=time.time()+0.5  
        while True:
            if time.time() > future:
                    logging.info('Trimit mesajul "%s" catre %s', mesaj, adresa)
                    sent = sock.sendto(mesaj, server_address)
                    future=time.time()+0.5
            if (ACK!=" "):
                    break

finally:
    logging.info('closing socket')
    sock.close()
