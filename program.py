from twilio.rest import Client
import random 
from tkinker import *
from tkinker import messagebox

class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600*550")
        self.resizable(False, False)

