def myfunc (input_array):
    
    # put array elements into set
    seq = set()
    for element in input_array:
        seq.add(element)
    
    # max subsequence length
    max = 0

    while (len(seq) > max):
        
        # current is base element that consecutive subsequence will be found around
        current = seq.pop()
        current_len = 1

        # check for consecutive chain of numbers greater than base number (increasing)
        next_num = current + 1
        while (next_num in seq):
            seq.remove(next_num)
            next_num += 1
            current_len += 1
        
        # check for consecutive chain of numbers less than base numner (decreasing)
        next_num = current - 1
        while (next_num in seq):
            seq.remove(next_num)
            next_num -= 1
            current_len += 1

        if (current_len > max):
            max = current_len

    # output into output.txt
    f = open("output.txt","w+")
    f.write(str(max))
    f.close



# first line
input = [1, 2, 3, 10, 4, 20, 2, 11, 39, 15, 100, 12, 13, 21, 17, 14]
myfunc(input)