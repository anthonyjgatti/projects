import sys, random, string, math

def radixSort(array, maxRadix = -1, radix = 1, base = 10):
    '''An implementation of radix sort taking an array.'''

    print('iterating...', radix * base)
    
    # Determine maximum radix on first pass
    if maxRadix < 0:
        maxRadix = len(str(max(array)))
    
    # Instantiate digit buckets, count array items ending in digit indexed by digit
    digits = [0]*base
    for x in array:
        digits[int(x / radix) % base] += 1

    # Overwrite digit as a running sum of elements in array
    for i in range(1,len(digits)):
        digits[i] = digits[i-1] + digits[i]

    # Allocate new array, descend array, decrement digit counter by index, write to output
    out_array = [0]*len(array)
    for x in reversed(array):
        digits[int(x / radix) % 10] -= 1
        out_array[digits[int(x / radix) % base]] = x

    # Recurse, stopping when radix * base equals base ^ max radix
    if int(base ** maxRadix) == radix * base:
        return out_array
    else:
        return radixSort(out_array, maxRadix, radix * base, base)
        
if __name__ == '__main__':
    
    def randomword(length):
        '''Test by implementing a random word generator.'''
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))

    # Hash word array
    word_array = [randomword(7) for _ in range(100)]
    in_array = [(hash(_) + sys.maxsize + 1) % (10 ** 8) for _ in word_array]
    
    # Print sorted hashed array
    x = radixSort(in_array)
    print(x)