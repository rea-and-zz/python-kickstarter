# Input: an integer like 13323
# An integer which is the "spoken" version of the number, see:
# 113323

def speak_number(number):
    number_str = str(number)
    new_str = []
    block_size = 0
    block_char = None
    for i, char in enumerate(number_str):
        if (char != block_char and block_char != None) or i == len(number_str)-1:
            # previous sequence is over, flush
            new_str.append(str(block_size))
            new_str.append(block_char)
            block_size = 0
        block_char = char
        block_size += 1
    return (int(''.join(new_str)))
  
input = 1134555
print('Speak The Number App!')
print('Input: {}\nResult: {}'.format(input, speak_number(input)))




