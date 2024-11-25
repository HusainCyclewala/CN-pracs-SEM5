
#5 bit data aaya toh 4 parity le lena baaki same karo aage

#   HAMMING GENERATION
array = [None] * 7
data = input("Enter 4-bit data to send: ")

if len(data) != 4:
    print("Error")
else:
    array[0] = int(data[0])  
    array[1] = int(data[1])  
    array[2] = int(data[2])
    array[4] = int(data[3])

    sum1 = array[0] + array[2] + array[4]
    sum2 = array[0] + array[1] + array[4]
    sum3 = array[0] + array[1] + array[2]

    def isEven(sum):
        if sum % 2 == 0:
            return 0
        else:
            return 1

    p1 = isEven(sum1)
    p2 = isEven(sum2)
    p4 = isEven(sum3)

    array[6] = p1
    array[5] = p2
    array[3] = p4

    result = ''.join(map(str, array))
    print(result)




#  ERROR CORRECTION    
data = input("Enter 7-bit data that was transmitted: ")
array = [None] * 7
for i in range(0, 7):
    array[i] = int(data[i]) 

#  CALCULATING PARITY BITS 
sum1 = array[6] + array[4] + array[2] + array[0]    #p1
sum2 = array[5] + array[4] + array[1] + array[0]    #p2
sum3 = array[3] + array[2] + array[1] + array[0]    #p4

def isEven(sum):
    if sum % 2 == 0:
        return 0
    else:
        return 1

e1 = isEven(sum1)
e2 = isEven(sum2)
e3 = isEven(sum3)

errorbinary = f"{e3}{e2}{e1}"
errordecimal = int(errorbinary, 2)

print("Array:", array)
print("Error Position (Binary):", errorbinary)
print("Error Position (Decimal):", errordecimal)

if errordecimal != 0:  # Only flip if there's an error
    if array[7 - errordecimal] == 1:
        array[7 - errordecimal] = 0
    else:
        array[7 - errordecimal] = 1

print("Corrected data:", array)   




