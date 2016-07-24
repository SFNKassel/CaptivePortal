import mac_list
import time

ACTIVE_FILE = "users"
LOG_FILE = "log"

users = mac_list.read_file("users")
lf = open(LOG_FILE, "a")


def login(user, mac):
    users[mac] = user
    mac_list.write_file(ACTIVE_FILE, users)
    lf.write("%.1f: %s logged in  @%s\n" % (time.time(), user, mac))
    lf.flush()


def logout(mac):
    lf.write("%.1f: %s logged out @%s\n" % (time.time(), users[mac], mac))
    lf.flush()
    del users[mac]
    mac_list.write_file(ACTIVE_FILE, users)


def get_user(mac):
    try:
        user = users[mac]
    except KeyError:
        user = None
    return user
