import mac_list
import time

ACTIVE_FILE = "users"
LOG_FILE = "log"

users = mac_list.read_file("users")
lf = open(LOG_FILE, "a")


def login(user, mac):
    users[mac] = user
    mac_list.write_file(ACTIVE_FILE, users)
    lf.write("%s: %s logged in @%s" % (str(time.time()), user, mac))


def logout(mac):
    lf.write("%s: %s logged out @%s" % (str(time.time()), users[mac], mac))
    del users[mac]
    mac_list.write_file(ACTIVE_FILE, users)


def get_user(mac):
    try:
        user = users[mac]
    except KeyError:
        user = None
    return user
