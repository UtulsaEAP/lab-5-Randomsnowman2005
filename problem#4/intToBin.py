# Mohamad Ali Fakhoury Thurs @2pm
def int_to_reverse_binary(num1):
    binary_val = ''
#write your while loop here
    while num1 > 0:
        binary_val = binary_val + str(num1 % 2)
        num1 = num1 // 2
    return(binary_val)


def string_reverse(input_string): 
    reverse_input = ''
    z = len(input_string)
    word = str(input_string)
    while z> 0:
        num = word[z-1]
        reverse_input = reverse_input + num
        z = z -1
    return reverse_input


if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)