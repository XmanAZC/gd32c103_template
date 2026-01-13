#!/bin/bash
# TODO: 替换为你的交叉编译器路径
export RTT_EXEC_PATH=/home/debian/software/gcc-arm-none-eabi-10.3-2021.10/bin

# 获取构建模式，默认为 debug
BUILD_MODE="${1:-debug}"

case "$BUILD_MODE" in
    debug)
        echo "=== Building in DEBUG mode ==="
        export BUILD_TYPE=debug
        cat link.ld | sed 's/\<ROM_ORIGIN\>/0x8000000/g' | sed 's/\<ROM_LENGTH\>/128k/g' > link.ld.tmp
        mkdir -p build
        scons -j"$(nproc)"
        ;;
    release)
        echo "=== Building in RELEASE mode ==="
        export BUILD_TYPE=release
        cat link.ld | sed 's/\<ROM_ORIGIN\>/0x8000000/g' | sed 's/\<ROM_LENGTH\>/128k/g' > link.ld.tmp
        mkdir -p build
        scons -j"$(nproc)"
        ;;
    clean)
        echo "=== Cleaning build ==="
        scons -c
        rm -rf build
        rm -f link.ld.tmp
        rm -f *.elf *.bin *.map
        echo "=== Clean completed ==="
        ;;
    *)
        echo "Usage: $0 [debug|release|clean]"
        echo "  debug   - Build with debug flags (default)"
        echo "  release - Build with release optimization"
        echo "  clean   - Clean all build artifacts"
        exit 1
        ;;
esac
