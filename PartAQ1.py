from pathlib import Path
import numpy as np


if __name__ == '__main__':
    outfile_path = r'C:\Users\David Hunter\OneDrive\Northeastern Classes\Graduate\Computer Architecture\Homework4\PartA'
    block_size = 64
    cache_size = 8 #KB

    cache_size = 8*1024
    file = open(outfile_path + '/' + 'trace1.txt', "a+")
    for instruction in range(0,cache_size, block_size):
        file.write(f'2 {instruction:x}\n')

    file.close()
