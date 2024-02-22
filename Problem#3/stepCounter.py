# Mohamad Ali Fakhoury Thurs @2pm
def feet_to_steps(user_feet):
   return(user_feet/2.5)

if __name__ == '__main__':
    user_feet = float(input())
    steps = int(feet_to_steps(user_feet))
    print(steps)