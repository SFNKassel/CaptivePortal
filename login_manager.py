from logger import Logger
from users_list import Users_List
import iptables

USERS_FILE = "users"
LOG_FILE = "log"

# initialize the users list and add ldap rules for existing users
users = Users_List(USERS_FILE)
for mac in users:
    iptables.add_mac()

# initialize the logger
l = Logger(LOG_FILE)


def login(user, mac):
    # modify the iptables rule
    iptables.add_mac(mac)

    # modify persistent foo
    users[mac] = user

    # log the login
    l.log("%s logged out @%s" % (users[mac], mac))


def logout(mac):
    # modify the iptables rule
    iptables.remove_mac(mac)

    # modify persistent foo
    del users[mac]

    # log the login
    l.log("%s logged out @%s" % (users[mac], mac))


def get_user(mac):
    try:
        user = users[mac]
    except KeyError:
        user = None
    return user
