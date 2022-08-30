# -*- encoding: utf-8 -*-
import os
import shutil

shutil.move("/home/cpi/Retro_Game_Fba_Install/FBA.png", "/home/cpi/launcher/skin/default/Menu/GameShell/20_Retro Games/FBA.png")
shutil.move("/home/cpi/Retro_Game_Fba_Install/fbalpha2012_libretro.so", "/home/cpi/apps/emulators/fbalpha2012_libretro.so")
shutil.move("/home/cpi/Retro_Game_Fba_Install/11_FBA", "/home/cpi/apps/Menu/20_Retro Games/11_FBA")
os.system("rm -rf /home/cpi/Retro_Game_Fba_Install")
print("----- FBA模拟器安装完成！ -----")
