# -*- encoding: utf-8 -*-
import os

if os.path.exists("/home/cpi/launcher/skin/default/Menu/GameShell/20_Retro Games/FBA.png"):
    os.remove("/home/cpi/launcher/skin/default/Menu/GameShell/20_Retro Games/FBA.png")

if os.path.exists("/home/cpi/apps/emulators/fbalpha2012_libretro.so"):
    os.remove("/home/cpi/apps/emulators/fbalpha2012_libretro.so")

if os.path.exists("/home/cpi/apps/Menu/20_Retro Games/11_FBA"):
    os.removedirs("/home/cpi/apps/Menu/20_Retro Games/11_FBA")

if os.path.exists("/home/cpi/games/FBA"):
    os.removedirs("/home/cpi/games/FBA")

print("----- fba模拟器已删除 -----")
