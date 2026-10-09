import subprocess

for i in range(10):
    result = subprocess.run(["ping", "-n", "1", "google.com"])
