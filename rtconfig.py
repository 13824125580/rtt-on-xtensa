import os
#env=Environment(ENV=os.environ)
#env.PrependENVPath('PATH','/home/zilong/WorkSpace/IOT/esp32/rtthread-esp/xtensa-esp32-elf/bin')

# toolchains options
ARCH='xtensa'
CPU='esp32'
CROSS_TOOL='gcc'
BOARD_NAME = 'ESP-WROOM-32'

if os.getenv('RTT_CC'):
    CROSS_TOOL = os.getenv('RTT_CC')

if  CROSS_TOOL == 'gcc':
    PLATFORM    = 'gcc'
    EXEC_PATH   = r'D:\tools\msys32\opt\xtensa-esp32-elf\bin'
else:
    print '================ERROR============================'
    print 'Unknown compiler'
    print '================================================='
    exit(0)

if os.getenv('RTT_EXEC_PATH'):
    EXEC_PATH = os.getenv('RTT_EXEC_PATH')

BUILD = 'debug'

if PLATFORM == 'gcc':
    # toolchains
    PREFIX = 'xtensa-esp32-elf-'
    CC  = PREFIX + 'gcc'
    CXX = PREFIX + 'g++'
    AS = PREFIX + 'gcc'
    AR = PREFIX + 'ar'
    LINK = PREFIX + 'g++'
    TARGET_EXT = 'elf'
    SIZE = PREFIX + 'size'
    OBJDUMP = PREFIX + 'objdump'
    OBJCPY = PREFIX + 'objcopy'

    DEVICE = ' '
    CFLAGS = DEVICE + '-Os -ffunction-sections -fdata-sections -fstrict-volatile-bitfields -mlongcalls -nostdlib -Wall'
    AFLAGS = ' -c' + DEVICE + ' -x assembler-with-cpp -MMD -MP -I./esp-idf/components/freertos/include/freertos -I./esp-idf/components/esp32/include -I.'
    LFLAGS = DEVICE + ' -u call_user_start_cpu0 -u __cxa_guard_dummy -Wl,--undefined=uxTopUsedPriority,--gc-sections,-Map=rtthread-esp32.map,-cref,-static -nostdlib -T esp32_out.ld -T esp32.common.ld -T esp32.rom.ld -T esp32.peripherals.ld -Wl,--defsym=rtc_set_cpu_freq=0x40000000 -Wl,--defsym=esp_wifi_stop=0x40000000 -Wl,--defsym=esp_wifi_connect=0x40000000   -Wl,--defsym=esp_wifi_init=0x40000000 -Wl,--defsym=esp_wifi_set_storage=0x40000000 -Wl,--defsym=esp_wifi_set_mode=0x40000000 -Wl,--defsym=esp_wifi_start=0x40000000 -Wl,--defsym=esp_wifi_get_config=0x40000000 -Wl,--defsym=esp_wifi_start=0x40000000 -Wl,--defsym=esp_wifi_get_config=0x40000000 -Wl,--defsym=esp_wifi_disconnect=0x40000000 -Wl,--defsym=esp_wifi_set_config=0x40000000 -Wl,--defsym=esp_smartconfig_start=0x40000000 -Wl,--defsym=esp_smartconfig_set_type=0x40000000 -Wl,--defsym=esp_smartconfig_stop=0x40000000 -Wl,--defsym=rtc_init_lite=0x40000000 -Wl,--defsym=esp_wifi_internal_reg_rxcb=0x40000000 -Wl,--defsym=esp_wifi_get_mac=0x40000000 -Wl,--defsym=esp_wifi_internal_set_sta_ip=0x40000000 -Wl,--defsym=esp_wifi_internal_tx=0x40000000 -Wl,--defsym=esp_wifi_internal_free_rx_buffer=0x400000000' 

    CPATH = ''
    LPATH = ''

    if BUILD == 'debug':
        CFLAGS += ' -ggdb'
        AFLAGS += ' -ggdb'
    else:
        CFLAGS += ' -O2'

    CXXFLAGS = CFLAGS + ' -std=gnu++11 -fno-exceptions -fno-rtti'
    CFLAGS   = CFLAGS + ' -std=gnu99'

    POST_ACTION = SIZE + ' $TARGET \n'
