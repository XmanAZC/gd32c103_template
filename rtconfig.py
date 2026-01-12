import os

# toolchains options
ARCH='arm'
CPU='cortex-m4'
CROSS_TOOL='gcc'
TARGET = "gd32c10x_template"

# bsp lib config
BSP_LIBRARY_TYPE = None

PLATFORM    = 'gcc'

if os.getenv('RTT_EXEC_PATH'):
    EXEC_PATH = os.getenv('RTT_EXEC_PATH')

# toolchains
PREFIX = 'arm-none-eabi-'
CC = PREFIX + 'gcc'
AS = PREFIX + 'gcc'
AR = PREFIX + 'ar'
CXX = PREFIX + 'g++'
LINK = PREFIX + 'gcc'
TARGET_EXT = 'elf'
SIZE = PREFIX + 'size'
OBJDUMP = PREFIX + 'objdump'
OBJCPY = PREFIX + 'objcopy'
DEVICE = ' -mcpu=cortex-m4 -mthumb -mfpu=fpv4-sp-d16 -mfloat-abi=hard -ffunction-sections -fdata-sections'
CFLAGS = DEVICE + ' -Dgcc -g -O0'
AFLAGS = ' -c' + DEVICE + ' -x assembler-with-cpp -Wa,-mimplicit-it=thumb '
LFLAGS = DEVICE + f' -Wl,--gc-sections,-Map={TARGET}.map,-cref,-u,Reset_Handler -T link.ld.tmp'
CPATH = ''
LPATH = ''

CXXFLAGS = CFLAGS 
POST_ACTION = OBJCPY + f' -O binary {TARGET}.elf {TARGET}.bin\n' + SIZE + f' {TARGET}.elf \n'


def dist_handle(BSP_ROOT, dist_dir):
    import sys
    cwd_path = os.getcwd()
    sys.path.append(os.path.join(os.path.dirname(BSP_ROOT), 'tools'))
    from sdk_dist import dist_do_building
    dist_do_building(BSP_ROOT, dist_dir)
