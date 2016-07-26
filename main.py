#!/usr/bin/env python2
from flask import Flask, request, redirect
import auth #auth_test as auth
import ip2mac
import login_manager as l
import os
from multiprocessing import Process

app = Flask(__name__)


# make development easier and disable browser-cache
@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "public, max-age=0"
    return response


@app.route('/')
def index():
    return app.send_static_file('index.html'), "511 network authentication required"


@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

@app.errorhandler(404)
def page_not_found(e):
    return index()


@app.route('/api/login')
def login():
    user = request.args.get("user")
    passwd = request.args.get("passwd")

    if not user or not passwd:
        return "username or password missing!", 400

    if auth.check_credentials(user, passwd):
        mac = ip2mac.lookup(request.remote_addr)
	if(not mac):
		return "not in network", 500
        l.login(user, mac)
        name = auth.get_name(user)
        return '{"user": "%s", "name": "%s"}' % (user, name), 202
    else:
        return "wrong username or password", 401


@app.route('/api/logout')
def logout():
    try:
        mac = ip2mac.lookup(request.remote_addr)
        l.logout(mac)
        return "logged out successfully", 202
    except KeyError:
        return "you are not logged in", 400


@app.route('/api/state')
def state():
    mac = ip2mac.lookup(request.remote_addr)
    user = l.get_user(mac)
    name = auth.get_name(user)
    if user:
        return '{"user": "%s", "name": "%s"}' % (user, name), 200
    else:
        return "you are not logged in", 511

def launch_https():
    app.run(host="0.0.0.0", port=5001, ssl_context='adhoc')
    


if __name__ == "__main__":
    os.system("iptables -I INPUT -p tcp -m tcp --dport 5000 -j ACCEPT")
    os.system("iptables -I INPUT -p tcp -m tcp --dport 5001 -j ACCEPT")
    os.system("iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to 192.168.1.1:5000")
    os.system("iptables -t nat -A PREROUTING -p tcp --dport 443 -j DNAT --to 192.168.1.1:5001")

    Process(target=launch_https).start()
    app.run(host="0.0.0.0", port=5000)
