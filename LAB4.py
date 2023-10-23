# Opening a file for reading
file = open("LAB4.txt", "r")

# Reading file content

content = file.readlines()
sumi = 0
products = 1
for line in content:
    #sumi = sumi + int(line)
    sumi += int(line)
    #products = products * int(line)
    products *= int(line)
# Closing the file
print("sum = ", sumi)
print("product = ", products)
file.close()