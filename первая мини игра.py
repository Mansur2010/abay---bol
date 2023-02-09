# from mcpi.minecraft import Minecraft
# mc = Minecraft.create()
# from datetime import datetime
# import time
# import random
# x_start, y_start, z_start = mc.player.getTilePos()
# lava = 11
# lava1 = 10
# block = 4
# length = 50
# width = 50
#
# mc.setBlocks(x_start, y_start-1, z_start, x_start+length, y_start-1, z_start + width, 4)
# mc.setBlocks(x_start, y_start-3, z_start, x_start+length, y_start-3, z_start + width, 11)
# mc.postToChat("game is start in 10 seconds")
# time.sleep(10)
# start = datetime.now()
# while True:
#     x, y, z = mc.player.getTilePos()
#     mc.setBlock(x, y-1, z, 0)
#     if mc.getBlock(x, y, z) == lava or mc.getBlock(x, y, z) == lava1:
#         break
#     if x < x_start or x > x_start + length or z < z_start or z > z_start + length:
#         mc.player.setTilePos(x_start + random.randint(0, length), y_start, z_start + random.randint(0, width))
# mc.postToChat('game over.playtime:')
# mc.postToChat(datetime.now() - start)


# 31.01.23
# 1111111111111111111111111111111111



from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from datetime import datetime
import time
import random
import keyboard
x_start, y_start, z_start = mc.player.getTilePos()
qwert = 35, 9
qwerty = 169
c = 0
qwertyu = 35, 14
for x in range(25):
    for z in range(25):
        for y in range(25):
            mc.setBlock(x_start + x, y_start + y, z_start + z, random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, qwert, qwert, qwert, qwert, qwert, qwert, qwert, qwert, qwert,  qwert, qwert, qwert, qwerty, qwerty, qwerty]))
        y = 0
    z = 0

mc.postToChat("game is start in 10 seconds")
time.sleep(10)
start = datetime.now()
while True:
    x, y, z = mc.player.getTilePos()
    if keyboard.is_pressed("q"):
        mc.setting('world_immutable', True)
        mc.postToChat("мир неразрушаемый")

    elif keyboard.is_pressed("r"):
        mc.setting('world_immutable', False)
        mc.postToChat("мир разрушаемый")
    if y > y_start + 25:
        mc.postToChat('game over')
        break







































