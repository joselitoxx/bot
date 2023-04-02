import socket
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re
from unicodedata import normalize
###
def head():
    def normalizar(message: str):
        # -> NFD y eliminar diacríticos
        message = re.sub(
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
            normalize("NFD", message), 0, re.I
        )

        # -> NFC
        return normalize('NFC', message)

    def identificar_mensaje1():
        time.sleep(3)
        element_box_message = driver.find_elements(By.ID,"line1")
        posicion = len(element_box_message) - 1

        element_message = element_box_message[posicion].find_elements(By.CLASS_NAME, "bot")
        message = element_message[0].text.upper().strip()
        #print("RESPUESTA BOT:", message)
        return normalizar(message)

    def preparar_respuesta1(message: str):
        print("PREPARANDO RESPUESTA")
        response = input("respuesta ")
        return response

    def procesar_mensaje1(message: str):
        time.sleep(3)
        chatbox = driver.find_element(By.XPATH, "//*[@id='avatarform']/input[1]")
        response = message

        chatbox.send_keys(response)
        driver.find_element(By.XPATH, '// *[ @ id = "avatarform"] / input[2]').click()
    #############

    HEADER = 64
    PORT = 5050
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    SERVER = local_ip
    ADDR = (SERVER, PORT)
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

    def enviar():
        conn, addr = server.accept()
        while True:

            mens = identificar_mensaje1() # RESIV EL MENSAGE DEL MONO
            print("bot menssage = ",mens)
            conn.send(mens.encode(FORMAT)) # mandA EL MENSAJE A WHATSAPP
            time.sleep(1)
            msg_length = conn.recv(HEADER).decode(FORMAT) #RECIVE MENSAGE DE WHASAPP
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT) # DECODIFICA EL MENSAJE
                if msg == DISCONNECT_MESSAGE:
                    break
                else:
                    print("MENSAJE DE WHASTSAPP = ", msg)
                    procesar_mensaje1(msg)   #MANDA EL MESAGE DE MONO

    print("[STARTING] server is starting...")
    ###
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.chimbot.com/es/')
    driver.find_element(By.XPATH, "//*[@id='suitablenote']/p[6]/span").click()
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    enviar()


head()






