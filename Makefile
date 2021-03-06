
depend:
	pip2 install -r requirements.txt	

install: depend
	cp -TRf src /usr/local/bin/captivePortal
	chmod 755 /usr/local/bin/captivePortal/main.py
	install -o root -g root -m 755 captivePortal /etc/init.d/ 		
	update-rc.d captivePortal defaults
	service univention-firewall restart
	service captivePortal restart
