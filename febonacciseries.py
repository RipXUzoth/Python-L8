n = int(input("Enter the number of terms: "))
a, b = 0,1
count = 0
print("Febonacci Series: ")
while count<n:
    print(a, end=" ")
    temp = a + b
    a = b
    b = temp
    count += 1