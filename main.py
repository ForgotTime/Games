import subprocess
file = open("game_status.txt", "w")
file.close()
while True:
    file = open("game_status.txt", "r")
    content = file.read().strip()
    file.close()
    if content == "q":
        break
    subprocess.run("python3 test.py", shell=True)
print("bye~~")