import netifaces as nif


def lookup(ip):
    'Returns a list of MACs for interfaces that have given IP, returns None if not found'
    for i in nif.interfaces():
        address = nif.ifaddresses(i)
        try:
            if_mac = address[nif.AF_LINK][0]['addr']
            if_ip = address[nif.AF_INET][0]['addr']
        except(IndexError, KeyError):  # ignore ifaces that dont have MAC or IP
            if_mac = if_ip = None
        if if_ip == ip:
            return if_mac
    return None
