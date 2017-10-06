from mcpi import minecraft

mc = minecraft.Minecraft.create()
mc.postToChat("Hello World !")

x,y,z = mc.player.getPos()
mc.player.setPos(x, y+100, z)

mc.setBlock(x+1,y,z,1)
mc.setBlock(x+1,y,z,2)
