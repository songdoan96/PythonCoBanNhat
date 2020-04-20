num = [1, 4, 7, 3, 9, 6, 1, 3, 5]
name = ["song", "doan", "quang"]
print(len(num))  # do dai cua list

# trich xuat mang con
print(num[:2])  # tu vi tri dau tien -> 2 phan tu
print(num[-3:])  # tu vi tri cuoi -> 3 phan tu

# xoa phan tu cua mang
del num[2]
print(num)

del num[3:5]  # xoa tu vi tri 3-5
print(num)

# noi mang
num1 = [91, 96, 91, 93, 95]
num2 = num + num1
print(num2)


# them phan tu vao cuoi mang
num1.append(99)
print(num1)

# lay phan tu cuoi cung cua mang
print(num1.pop())

# tim vi tri cua phan tu trong mang
print(num1.index(95))

# dao nguoc gia tri cua mang
num2.reverse()
print(num2)

# sap xep mang
num2.sort()  # mac dinh tang dan
print(num2)
num2.sort(reverse = True)  # mac dinh tang dan
print(num2)
