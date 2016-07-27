import os


def init_iptables():
    os.system("iptables -D INPUT -p tcp -m tcp --dport 5000 -j ACCEPT")
    os.system("iptables -I INPUT -p tcp -m tcp --dport 5000 -j ACCEPT")
    os.system("iptables -D INPUT -p tcp -m tcp --dport 5001 -j ACCEPT")
    os.system("iptables -I INPUT -p tcp -m tcp --dport 5001 -j ACCEPT")
    os.system("iptables -t nat -D PREROUTING -p tcp --dport 80 -j DNAT --to 192.168.1.1:5000")
    os.system("iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to 192.168.1.1:5000")
    os.system("iptables -t nat -D PREROUTING -p tcp --dport 443 -j DNAT --to 192.168.1.1:5001")
    os.system("iptables -t nat -A PREROUTING -p tcp --dport 443 -j DNAT --to 192.168.1.1:5001")
    os.system("iptables -t filter -D PREROUTING -p tcp --dport 80 -j REJECT")
    os.system("iptables -t filter -A PREROUTING -p tcp --dport 80 -j REJECT")


def add_mac(mac):
    remove_mac(mac)
    os.system("iptables -t nat -I PREROUTING 2 -m mac --mac-source %s -j ACCEPT" % mac)


def remove_mac(mac):
    os.system("iptables -t nat -D PREROUTING -m mac --mac-source %s -j ACCEPT" % mac)
