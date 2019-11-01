#!/usr/bin/env python3
import sys
import threading
import nia as NIA
import argparse
from pythonosc import udp_client

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1", help="OSC server IP")
parser.add_argument("--port", type=int, default=5005, help="OSC server port")
args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)
milliseconds = 10

# open the NIA, or exit with a failure code
nia = NIA.NIA()
if not nia.open():
    sys.exit(1)

nia_data = NIA.NiaData(nia, milliseconds)

while True:
    nia_data.get_data()
    
    # get the fourier data from the NIA
    data, steps = nia_data.fourier(nia_data)
    for num, step in enumerate(steps):
        print(step)
        client.send_message('/finger{0}'.format(num), step)

    # exit if we cannot read data from the device
    if nia_data.AccessDeniedError:
        sys.exit(1)

nia.close()
sys.exit(0)
