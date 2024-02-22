# Mohamad Ali Fakhoury Thurs @2pm
def swap_values(user_val1, user_val2, user_val3, user_val4):   
   n1 = user_val1
   n2 = user_val2
   n3 = user_val3
   n4 = user_val4
   user_val1 = n2
   user_val2 = n1
   user_val3 = n4
   user_val4 = n3
   print(f'{user_val1} {user_val2} {user_val3} {user_val4}')

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   swap_values(user_input1,user_input2,user_input3,user_input4)
   
   
   

 