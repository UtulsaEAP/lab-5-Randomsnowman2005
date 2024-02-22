# Mohamad Ali Fakhoury Thurs @2pm
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   gallons = miles_driven /miles_per_gallon
   return(gallons * dollars_per_gallon)


if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    print(f'{driving_cost(miles_per_gallon,dollars_per_gallon,10):.2f}')
    print(f'{driving_cost(miles_per_gallon,dollars_per_gallon,50):.2f}')
    print(f'{driving_cost(miles_per_gallon,dollars_per_gallon,400):.2f}')

    
   