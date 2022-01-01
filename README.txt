The GPIO daemon is started in /etc/rc.local via the second last line "pigpiod".

The app itself is started as a service. The service is configured in /lib/systemd/system/tank.service.

If the above is edited, you must: 'sudo systemctl daemon-reload'

You can disable startup by: 'sudo systemctl disable tank.service'

See https://www.digikey.ca/en/maker/projects/how-to-run-a-raspberry-pi-program-on-startup/ for further info.

Try journalctl -u tank



