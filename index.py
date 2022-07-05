# This program prints Hello, world!

print('Hello, world!')

if 5>2:
    print("Five is gereter that two");
else:
    print("two is greater than 5");
    

a = "Hello, World!"
print(a[1])


import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

def my_function():
  print("Hello from a function")

my_function()

