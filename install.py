# -*- encoding: utf-8 -*-
#pay attention this project was base in python2

import os
import shutil

print("----- FBA模拟器开始安装！ -----")
os.system('cd /home/cpi/Retro_Game_Fba_Install')
shutil.move('FBA.png', "/home/cpi/launcher/skin/default/Menu/GameShell/20_Retro Games/FBA.png")
shutil.move("fbalpha2012_libretro.so", "/home/cpi/apps/emulators/fbalpha2012_libretro.so")
shutil.move('11_FBA', "/home/cpi/apps/Menu/20_Retro Games/11_FBA")
os.system('rm - rf /home/cpi/Retro_Game_Fba_Install')
print("----- FBA模拟器安装完成！ -----")
