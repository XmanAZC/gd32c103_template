import os
Import('RTT_ROOT')
from building import *

src = []

group = DefineGroup('app', src, depend = [''], CPPPATH = [''])

group = group + SConscript('application/SConscript')

# include libraries
group = group + SConscript('GD32C10x_Firmware_Library/SConscript')

# include drivers
group = group + SConscript('gd32_drivers/SConscript')

# include mcu components
group = group + SConscript('mcu_components/SConscript')

Return('group')
