from pathlib import Path
import numpy as np


if __name__ == '__main__':
    outfile_path = r'C:\Users\dihdd\OneDrive\Northeastern Classes\Graduate\Computer Architecture\Homework4\PartA'
    block_size = 64
    cache_size = 8 #KB
    cache_size = 8*1024
    loops = 3
    associativity = 4
    file = open(outfile_path + '/' + 'trace2.din', "a+")

    for offset in range(0, loops):
        for instruction in range(0 + associativity * (offset * block_size),
                                 cache_size+associativity*(offset*block_size),
                                 block_size*associativity):

            file.write(str(f"2 {hex(instruction)}    \n"))

            file.write(str(f"2 {hex(instruction)}    \n"))

    file.close()
