import pandas as pd
import numpy as np

CACHE_SIZE = 8  # In KBytes

BLOCK_SIZE = 16  # In Bytes
ADDRESS_STREAM_PATH = r'C:\Users\David Hunter\OneDrive\Northeastern Classes\Graduate\Computer Architecture\Homework4\PartB\tracefile\trace'

if __name__ == '__main__':
    dataset = pd.read_csv(ADDRESS_STREAM_PATH, delimiter=' ')

    # Program is intended to only model an instruction cache, so other instructions can be ignored
    # Select instruction addresses
    instruction_stream = dataset[dataset.values[:, 0] == 2]
    instruction_stream = np.squeeze(instruction_stream.values[:, 1])
    number_cache_indexes = int((8 * 1024) / BLOCK_SIZE)
    # Create the column cache
    column_cache = pd.DataFrame(index=range(number_cache_indexes), columns=range(2))
    column_cache = column_cache.set_axis(['Address', 'Rehash'], axis=1, inplace=False)
    temp_cache_address = ' '
    temp_cache_rehash = 1
    instruction_total = instruction_stream.shape[0]
    print(f'Number of Instruction Addresses to Process: {instruction_total}')
    column_cache['Rehash'] = 1
    miss_total = 0
    hit_total = 0
    instr_count = 0

    # Start filling in the cache
    for address in instruction_stream:
        instr_count += 1
        if instr_count%10000 == 0:
            print(f'Processed {instr_count} Instructions...')
        address = int(address, 16)
        # Initial hashing index calculation (assumed that the address is stored, no need to calculate tag or index field)
        cache_index_1 = int(address % (int(number_cache_indexes / 2)))
        # Check if index is occupied, if occupied then rehash and check next hashed index
        if not address == column_cache['Address'][cache_index_1]:  # MISS
            if column_cache['Rehash'][cache_index_1] == 1:
                # Update stored address
                column_cache['Address'][cache_index_1] = address
                # Update Rehash bit
                column_cache['Rehash'][cache_index_1] = 0
            else:
                cache_index_2 = int(cache_index_1 + (number_cache_indexes / 2))
                # Check if address is stored in the offset portion of the cache
                if not address == column_cache['Address'][cache_index_2]:  # MISS
                    miss_total += 1
                    # Store address in cache
                    column_cache['Address'][cache_index_2] = address
                    column_cache['Rehash'][cache_index_2] = 0

                    # Perform swap
                    # Load to temp cache
                    temp_cache_addr = column_cache['Address'][cache_index_1]
                    temp_cache_rehash = column_cache['Rehash'][cache_index_1]

                    # Swap 2 into 1
                    column_cache['Address'][cache_index_1] = column_cache['Address'][cache_index_2]
                    column_cache['Rehash'][cache_index_1] = column_cache['Rehash'][cache_index_2]

                    # Swap temp (1) into 2
                    column_cache['Address'][cache_index_2] = temp_cache_addr
                    column_cache['Rehash'][cache_index_2] = temp_cache_rehash
                # Condition for a delayed hit
                else:  # HIT
                    hit_total += 1

                    # Perform swap
                    # Load to temp cache
                    temp_cache_addr = column_cache['Address'][cache_index_1]
                    temp_cache_rehash = column_cache['Rehash'][cache_index_1]

                    # Swap 2 into 1
                    column_cache['Address'][cache_index_1] = column_cache['Address'][cache_index_2]
                    column_cache['Rehash'][cache_index_1] = column_cache['Rehash'][cache_index_2]

                    # Swap temp (1) into 2
                    column_cache['Address'][cache_index_2] = temp_cache_addr
                    column_cache['Rehash'][cache_index_2] = temp_cache_rehash
        # Condition for hit on the first check
        else:  # HIT
            hit_total += 1

    print(f'Compiling Results for Column Cache...')
    print(f'Hit Ratio = {hit_total/instruction_total}')
    print(f'Miss Ratio = {miss_total/instruction_total}')
    print(f'\n')