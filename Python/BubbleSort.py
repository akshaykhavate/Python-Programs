num_array = list()
num = input("Enter how many elements you want:")
print('Enter numbers in array: ')
for i in range(int(num)):
    n = input("num :")
    num_array.append(int(n))
print('ARRAY: ',num_array)
print(len(num_array))
for i in range(0,len(num_array)):
    for j in range(1,len(num_array)):
        if num_array[j-1]>num_array[j]:
            num_array[j-1],num_array[j]=num_array[j],num_array[j-1]
    print('ARRAY: ',num_array)
