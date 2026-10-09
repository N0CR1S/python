import subprocess

for i in range(10):
    subprocess.Popen(['powershell', 'start-process cmd.exe'])
