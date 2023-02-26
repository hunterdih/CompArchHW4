if __name__ == '__main__':
    outfile_path = r'C:\Users\David Hunter\OneDrive\Northeastern Classes\Graduate\Computer Architecture\Homework4\PartA'
    block_size = 16  # Bytes
    cache_size = 32  # KBytes
    cache_size_bytes =cache_size* 1024  # Bytes
    max_associativity = 4
    file = open(outfile_path + '/' + 'trace5.din', "a+")
    address_list = []
    for address in range(0, max_associativity*cache_size_bytes, cache_size_bytes):
        address_list.append(f'2 {address:x}  \n')
    file.writelines(address_list)
    reversed_address_list = address_list[::-1]
    file.writelines(reversed_address_list)
    file.close()

