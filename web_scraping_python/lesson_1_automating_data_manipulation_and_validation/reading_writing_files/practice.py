#automating terminal commands w/ python Subprocess module.
#Subprocess library connects python w/ CLI.
import subprocess

for i in range(20):
    subprocess.check_call(["python3", "example.py"])

#only works in CLI and not REPL
#same as running "python3 example.py" 20 times manually in CLI
#we run a py file 20 times from another file (automation)