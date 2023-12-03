# modules/vrchat_osc.py

import time
from pythonosc import udp_client

# Configuration VRChat
IP_VRCHAT = "127.0.0.1"  # Adresse IP de votre instance VRChat
PORT_VRCHAT_SEND = 9000  # Port d'envoi OSC de VRChat

def send_osc_message(address, *args):
    client = udp_client.SimpleUDPClient(IP_VRCHAT, PORT_VRCHAT_SEND)
    client.send_message(address, args)

def advertise_kawaii_gang():
    kawaii_frames = [
        "🌈 Thanks for using Kawaii Squad Script! 🌸",
        "🌟 Discover amazing avatars with us! ✨",
        "🎉 Visit our community for free avatars! 🎊",
        "🌈 Join Kawaii Squad Avatar Reaper Free! 🌸"
    ]

    # Adresse OSC pour envoyer un message au chatbox de VRChat
    chatbox_address = "/chatbox/input"

    for frame in kawaii_frames:
        send_osc_message(chatbox_address, frame)
        time.sleep(2)
