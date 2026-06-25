# arithmetic operators
a = 10
b = 3

print(a + b)   
print(a - b)   
print(a * b)   
print(a / b)  
print(a // b)  
print(a % b)   
print(a ** b) 
# assignment operators
a = 10
b = 20

print(a == b) 
print(a != b)  
print(a > b)  
print(a < b) 
# logical operators
a = 10
b = 20

print(a < b and b > 15)  
print(a > b or b > 15)  
print(not(a > b)) 
# Bit-wise operators
a = 5      # 0101
b = 3      # 0011

print(a & b)   
print(a | b)   
print(a ^ b)   
print(a << 1)  
print(a >> 1) 
# membership operators
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)     
print("grapes" not in fruits) 
# identity operators
a = [1, 2]
b = a
c = [1, 2]

print(a is b)     
print(a is c)     
print(a == c)     
