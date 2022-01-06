The GPIO daemon is started in /etc/rc.local via the second last line "pigpiod".

The app itself is started as a service. The service is configured in /lib/systemd/system/tank.service.

If the above is edited, you must: 'sudo systemctl daemon-reload'

You can disable startup at boot by: 'sudo systemctl disable tank.service'
You can stop service re-starting by: 'sudo systemctl stop tank.service'
You can start service and app by: 'sudo systemctl start tank.service'

See
https://www.digikey.ca/en/maker/projects/how-to-run-a-raspberry-pi-program-on-startup/cc16cb41a3d447b8aaacf1da14368b13
for further info.

Try journalctl -u tank



