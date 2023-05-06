import random
import sys
import subprocess
subprocess.run("export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH", shell=True)
from cpgames import cpgames

game_client = cpgames.CPGames()
all_supports = game_client.getallsupported()
game_list = list(all_supports.values())
subprocess.run("clear", shell=True)
number = 1
for game in game_list:
    print(f"{number}.{game}")
    number += 1
code = input("number: ").strip()
n = int(code)
game = game_list[n-1]
game_client.execute(game)
#game_client.execute(random.choice(list(all_supports.values())))
