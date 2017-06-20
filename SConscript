from building import *
import os
env=Environment(ENV=os.environ)
env.PrependENVPath('PATH','/home/zilong/WorkSpace/IOT/esp32/rtthread-esp/xtensa-esp32-elf/bin')

cwd = str(Dir('#'))
objs = []
list = os.listdir(cwd)

for d in list:
    path = os.path.join(cwd, d)
    if os.path.isfile(os.path.join(path, 'SConscript')):
        objs = objs + SConscript(os.path.join(d, 'SConscript'))

Return('objs')
