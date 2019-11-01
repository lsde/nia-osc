# nia-midi
This application translates data from OCZ NIA to OSC.

It sends-out the "brain-fingers" as OSC message to the specified IP address and port.

Based on https://github.com/kevinmershon/pynia

## Prerequities
```
# apt install python-virtualenv python3-virtualenv
# cp 47-ocz-nia.rules /etc/udev/rules.d/`
# udevadm control --reload-rules
# virtualenv -p python3 venv
# venv/bin/pip install -r requirements.txt
```

## Running
````
# python nia-osc.py -h
usage: nia-osc.py [-h] [--ip IP] [--port PORT]

optional arguments:
  -h, --help   show this help message and exit
  --ip IP      OSC server IP
  --port PORT  OSC server port

# ./start.sh
````

## Autostart example using screen
````
# crontab -l
@reboot screen -dmS nia-osc /home/pi/nia-osc/start.sh --ip 239.1.1.1 --port 5005
````
