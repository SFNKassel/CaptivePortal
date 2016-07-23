from flask import Flask, request, send_from_directory
import testAuth as auth
import netUtil as nu

app = Flask(__name__)

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

@app.route('/api')
def api():
    try:
        ip = request.remote_addr
        user = request.args.get("user")
        passwd = request.args.get("passwd")
        mac = nu.mac_for_ip(ip)
    except(Exception):
        print(Exception)

    if(!mac):
        return "mac not found!", "500"

    if(!user and !passwd):
        #return state

    name = auth.test(user, passwd)
    if(name):
        return name, 202
    else:
        return "wrong username or password", "401"

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
