rom mcpi import minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

mc.setBlock(x+3,y,z,block.STONE.id)

dirt = 3
wool = 35

mc.setBlock(x,y,z,dirt)

mc.setBlock(x+2,y,z,wool,1)