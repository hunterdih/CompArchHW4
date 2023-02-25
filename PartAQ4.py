if __name__ == '__main__':
    outfile_path = r'C:\Users\David Hunter\OneDrive\Northeastern Classes\Graduate\Computer Architecture\Homework4\PartA'
    block_size = 32  # Bytes
    cache_size = 32  # KBytes
    cache_size = cache_size * 1024  # Bytes
    associativity = 4
    file = open(outfile_path + '/' + 'trace4.din', "a+")

    loops = (cache_size / block_size) / associativity

    for instruction in range(0, cache_size, block_size):
        file.write(f'0 {hex(instruction)}    \n')  # Miss
        file.write(f'1 {hex(instruction)}    \n')  # Hit

    for instruction in range(cache_size, 2 * cache_size, block_size):
        file.write(f'1 {hex(instruction)}    \n')  # Miss
        file.write(f'0 {hex(instruction)}    \n')  # Hit

    for instruction in range(2*cache_size, 3 * cache_size, block_size):
        file.write(f'0 {hex(instruction)}    \n')  # Miss
        file.write(f'1 {hex(instruction)}    \n')  # Hit

        # 3 Memory address values per line used, revert to first memory address
    for instruction in range(0, cache_size, block_size):
        file.write(f'1 {hex(instruction)}    \n')  # Miss
        file.write(f'0 {hex(instruction)}    \n')  # Hit

    for instruction in range(cache_size, 2 * cache_size, block_size):
        file.write(f'0 {hex(instruction)}    \n')  # Miss
        file.write(f'1 {hex(instruction)}    \n')  # Hit
    file.close()