import json
import os.path


class Users_List:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.isfile(filename):
            with open(self.filename, "w") as outfile:
                json.dump({}, outfile)

    def __len__(self):
        return self.get_list().len

    def __getitem__(self, mac):
        return self.get_list()[mac]

    def __delitem__(self, mac):
        list = self.get_list()
        del list[mac]
        self.store_list(list)

    def __setitem__(self, mac, val):
        list = self.get_list()
        list[mac] = val
        self.store_list(list)

    def __iter__(self):
        list = self.get_list()
        for i in list:
            yield i

    def get_list(self):
        with open(self.filename, "r") as infile:
            users = json.load(infile)
        return users

    def store_list(self, users):
        with open(self.filename, "w") as outfile:
            json.dump(users, outfile)
