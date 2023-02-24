from pathlib import Path
import numpy as np


if __name__ == '__main__':
    outfile_path = r'C:\Users\dihdd\OneDrive\Northeastern Classes\Graduate\Computer Architecture\Homework4\PartA'
    block_size = 64
    cache_size = 8 #KB
    offset = 64
    cache_size = 8*1024
    file = open(outfile_path + '/' + 'trace1.din', "a+")
    write_list = []
    for instruction in range(offset,cache_size+offset, block_size):
        file.write(str(f"2 {hex(instruction)}    \n"))

    for instruction in range(offset,cache_size+offset, block_size):
        file.write(str(f"2 {hex(instruction)}    \n"))

    file.close()
