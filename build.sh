#!/bin/bash
export RTT_EXEC_PATH=/home/debian/software/gcc-arm-none-eabi-10.3-2021.10/bin
cat link.ld | sed 's/\<ROM_ORIGIN\>/0x8000000/g' | sed 's/\<ROM_LENGTH\>/128k/g' > link.ld.tmp

mkdir -p build
scons -j"${nproc} -1"
