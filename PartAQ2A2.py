if __name__ == '__main__':
    outfile_path = r'C:\Users\David Hunter\OneDrive\Northeastern Classes\Graduate\Computer Architecture\Homework4\PartA'
    block_size = 64 # Bytes
    cache_size = 8 # KBytes
    associativity = 4
    file = open(outfile_path + '/' + 'trace2.din', "a+")
    cache_size = int((cache_size * 1024)/associativity)  # Bytes

    for instruction in range(0, cache_size, block_size):
        cache_set = (instruction/block_size)%associativity

        if cache_set == 0:
            print(f'{instruction=} Set 0')
            file.write(f'2 {instruction:x}  \n')
        if cache_set == 1:
            print(f'{instruction=} Set 1')
            file.write(f'2 {instruction:x}  \n')
        if cache_set == 2:
            print(f'{instruction=} Set 2')
            file.write(f'2 {instruction:x}  \n')
        if cache_set == 3:
            print(f'{instruction=} Set 3')
            file.write(f'2 {instruction:x}  \n')

    for instruction in range(cache_size, 2*cache_size, block_size):
        cache_set = (instruction/block_size)%associativity

        if cache_set == 0:
            print(f'{instruction=} Set 0')
            file.write(f'2 {instruction:x}  \n')
        if cache_set == 1:
            print(f'{instruction=} Set 1')
            file.write(f'2 {instruction:x}  \n')
        if cache_set == 2:
            print(f'{instruction=} Set 2')
            file.write(f'2 {instruction:x}  \n')
        if cache_set == 3:
            print(f'{instruction=} Set 3')
            file.write(f'2 {instruction:x}  \n')

    for instruction in range(0, cache_size, block_size):
        cache_set = (instruction/block_size)%associativity

        if cache_set == 0:
            print(f'{instruction=} Set 0')
            file.write(f'2 {instruction:x}  \n')
        if cache_set == 1:
            print(f'{instruction=} Set 1')
            file.write(f'2 {instruction:x}  \n')
        if cache_set == 2:
            print(f'{instruction=} Set 2')
            file.write(f'2 {instruction:x}  \n')
        if cache_set == 3:
            print(f'{instruction=} Set 3')
            file.write(f'2 {instruction:x}  \n')



    file.close()
