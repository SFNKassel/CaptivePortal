from flask import Flask, request, send_from_directory
import testAuth as auth
import netUtil as nu
import fileUtils as fu

app = Flask(__name__)
users = {}

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

@app.route('/api/login')
def api():
    try:
        ip = request.remote_addr
        user = request.args.get("user")
        passwd = request.args.get("passwd")
        mac = nu.mac_for_ip(ip)
    except(Exception):
        print(Exception)
        #do nothing, something was not set

    print(ip)
    print(mac)
    print(user)
    print(passwd)

    if(not user and not passwd):
        print("state check")

    if(auth.test(user, passwd)):
        name = auth.getName(user)
        users[ip] = user
        fu.writeFile("users", users)
        return name, 202
    else:
        return "wrong username or password", "401"

@app.route('/api/logout')
def logout():
    try:
        del users[request.remote_addr]
        fu.writeFile("users", users)
        return "logged out sucessfully", 202
    except(KeyError):
        return "you are not logged in", 400

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
    users = fu.readFile("users")
