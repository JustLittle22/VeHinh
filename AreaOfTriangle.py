import math

a = int(input("Nhập vào cạnh a:"))
b = int(input("Nhập vào cạnh b:"))
c = int(input("Nhập vào cạnh c:"))

# Nửa chu vi hình tam giác
cv = (a+b+c)/2

#Diện tích hình tam giác
S = math.sqrt(cv*(cv-a)*(cv-b)*(cv-c))

#Đáp án
print("Diện tích hình tam giác là:", S)