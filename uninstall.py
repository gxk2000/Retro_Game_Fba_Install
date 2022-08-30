# -*- encoding: utf-8 -*-
import os
from exts import de_clifile,de_file


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

print("----- fba模拟器已删除! -----")
