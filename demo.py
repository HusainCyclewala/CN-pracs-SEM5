print('\n \n')
print('nigga')
print("ypoo niogag")

list1= [1,9,4,4,5,3,2,7,9,7,8]
print(list1)

set1= set (list1)
print(set1)


c='hussy'
a= 4
b=99

print(str(a)+str(b)+c)              #TYPECAST INTO STRING
print("105 is ", 10-5) 
print("10 * 5 is ", 10*5)
print("10 / 5 is ", 10/5)
print("10 + 5 is ", 10+5)

#    IF ELSE SYNTAX
var1 = int(input("enter something: "))
print (var1, type(var1))

if(var1>4): 
    print("Variable is greater") 
elif (var1==2): 
    print("Variable is two") 
else: 
    print("Variable is not greater")

#     FOR LOOP  & WHILE LOOP
for i in range(0, 101): 
     print(i) 

i = 0 
while(i<101): 
 print(i) 
 i = i+1


#      FUNCTION
def average (no1,no2):
    avg= (no1+no2)/2
    return avg
print(average(3,9))


#   ERROR HANDLING
index=3
try:
    print (index)
except Exception as e: 
    print(e)


