import os

def init_iptables():
# the captive portal
    os.system("iptables -D INPUT -p tcp -m tcp --dport 5000 -j ACCEPT")
    os.system("iptables -I INPUT -p tcp -m tcp --dport 5000 -j ACCEPT")
    os.system("iptables -D INPUT -p tcp -m tcp --dport 5001 -j ACCEPT")
    os.system("iptables -I INPUT -p tcp -m tcp --dport 5001 -j ACCEPT")

# redirect some shit portals for dns to work better
    os.system("iptables -t nat -D PREROUTING -p tcp -d 192.168.1.1 --dport 80 -j DNAT --to 192.168.1.1:5000")
    os.system("iptables -t nat -I PREROUTING 2 -p tcp -d 192.168.1.1 --dport 80 -j DNAT --to 192.168.1.1:5000")
    os.system("iptables -t nat -D PREROUTING -p tcp -d 192.168.1.1 --dport 1337 -j DNAT --to 192.168.1.1:80")
    os.system("iptables -t nat -I PREROUTING 2 -p tcp -d 192.168.1.1 --dport 1337 -j DNAT --to 192.168.1.1:80")

# redirect the shit
    os.system("iptables -t nat -D PREROUTING -p tcp --dport 80 -j DNAT --to 192.168.1.1:5000")
    os.system("iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to 192.168.1.1:5000")
    os.system("iptables -t nat -D PREROUTING -p tcp --dport 443 -j DNAT --to 192.168.1.1:5001")
    os.system("iptables -t nat -A PREROUTING -p tcp --dport 443 -j DNAT --to 192.168.1.1:5001")

# dns
    os.system("iptables -t nat -D PREROUTING -p tcp --dport 53 -j DNAT --to 192.168.1.1")
    os.system("iptables -t nat -I PREROUTING 2 -p tcp --dport 53 -j DNAT --to 192.168.1.1")
    os.system("iptables -t nat -D PREROUTING -p udp --dport 53 -j DNAT --to 192.168.1.1")
    os.system("iptables -t nat -I PREROUTING 2 -p udp --dport 53 -j DNAT --to 192.168.1.1")
#    os.system("iptables -t nat -D PREROUTING -p tcp --dport 53 -j ACCEPT")
#    os.system("iptables -t nat -A PREROUTING -p tcp --dport 53 -j ACCEPT")
#    os.system("iptables -t nat -D PREROUTING -p udp --dport 53 -j ACCEPT")
#    os.system("iptables -t nat -A PREROUTING -p udp --dport 53 -j ACCEPT")

# redirect all foreign dns server requests to our local dns server
#    os.system("iptables -D FORWARD -p tcp --dport 53 -j DNAT --to 192.168.1.1:53")
#    os.system("iptables -I FORWARD -p tcp --dport 53 -j DNAT --to 192.168.1.1:53")
#    os.system("iptables -D FORWARD -p udp --dport 53 -j DNAT --to 192.168.1.1:53")
#    os.system("iptables -I FORWARD -p udp --dport 53 -j DNAT --to 192.168.1.1:53")

# ssh
    os.system("iptables -t nat -D PREROUTING -p tcp --dport 22 -j ACCEPT")
    os.system("iptables -t nat -A PREROUTING -p tcp --dport 22 -j ACCEPT")

# redirect the leftovers 
    os.system("iptables -t nat -D PREROUTING -p tcp -j DNAT --to 192.168.1.1:5000")
    os.system("iptables -t nat -A PREROUTING -p tcp -j DNAT --to 192.168.1.1:5000")
    os.system("iptables -t nat -D PREROUTING -p udp -j DNAT --to 192.168.1.1:5000")
    os.system("iptables -t nat -A PREROUTING -p udp -j DNAT --to 192.168.1.1:5000")


def add_mac(mac):
    remove_mac(mac)
    os.system("iptables -t nat -I PREROUTING 4 -m mac --mac-source %s -j ACCEPT" % mac)


def remove_mac(mac):
    os.system("iptables -t nat -D PREROUTING -m mac --mac-source %s -j ACCEPT" % mac)
