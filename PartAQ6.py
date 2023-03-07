if __name__ == '__main__':
    outfile_path = r'C:\Users\David Hunter\OneDrive\Northeastern Classes\Graduate\Computer Architecture\Homework4\PartA'
    block_size = 16  # Bytes
    cache_size = 32  # KBytes
    cache_size_bytes =cache_size* 1024  # Bytes
    associativity = 4
    file = open(outfile_path + '/' + 'trace6.din', "a+")
    address_list = []
    # Fill the cache set0
    for address in range(0, associativity * cache_size_bytes, cache_size_bytes):
        address_list.append(f'2 {address:x}  \n')
    file.writelines(address_list)
    # Access the first address once (0x0)
    file.write(f'2 {0:x}  \n') # Results in a Hit
    # Pass a new address that will require a replacement
    file.write(f'2 {(associativity*cache_size_bytes):x}  \n')
    # Check to see if the first entry is still in the cache (0x0)
    file.write(f'2 {0:x}  \n') # If a hit results, then LRU replacement, if not, then random or FIFO
    file.close()