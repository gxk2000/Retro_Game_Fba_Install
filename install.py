# -*- encoding: utf-8 -*-
import os
import shutil

# 清除上次安装
if os.path.exists("/home/cpi/launcher/skin/default/Menu/GameShell/20_Retro Games/FBA.png"):
    os.remove("/home/cpi/launcher/skin/default/Menu/GameShell/20_Retro Games/FBA.png")
if os.path.exists("/home/cpi/apps/emulators/fbalpha2012_libretro.so"):
    os.remove("/home/cpi/apps/emulators/fbalpha2012_libretro.so")
if os.path.exists("/home/cpi/apps/Menu/20_Retro Games/11_FBA"):
    os.removedirs("/home/cpi/apps/Menu/20_Retro Games/11_FBA")
if os.path.exists("/home/cpi/games/FBA"):
    os.removedirs("/home/cpi/games/FBA")

# 安装
shutil.move("/home/cpi/Retro_Game_Fba_Install/FBA.png", "/home/cpi/launcher/skin/default/Menu/GameShell/20_Retro Games/FBA.png")
shutil.move("/home/cpi/Retro_Game_Fba_Install/fbalpha2012_libretro.so", "/home/cpi/apps/emulators/fbalpha2012_libretro.so")
shutil.move("/home/cpi/Retro_Game_Fba_Install/11_FBA", "/home/cpi/apps/Menu/20_Retro Games/11_FBA")

# 提示
if os.path.exists("/home/cpi/launcher/skin/default/Menu/GameShell/20_Retro Games/FBA.png"):
    if os.path.exists("/home/cpi/apps/emulators/fbalpha2012_libretro.so"):
        if os.path.exists("/home/cpi/apps/Menu/20_Retro Games/11_FBA"):
            print("----- FBA模拟器安装完成！ -----")
else:
    print("----- FBA模拟器安装失败！ -----")
