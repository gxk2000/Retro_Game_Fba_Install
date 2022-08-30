# -*- encoding: utf-8 -*-
import os
import shutil
from exts import de_clifile,de_file,copy


# 清除上次安装
if os.path.exists("/home/cpi/launcher/skin/default/Menu/GameShell/20_Retro Games/FBA.png"):
    fpath = r"/home/cpi/launcher/skin/default/Menu/GameShell/20_Retro Games/FBA.png"
    de_file(fpath)

if os.path.exists("/home/cpi/apps/emulators/fbalpha2012_libretro.so"):
    fpath = r"/home/cpi/apps/emulators/fbalpha2012_libretro.so"
    de_file(fpath)

if os.path.exists("/home/cpi/apps/Menu/20_Retro Games/11_FBA"):
    cfpath = r"/home/cpi/apps/Menu/20_Retro Games/11_FBA"
    de_clifile(cfpath)

if os.path.exists("/home/cpi/games/FBA"):
    cfpath = r"/home/cpi/games/FBA"
    de_clifile(cfpath)


# 安装
shutil.copyfile("/home/cpi/Retro_Game_Fba_Install/FBA.png", "/home/cpi/launcher/skin/default/Menu/GameShell/20_Retro Games/FBA.png")
shutil.copyfile("/home/cpi/Retro_Game_Fba_Install/fbalpha2012_libretro.so", "/home/cpi/apps/emulators/fbalpha2012_libretro.so")
old = r"/home/cpi/Retro_Game_Fba_Install/11_FBA"
new = r"/home/cpi/apps/Menu/20_Retro Games/11_FBA"
copy(old,new)


# 提示
if os.path.exists("/home/cpi/launcher/skin/default/Menu/GameShell/20_Retro Games/FBA.png"):
    if os.path.exists("/home/cpi/apps/emulators/fbalpha2012_libretro.so"):
        if os.path.exists("/home/cpi/apps/Menu/20_Retro Games/11_FBA"):
            print("----- FBA模拟器安装完成！ -----")
else:
    print("----- FBA模拟器安装失败！ -----")
