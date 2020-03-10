import os

os.system('esptool.exe --port COM4 erase_flash')

os.system('esptool.exe --port COM4 --baud 1000000 write_flash -z 0x1000 esp32spiram-idf4-20200309-v1.12-213-g8db5d2d1f.bin')