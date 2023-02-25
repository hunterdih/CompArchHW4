if __name__ == '__main__':
    outfile_path = r'C:\Users\David Hunter\OneDrive\Northeastern Classes\Graduate\Computer Architecture\Homework4\PartA'
    block_size = 16  # Bytes
    cache_size = 32  # KBytes
    cache_size_bytes = 1024  # Bytes
    associativity = 4
    file = open(outfile_path + '/' + 'trace5.din', "a+")

    for instruction in range(0, 1024, block_size):
        file.write(f'2 {hex(instruction)}    \n')
    for instruction in range(0, 1024, block_size):
        file.write(f'2 {hex(instruction)}    \n')

    for instruction in range(1024, 3072, block_size):
        file.write(f'2 {hex(instruction)}    \n')
    for instruction in range(1024, 3072, block_size):
        file.write(f'2 {hex(instruction)}    \n')

    for instruction in range(3072, 7168, block_size):
        file.write(f'2 {hex(instruction)}    \n')
    for instruction in range(3072, 7168, block_size):
        file.write(f'2 {hex(instruction)}    \n')

    for instruction in range((4 * 1024), (8 * 1024) + (4 * 1024), block_size):
        file.write(f'2 {hex(instruction)}    \n')
    for instruction in range((4 * 1024), (8 * 1024) + (4 * 1024), block_size):
        file.write(f'2 {hex(instruction)}    \n')

    for instruction in range((8 * 1024), (16 * 1024) + (8 * 1024), block_size):
        file.write(f'2 {hex(instruction)}    \n')
    for instruction in range((8 * 1024), (16 * 1024) + (8 * 1024), block_size):
        file.write(f'2 {hex(instruction)}    \n')

    for instruction in range((16 * 1024), (32 * 1024) + (16 * 1024), block_size):
        file.write(f'2 {hex(instruction)}    \n')
    for instruction in range((16 * 1024), (32 * 1024) + (16 * 1024), block_size):
        file.write(f'2 {hex(instruction)}    \n')
    file.close()
