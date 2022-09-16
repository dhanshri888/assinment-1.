# write a python program to get the fibonacci series between 0 to 50
#o 1 1 2 3 5 8 13 21
# output - 1 1 2 3 5 8 13 21 34

num = int(input("Enter the number in terms:"))
no1 = 0
no2 = 1
no3 = 0

for x in range(num):
    print(no3,end = " ")
    no3 = no1 + no2
    no2 = no1
    no1 = no3
    


    


    

