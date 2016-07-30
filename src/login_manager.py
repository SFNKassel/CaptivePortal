from logger import Logger
from users_list import Users_List
import iptables

USERS_FILE = "/etc/captive.users"
LOG_FILE = "/var/log/captivePortal.log"

# initialize the logger
l = Logger(LOG_FILE)

# read the user list
users = Users_List(USERS_FILE)

# initialize the users list and add ldap rules for existing users
def init():
    for mac in users:
        print("adding mac" + mac)
        iptables.add_mac(mac)

def login(user, mac):
    # modify the iptables rule
    iptables.add_mac(mac)

    # modify persistent foo
    users[mac] = user

    # log the login
    l.log("%s logged in @%s" % (users[mac], mac))


def logout(mac):
    # modify the iptables rule
    iptables.remove_mac(mac)

    # log the login
    l.log("%s logged out @%s" % (users[mac], mac))

    # modify persistent foo
    del users[mac]


def get_user(mac):
    try:
        user = users[mac]
    except KeyError:
        user = None
    return user
