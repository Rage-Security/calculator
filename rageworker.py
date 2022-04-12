#import http.server
#import socketserver
#import socket
import subprocess
import os



os.system('rm -rf ~/.cache/main.py/')
os.system('rm -rf static/*')




'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
addr = s.getsockname()
s.close()


with open('lp','w') as lpf:
    lpf.write(str(addr[1]))
    lpf.close()

PORT = addr[1]
'''

subprocess.Popen(['python3','cp1.py'])
subprocess.Popen(['python3','main.py'])


'''
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Server started at 127.0.0.1:" + str(PORT))
    httpd.serve_forever()
'''