from mcpi import minecraft
from time import sleep

mc = minecraft.Minecraft.create()

tnt = 46

x,y,z = mc.player.getPos()

mc.setBlocks(x+1,y+1,z+1, x+11, y+11, z+11, tnt, 1)