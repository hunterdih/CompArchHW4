if __name__ == '__main__':
    outfile_path = r'C:\Users\David Hunter\OneDrive\Northeastern Classes\Graduate\Computer Architecture\Homework4\PartA'
    block_size = 64  # Bytes
    cache_size = 8  # KBytes
    cache_size = cache_size * 1024  # Bytes
    associativity = 4
    file = open(outfile_path + '/' + 'trace3.din', "a+")

    for instruction in range(0, cache_size, block_size):
        file.write(f'2 {hex(instruction)}    \n')  # Miss
        file.write(f'2 {hex(instruction)}    \n')  # Hit

    for instruction in range(cache_size, 2 * cache_size, block_size):
        file.write(f'2 {hex(instruction)}    \n')  # Miss
        file.write(f'2 {hex(instruction)}    \n')  # Hit

    for instruction in range(2*cache_size, 3 * cache_size, block_size):
        file.write(f'2 {hex(instruction)}    \n')  # Miss
        file.write(f'2 {hex(instruction)}    \n')  # Hit

        # 3 Memory address values per line used, revert to first memory address
    for instruction in range(0, cache_size, block_size):
        file.write(f'2 {hex(instruction)}    \n')  # Miss
        file.write(f'2 {hex(instruction)}    \n')  # Hit

    for instruction in range(cache_size, 2 * cache_size, block_size):
        file.write(f'2 {hex(instruction)}    \n')  # Miss
        file.write(f'2 {hex(instruction)}    \n')  # Hit
    file.close()
