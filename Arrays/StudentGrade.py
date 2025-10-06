tc = int(input("Enter No.of Test Cases :"))

for i in range(tc):
    num = int(input("Enter Number :"))
    c = 1 
    
    if num < 38:
        print(num)
    else:
        while(5 * c <= num):
            c += 1 
        
        if (5 * c - num < 3):
            print(5 * c)
        else:
            print(num)
        
