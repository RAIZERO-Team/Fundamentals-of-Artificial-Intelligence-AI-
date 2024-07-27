# Conditions
  * ### if Condition
  * ### Nested  if Condition
  ___
# First : if Condition
##  **<u>Identification</u>**
###### The if statement is used for conditional execution of code. It allows the program to execute certain blocks of code based on whether a condition is true or false.
_____

* ## Basic Syntax
 ```python
       if Condition(Boolean) 
            // code to execute if condition is true
```
___

### note:
##### <u>Condition(Boolean)</u>This condition must be boolean execute certain blocks of code based on whether a condition is true or false.
____
```python
num = 20
if num == 10: # -----> This is Condition  
    print("x is Equal than 5") # ----> This is code to execute if condition is true
```
___
### note:
In the rule of IF, distances are necessary.
```python
num=3
if num==3:
    print("yes")
print("None")    
## output 
## yes
## none
Becouse the Condition is True  
```
```python
num=5
if num==3:
    print("yes")
print("None")    
## output None
Becouse the Condition is false 
```

____
####  Comparison Operators To Use It In Condition(Boolean) 

*      ==: Equal to
*      !=: Not equal to
*      <: Less than
*      <=: Less than or equal to
*      >: Greater than
*      >=: Greater than or equal to
## Example 
```python
x = 10
if x == 10:
    print("x is equal to 10")
if x != 5:
    print("x is not equal to 5")
if x < 15:
    print("x is less than 15")
if x <= 10:
    print("x is less than or equal to 10")
if x > 5:
    print("x is greater than 5")
if x >= 10:
    print("x is greater than or equal to 10")
```
____
# else: 
#### The else statement can be used to execute a block of code if the if condition is false
___
#### Basic Syntax
```python
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
```
#### Example 
```python
x = 5
if x == 5:
    print("x is Equal than 5")
else:
    print("x is not Equal than 5")
## output ->> x is Equal than 5
## Becose the condition if is True
```
```python
x = 10
if x == 5:
    print("x is Equal than 5")
else:
    print("x is not Equal than 5")
## output ->> x is not Equal than 5
## Becose the condition if is False
```
____
# else if :
##### The elif (short for else if) statement allows you to check multiple conditions sequentially.
_____
#### Basic Syntax
```python
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
elif condition3:
    # code to execute if condition2 is true
elif condition4
    # code to execute if condition2 is true    
else:
    # code to execute if none of the above conditions are true
```
### Example 
```python
x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
# output ->> x is equal to 5 
# Becose the condition if is False
```
```python
x = 3
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
# output ->> x is equal to 5 
# Becose the condition if and else if are False
```
____
#  Second: Nested if Statements
##  **<u>Identification</u>**
###### You can nest if statements inside other if statements to check multiple conditions.
___
###### Basic Syntax
```python
if condition1:## ->> must this condition1 is True to execute the  nest if
    if condition2:
        # code to execute if both condition1 and condition2 are true
```
###### Example 
```python
num =int(input("Please Enter The Number Want To Check : "))
if num>0:
    if num % 2 == 0:
        print("This number is positive and Enen")
    else:
          print("This number is positive and Odd")
elif num<0:
       if num % 2 == 0:
          print("This number is negative and Enen")  
       else:
             print("This number is negative and Odd")
else:
     print("Neither even nor odd")
```
__________
# Logical Operators
##### You can use logical operators (and, or, not) to combine multiple conditions
____
######  Basic Syntax
```python
if condition1 and condition2:
    # code to execute if both condition1 and condition2 are true
if condition1 or condition2:
    # code to execute if either condition1 or condition2 is true
if not condition:
    # code to execute if condition is false
```
###### Example
```python
x = 10
y = 5
if x > 5 and y < 10:
    print("x is greater than 5 and y is less than 10")
if x > 15 or y < 10:
    print("x is greater than 15 or y is less than 10")
if not x == 5:
    print("x is not equal to 5")
```
______________________________
# General examples

###### Example1
```python
num1,num2,num3  = map(int,input().split())

if num1 >= num2 and num1 >= num3:
    if num2 > num3:
        print(num3, num1)
    else:
        print(num2, num1)
elif num2 >= num1 and num2 >= num3:
    if num1 > num3:
        print(num3, num2)
    else:
        print(num1, num2)
elif num3 >= num2 and num3 >= num1:
    if num1 > num2:
        print(num2, num3)
    else:
        print(num1, num3)
```
###### Example2
```python
a, s, b = input().split()
a = int(a)
b = int(b)

if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
else:
    print(a / b)
```
______
# Exercises
| Problems || Link Problems
|-----------|-|-------------
| The Brothers||https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/L   
| Capital or Small or Digit||https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/M     
| Sort Numbers ||https://codeforces.com/group/MWSDmqGsZm/contest/219158/problem/T          
_________
_________
# LOOPS
* FOR LOOP
* INSTED LOOP
* WHILE LOOP
* INFINTIE LOOP
____
# First For Loop
##  **<u>Identification</u>**
###### A for loop iterates over a sequence (like a list, tuple, string, or range). The loop continues until all items in the sequence have been processed. 
_____ 
#####  Basic Syntax
```python
for variable in sequence:
    # code block to be executed
```
###### Example
```python
for i in range(5):
    print(i)
# output 
# 0
# 1
# 2
# 3
# 4
```
___
## break and continue

* #  break
##### Terminates the loop prematurely when a specific condition is met.
###### Example
```python
for i in range(10):
    if i == 5:
        break
    print(i)
# output
# 0
# 1
# 2
# 3
# 4
```
* #  continue
##### Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
###### Example
```python
for i in range(10):
    if i == 5:
        continue
    print(i)
# output
# 0
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
```
_____
# Nested Loops
##  **<u>Identification</u>**
###### You can also nest loops, which means having a loop inside another loop.
#####  Basic Syntax
_____
```python
for variable in sequence:
    for variable in sequence:
    # code block to be executed
```
###### Example
```python
for i in range(3):
    for j in range(3):
        print("i = ",i ,"  ", "j =" , j)
# output
# i =  0    j = 0
# i =  0    j = 1
# i =  0    j = 2
# i =  1    j = 0
# i =  1    j = 1
# i =  1    j = 2
# i =  2    j = 0
# i =  2    j = 1
# i =  2    j = 2        
```
_______
# while Loop
##  **<u>Identification</u>**
###### A while loop repeatedly executes the code block as long as the condition is true. Once the condition becomes false, the loop stops.
___
#####  Basic Syntax
```python
# intilization
while condition:
    # code block to be executed
    #incemen
```
###### Example
```python
i = 0
while i < 5:
    print(i)
    i += 1
# output
# 0
# 1
# 2
# 3
# 4
```
___
# Infinite Loops 
```python
while True:
    for i in range(5):
        print(i)

```
______
# # General examples 
```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
# output 
# apple
# banana
# cherry   
```
```python
person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(key , value)
#output 
# name John
# age 30
# city New York
```
```python
n = int(input("Enter the number of elements: "))

e = 0  
o = 0 
pos = 0  
neg = 0 
for i in range(n):
    x = int(input("Enter a number: "))
    if x % 2 == 0:
        e += 1
    else:
        o += 1
    
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
print("Even:", e)
print("Odd:", o)
print("Positive:", pos)
print("Negative:", neg)
# output
# Even: 2
# Odd: 2
# Positive: 4
# Negative: 0
```
# Exercises
| Problems || Link Problems
|-----------|-|-------------
| 1 to N||https://codeforces.com/group/MWSDmqGsZm/contest/219432/my   
| Fixed Password||https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/D     
|  Palindrome ||https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/I   

