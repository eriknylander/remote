# Chromecast Remote
Use an old HP remote with an XPC-RC01 USB IR receiver to control your Chromecast.

## Dependencies
`pyusb` is used to communicate with the IR receiver.

`pychromecast` is used to communicate with the Chromecast.

## How to run
Quite simple, `sudo python3 main.py`. To avoid having to use `sudo`, a rule can be added to let your user access the IR receiver. 

1. Add a file named `50-usbcontrol.rules` in `/etc/udev/rules.d` with the following content:
```
ACTION=="add", SUBSYSTEMS=="usb", ATTRS{idVendor}=="3353", ATTRS{idProduct}=="3713", MODE="660", GROUP="plugdev"
``` 
2. Make sure your user is a member of `plugdev`.
```
adduser username plugdev
```
3. Reload rules
```
sudo udevadm control --reload
sudo udevadm trigger
```

4. Reboot your machine.

Thanks to [this comment](https://stackoverflow.com/a/31994168) for the instructions.

## Running as a background service
1. Add a file called `chromecastremote.service` in `/etc/systemd/system` with the content:
```
[Unit]
Description=Chromecast Remove service
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /path/to/main.py

[Install]
WantedBy=multi-user.target
```
2. `sudo systemctl daemon-reload`
3. Enable the service so that it starts if your server restarts using `sudo systemctl enable chromecastremote.service`
4. Start the service using `sudo systemctl start chromecastremote.service`

Instructions taken from [this blog](https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267)
