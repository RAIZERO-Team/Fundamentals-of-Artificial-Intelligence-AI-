# Function


## Basic Input/Output

### Example: Asking for User Input and Printing a Response

```python
name = input('What is your name?')  # Prompts user for input in Arabic
print(f'Welcome to Python {name}')  # Outputs a message with the user's input

```

## Function Definitions and Calls

### Function Definition

```python
def greeting():
    name = input('What is your name?')
    print(f'Welcome to Python {name}')

```

### Function Call

```python
greeting()  # Calls the greeting function to execute its code

```

## Passing Arguments

### Passing Single Argument

```python
def greeting(username):
    """This function takes a username as an argument and greets them."""
    print(f'Welcome to Python Mr. {username.title()}!')

```

### Call

```python
greeting('ahmed')  # Calls greeting with 'ahmed' as an argument
# Output: Welcome to Python Mr. Ahmed!
```

```python

greeting?? # Output: 

"""

Signature: greeting(username)
Source:   
def greeting(username):
    "This function takes a username as an argument and greets them."
    print(f'Welcome to Python Mr. {username.title()}!')
File:      c:\users\ahmed\appdata\local\temp\ipykernel_12880\3975449673.py
Type:      function

"""

```

### Passing Multiple Arguments

```python
def pets(owner_name, pet_name):
    print(f'Hi {owner_name.title()} please take care of {pet_name.title()}!')

```

### Calls

```python
pets('ahmed', 'Sultan')  # Calls pets with 'ahmed' and 'Sultan' as arguments
# Output: Hi Ahmed please take care of Sultan!

pets('sultan', 'ahMed')  # Calls pets with 'sultan' and 'ahMed' as arguments
# Output: Hi Sultan please take care of Ahmed!

```

## Keyword Arguments and Default Values

### Keyword Arguments

```python
pets(pet_name='sultan', owner_name='ahmed')  # Uses keyword arguments to call the pets function
# Output: Hi Ahmed please take care of Sultan!

```

### Default Values

```python
def pets(owner_name, pet_name='sultan'):
    """This function has a default value for pet_name."""
    print(f'Hi {owner_name.title()} please take care of {pet_name.title()}!')

```

### Call

```python
pets('ahmed')  # Calls pets with 'ahmed' as the only argument
# Output: Hi Ahmed please take care of Sultan!

```

## Return Values

### Function with Return Value

```python
def pets(owner_name='ahmed', pet_name='sultan'):
    """This function returns a message string instead of printing it."""
    advice = f'Hi {owner_name.title()} please take care of {pet_name.title()}!'
    return advice

```

### Call

```python
advice = pets()  # Calls pets and stores the return value in 'advice'
print(advice)  # Prints the returned advice
# Output: Hi Ahmed please take care of Sultan!

print(type(advice))  # Prints the type of the return value
# Output: <class 'str'>

```

## Optional Arguments

### Function with Optional Arguments

```python
def fullname(fname='x', mname='y', lname='z'):
    """This function prints the full name with optional middle name."""
    return f'Your full name is: {fname.title()} {mname.title()} {lname.title()}-'

```

### Calls

```python
print(fullname('magnus', 'michal', 'carlsen'))  # Calls fullname with all arguments
# Output: Your full name is: Magnus michal Carlsen-

print(fullname('magnus'))  # Calls fullname with only the first name
# Output: Your full name is: Magnus Y Z-

```

### Optional Arguments Must Be Last

```python
def fullname(fname, lname, mname=''):
    """This function handles an optional middle name parameter."""
    if mname:
        fname = f'Your full name is: {fname.title()} {mname.title()} {lname.title()}-'
    else:
        fname = f'Your full name is: {fname.title()} {lname.title()}-'
    return fname

```

### Calls

```python
print(fullname('magnus', 'michal', 'carlsen'))  # Calls fullname with all arguments
# Output: Your full name is: Magnus michal Carlsen-

print(fullname('magnus', 'carlsen'))  # Calls fullname without the middle name
# Output: Your full name is: Magnus Carlsen-

```

### Docstrings

```python
def fullname(fname, lname, mname=''):
    """prints out a fullname for a given triplet firstname, middlename and last name
    with an optional parameter 'middlename'"""
    if mname:
        fname = f'Your full name is: {fname.title()} {mname.title()} {lname.title()}-'
    else:
        fname = f'Your full name is: {fname.title()} {lname.title()}-'
    return fname

```

## Arbitrary Argument Lists

### Function with Arbitrary Arguments

```python
def average(*args):
    """This function calculates the average of all its arguments."""
    return sum(args) / len(args)

```

### Call

```python
print(average(1, 2, 3, 4, 5, 56, 878, 23))  # Calls average with multiple arguments
# Output: 121.5

```

## Local Scope vs Global Scope

### Local Scope

```python
x = 10  # Global variable
 
def access_global():
    """This function accesses a global variable."""
    print('x printed from access_global:', x)

access_global()  # Calls the function to print the global variable
# Output: x printed from access_global: 10

```

### Modifying Global Variable

```python
def try_to_modify_global():
    """This function tries to modify a global variable locally."""
    x = 3.5  # Local variable
    print('x printed from try_to_modify_global:', x)

try_to_modify_global()  # Calls the function
# Output: x printed from try_to_modify_global: 3.5

print(x)  # Prints the global variable to show it hasn't changed
# Output: 10

def modify_global():
    """This function modifies a global variable using the global keyword."""
    global x
    x = 'hello'
    print('x printed from modify_global:', x)

modify_global()  # Calls the function to modify the global variable
# Output: x printed from modify_global: hello

print(x)  # Prints the modified global variable
# Output: hello

```

## Immutable Objects

### Example with Immutable Objects

```python
def cube(number):
    """This function prints the id of the number before and after modification."""
    print('id(number) before modifying number:', id(number))
    number **= 3
    print('id(number) after modifying number:', id(number))
    return number

```

### Call

```python
print(cube(13))  # Calls the cube function
# Output:
# id(number) before modifying number: 140716967968048
# id(number) after modifying number:  140716968048016
# 2197

```

## Lambda Expressions

### Basic Lambda Expression

```python
f = lambda x: x ** 2  # Lambda expression to square a number
print(f(2))  # Prints the square of 2
# Output: 4

```

### Lambda with Multiple Arguments

```python
f = lambda x, y: 3 * (x ** 2) + 2 * y - 5  # Lambda expression with multiple arguments
print(f(2, 3))  # Prints the result of the expression
# Output: 11

```

### Sorting with Lambda

```python
the_greats = ['machael jackson', 'ahmed sami', 'magdi shatta', 'alireza firouzja', 'marwan pablo']
the_greats.sort()  # Sorts the list alphabetically
for name in the_greats:
    print(name.split(' ')[0])  # Prints the first name of each person
# Output:
# ahmed
# alireza
# macahel
# magdi
# marwan

```

### Lambda as Return Value

```python
def myfunc(n):
    """This function returns a lambda function that multiplies its argument by n."""
    return lambda a: a * n

mydoubler = myfunc(2)  # Creates a lambda function that doubles its input
print(mydoubler(11))  # Prints the result of doubling 11
# Output: 22

```


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


## Exception Handling in Python

### 1. Basic Input Handling

### Code Block 1

```python
value = int(input("Enter your number: "))  # Input is int
print(value, "success")

```

**Expected Output**:

- Input: `5`
- Output: `5 success`

### Code Block 2

```python
value = int(input("Enter your number: "))  # Input is str
print(value, "success")

```

**Expected Output**:

- Input: `abc`
- Output: Raises a `ValueError`

### 2. Try-Except Block

### Code Block 3

```python
try:
    value = int(input("Enter your number: "))  # Input is str
    print(value, "success")
# This code won't run without an except block

```

### 3. Default Exception Handling

### Code Block 4

```python
try:
    value = int(input("Enter your number: "))  # Input is str
    print(value, "success")
except:  # Default handling
    print("invalid input")

```

**Expected Output**:

- Input: `abc`
- Output: `invalid input`

### 4. Uncaught Exception

### Code Block 5

```python
result = 10 / 0
try:
    value = int(input("Enter your number: "))
    print(value, "success")
except:
    print("invalid input")

```

**Expected Output**:

- Raises a `ZeroDivisionError` before the input prompt.

### 5. Misleading Output due to Unhandled Exception

### Code Block 6

```python
try:
    result = 10 / 0
    value = int(input("Enter your number: "))
    print(value, "success")
except:
    print("invalid input")
# Output is misleading because the exception occurs before input

```

**Expected Output**:

- Output: `invalid input` (This is misleading because the exception was due to division by zero)

### 6. Specific Exception Handling

### Code Block 7

```python
try:
    result = 10 / 0
    value = int(input("Enter your number: "))
    print(value, "success")
except ZeroDivisionError:  # Specific exception
    print("you cannot divide by zero")

```

**Expected Output**:

- Output: `you cannot divide by zero`

### 7. Multiple Exception Handling

### Code Block 8

```python
try:
    value = int(input("Enter your number: "))  # Input is str
    print(value, "success")
    result = 10 / 0
except ZeroDivisionError:
    print("you cannot divide by zero")

```

**Expected Output**:

- Input: `abc`
- Raises a `ValueError` which is not caught.

### Code Block 9

```python
try:
    value = int(input("Enter your number: "))  # Input is str
    print(value, "success")
    result = 10 / 0
except ZeroDivisionError:
    print("you cannot divide by zero")
except:  # Default except
    print("invalid input")
# In Python, multiple except blocks are allowed
# The default except must be the last one

```

**Expected Output**:

- Input: `abc`
- Output: `invalid input`
- Input: `5`
- Output: `you cannot divide by zero`

### 8. Using Named Exceptions

### Code Block 10

```python
try:
    value = int(input("Enter your number: "))  # Input is str
    print(value, "success")
    result = 10 / 0
except ZeroDivisionError as err:
    print(err)
    print("you cannot divide by zero")
except ValueError as err2:
    print(err2)
    print("invalid input")

```

**Expected Output**:

- Input: `abc`
- Output: `invalid input`
- Input: `5`
- Output: `division by zero\\n you cannot divide by zero`

### 9. Raising Exceptions

### Code Block 11

```python
x = -10
if x < 0:
    raise Exception(f"The number {x} is less than zero")
    print("This will not print because the error")
else:
    print(f"{x} is a good number and ok")
print('Print message after if condition')

```

**Expected Output**:

- Output: `Exception: The number -10 is less than zero`

### Code Block 12

```python
y = "ahmed"
if type(y) != int:
    raise ValueError("Only numbers allowed")
    # raise Exception("Only numbers allowed") can write this
print('Print message after if condition')

```

**Expected Output**:

- Output: `ValueError: Only numbers allowed`

### 10. Try-Except-Else-Finally

### Code Block 13

```python
try:
    number = int(input("Write your age: "))
    print("Good, this is an integer from try")
except:
    print("Bad, this is not an integer")
else:
    print("Good, this is an integer from else")
finally:
    print("Print from finally whatever happens")

```

**Expected Output**:

- Input: `25`
- Output:
    - `Good, this is an integer from try`
    - `Good, this is an integer from else`
    - `Print from finally whatever happens`
- Input: `abc`
- Output:
    - `Bad, this is not an integer`
    - `Print from finally whatever happens`

### 11. Multiple Specific Exceptions

### Code Block 14

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Can't divide")
except NameError:
    print("Identifier not found")
except ValueError:
    print("Value error Elzero")
except:
    print("Error happens")

```

**Expected Output**:

- Output: `Can't divide`

### Code Block 15

```python
try:
    print(x)
except ZeroDivisionError:
    print("Can't divide")
except NameError:
    print("Identifier not found")
except ValueError:
    print("Value error Elzero")
except:
    print("Error happens")

```

**Expected Output**:

- Output: `Identifier not found`

### Code Block 16

```python
try:
    print(int("Hello"))
except ZeroDivisionError:
    print("Can't divide")
except NameError:
    print("Identifier not found")
except ValueError:
    print("Value error Elzero")
except:
    print("Error happens")

```

**Expected Output**:

- Output: `Value error Elzero`

### 12. Advanced Example with File Handling

### Code Block 17

```python
the_file = None
the_tries = 5

while the_tries > 0:
    try:  # Try to open the file
        print("Enter the file name with absolute path to open")
        print(f"You have {the_tries} tries left")
        print("Example: D:\\\\Python\\\\Files\\\\yourfile.extension")
        file_name_and_path = input("File Name => : ").strip()
        the_file = open(file_name_and_path, 'r')
        print(the_file.read())
        break
    except FileNotFoundError:
        print("File not found. Please be sure the name is valid")
        the_tries -= 1
    except:
        print("Error happened")
    finally:
        if the_file is not None:
            the_file.close()
            print("File closed.")
else:
    print("All tries are done")

```

**Expected Output**:

- If the file is not found after 5 tries, it will print "All tries are done".
- If the file is found, it will print the file contents and "File closed." when the loop breaks.

---

### Common Built-in Exceptions

1. **`ArithmeticError`**
    - **Description**: Base class for all errors that occur for numeric calculations.
    - **Examples**: `ZeroDivisionError`, `OverflowError`, `FloatingPointError`.
2. **`ZeroDivisionError`**
    - **Description**: Raised when the second argument of a division or modulo operation is zero.
    - **Example**:
        
        ```python
        try:
            result = 10 / 0
        except ZeroDivisionError as e:
            print(e)  # Output: division by zero
        
        ```
        
3. **`ValueError`**
    - **Description**: Raised when a function receives an argument of the correct type but inappropriate value.
    - **Example**:
        
        ```python
        try:
            number = int("abc")
        except ValueError as e:
            print(e)  # Output: invalid literal for int() with base 10: 'abc'
        
        ```
        
4. **`TypeError`**
    - **Description**: Raised when an operation or function is applied to an object of inappropriate type.
    - **Example**:
        
        ```python
        try:
            result = "2" + 2
        except TypeError as e:
            print(e)  # Output: can only concatenate str (not "int") to str
        
        ```
        
5. **`IndexError`**
    - **Description**: Raised when a sequence subscript is out of range.
    - **Example**:
        
        ```python
        try:
            lst = [1, 2, 3]
            print(lst[5])
        except IndexError as e:
            print(e)  # Output: list index out of range
        
        ```
        
6. **`KeyError`**
    - **Description**: Raised when a dictionary key is not found in the set of existing keys.
    - **Example**:
        
        ```python
        try:
            d = {"a": 1}
            print(d["b"])
        except KeyError as e:
            print(e)  # Output: 'b'
        
        ```
        
7. **`FileNotFoundError`**
    - **Description**: Raised when an operation like `open()` cannot find the specified file.
    - **Example**:
        
        ```python
        try:
            f = open("nonexistentfile.txt", "r")
        except FileNotFoundError as e:
            print(e)  # Output: [Errno 2] No such file or directory: 'nonexistentfile.txt'
        
        ```
        
8. **`OSError`**
    - **Description**: Raised when a system function returns a system-related error, including I/O failures.
    - **Example**:
        
        ```python
        try:
            f = open("/etc/passwd", "w")
        except OSError as e:
            print(e)  # Output: [Errno 13] Permission denied: '/etc/passwd'
        
        ```
        
9. **`ImportError`**
    - **Description**: Raised when the `import` statement has trouble trying to load a module.
    - **Example**:
        
        ```python
        try:
            import non_existent_module
        except ImportError as e:
            print(e)  # Output: No module named 'non_existent_module'
        
        ```
        
10. **`AttributeError`**
    - **Description**: Raised when an attribute reference or assignment fails.
    - **Example**:
        
        ```python
        try:
            class MyClass:
                pass
            obj = MyClass()
            print(obj.attribute)
        except AttributeError as e:
            print(e)  # Output: 'MyClass' object has no attribute 'attribute'
        
        ```
        
11. **`NameError`**
    - **Description**: Raised when a local or global name is not found.
    - **Example**:
        
        ```python
        try:
            print(non_existent_variable)
        except NameError as e:
            print(e)  # Output: name 'non_existent_variable' is not defined
        
        ```
        
12. **`MemoryError`**
    - **Description**: Raised when an operation runs out of memory.
    - **Example**:
        
        ```python
        try:
            lst = [1] * (10**10)
        except MemoryError as e:
            print(e)  # Output: MemoryError
        
        ```
        
13. **`RuntimeError`**
    - **Description**: Raised when an error is detected that doesn’t fall in any of the other categories.
    - **Example**:
        
        ```python
        def recursive_call():
            return recursive_call()
        try:
            recursive_call()
        except RuntimeError as e:
            print(e)  # Output: maximum recursion depth exceeded in comparison
        
        ```
        
14. **`StopIteration`**
    - **Description**: Raised by the `next()` function to indicate that there are no further items produced by the iterator.
    - **Example**:
        
        ```python
        try:
            it = iter([1, 2, 3])
            while True:
                print(next(it))
        except StopIteration:
            print("End of iteration")
        
        ```
        

### Handling Each Exception

- **ZeroDivisionError**: Handle divisions, ensure the divisor is not zero.
- **ValueError**: Validate and sanitize user inputs.
- **TypeError**: Ensure type compatibility before performing operations.
- **IndexError**: Validate index bounds before accessing lists.
- **KeyError**: Check dictionary keys' existence before accessing.
- **FileNotFoundError**: Ensure file paths are correct and files exist before opening.
- **OSError**: Handle permissions and OS-level errors.
- **ImportError**: Check module availability and installation.
- **AttributeError**: Ensure object attributes exist before accessing.
- **NameError**: Ensure variables are defined before using.
- **MemoryError**: Manage memory usage efficiently.
- **RuntimeError**: Use for catching general runtime errors not covered by specific exceptions.
- **StopIteration**: Handle the end of iterations graceful


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>




# file manipulation


Certainly! Here is an expanded version of the README with more detailed explanations:

---

# Understanding Absolute and Relative Paths in File Systems

The difference between absolute and relative paths is crucial in understanding how to navigate file systems and manage files in programming. This document provides a detailed explanation of these concepts, along with practical Python code examples for handling files.

## Absolute Path

An absolute path is a complete path that specifies the location of a file or directory from the root directory of the file system. It includes all the directories from the root to the target file or directory.

### Key Characteristics:

1. **Starts from the Root:** The path starts from the root directory (`/` in Unix/Linux, `C:\\` in Windows).
2. **Always Unique:** It uniquely identifies a file or directory regardless of the current working directory.
3. **Examples:**
    - Unix/Linux: `/home/user/documents/report.txt`
    - Windows: `C:\\Users\\User\\Documents\\report.txt`

An absolute path is useful when you need to ensure that a specific file or directory is accessed regardless of where the command is executed.

## Relative Path

A relative path specifies the location of a file or directory relative to the current working directory. It does not start from the root directory.

### Key Characteristics:

1. **Starts from the Current Directory:** The path is relative to the directory you are currently working in.
2. **Can Vary:** The same relative path can point to different locations depending on the current working directory.
3. **Examples:**
    - If the current working directory is `/home/user`, then `documents/report.txt` is a relative path to `/home/user/documents/report.txt`.
    - If the current working directory is `C:\\Users\\User`, then `Documents\\report.txt` is a relative path to `C:\\Users\\User\\Documents\\report.txt`.

A relative path is useful for making code or commands more portable within a project. It allows you to specify file locations in a way that is independent of the root directory structure.

## Differences

1. **Starting Point:**
    - **Absolute Path:** Starts from the root directory.
    - **Relative Path:** Starts from the current working directory.
2. **Usage:**
    - **Absolute Path:** Used when you need to specify a path that works regardless of the current working directory.
    - **Relative Path:** Used when you want to specify a path relative to the current working context.
3. **Portability:**
    - **Absolute Path:** Less portable because it depends on the exact file system structure.
    - **Relative Path:** More portable within a given project or script, as long as the relative structure remains consistent.

## Example Code

### Working with File Paths in Python

The following Python code demonstrates how to work with absolute and relative paths using the `os` module.

```python
import os

FILE = open('F:\\\\F.Python\\\\OOP\\\\Ma7er.txt')

# Get current working directory
print(os.getcwd())
print("*" * 50)

# Get the absolute path of the current script
print(os.path.abspath(__file__))
print("*" * 50)

# Print the current working directory
print(os.getcwd())
print("*" * 50)

# Get the directory for the opened file
print(os.path.dirname(os.path.abspath(__file__)))
print("*" * 50)

# Change current working directory to the directory of the file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

```

**Expected Output:**

```
C:\\Users\\User\\Projects
**************************************************
C:\\Users\\User\\Projects\\script.py
**************************************************
C:\\Users\\User\\Projects
**************************************************
C:\\Users\\User\\Projects
**************************************************

```

### File Handling Modes in Python

File handling in Python is done using various modes that specify the purpose of opening a file. Here are the most common modes:

- `"a"` Append: Open file for appending values, create the file if it does not exist.
- `"r"` Read (default): Open file for reading, error if the file does not exist.
- `"w"` Write: Open file for writing, create the file if it does not exist.
- `"x"` Create: Create a file, error if the file already exists.

```python
FILE = open('F:\\\\F.Python\\\\OOP\\\\Ma7er.txt')
FILE = open(r'F:\\\\F.Python\\\\OOP\\\\Ma7er.txt')

```

### Reading Files in Python

The following code demonstrates various ways to read a file in Python:

```python
myFile = open("F:\\\\F.Python\\\\OOP\\\\Ma7er.txt", "r")

print(myFile)  # File data object
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)

# Read the entire content of the file
print(myFile.read())

# Read the first 5 characters of the file
print(myFile.read(5))

# Read lines from the file
print(myFile.readline(5))  # Read first 5 characters of the line
print(myFile.readline())   # Read the rest of the line
print(myFile.readline())   # Read the next line

# Read all lines into a list
print(myFile.readlines())
print(myFile.readlines(50))  # Read lines into a list with a size hint
print(type(myFile.readlines()))

# Read file line by line using a loop
for line in myFile:
    print(line)
    if line.startswith("07"):
        break

# Close the file
myFile.close()

```

**Expected Output:**

```
<_io.TextIOWrapper name='F:\\\\F.Python\\\\OOP\\\\Ma7er.txt' mode='r' encoding='cp1252'>
F:\\F.Python\\OOP\\Ma7er.txt
r
cp1252
(Content of the file)
(Content of the file truncated to first 5 characters)
(Content of the file read line by line)

```

### Using `with` for File Operations

Using `with` for file operations ensures that the file is properly closed after its suite finishes, even if an exception is raised.

### Reading Files

```python
input_file = 'F:\\\\F.Python\\\\OOP\\\\Ma7er.txt'

# Read the entire content of the file
try:
    with open(input_file, 'r') as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Read the first line of the file
try:
    with open(input_file, 'r') as file:
        content = file.readline(7)
        content = file.readline()
        print(content)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Read all lines into a list
try:
    with open(input_file, 'r') as file:
        content = file.readlines()
        print(content)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

```

**Expected Output:**

```
(Content of the file)
(First line after reading 7 characters and then reading the line)
['Line 1\\n', 'Line 2\\n', 'Line 3\\n', 'Line 4\\n', 'Line 5\\n']

```

### Writing to Files

```python
# Write to file (overwrite)
try:
    with open(input_file, 'w') as file:
        file.write("\\nthis is a new line")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# Append to file
try:
    with open(input_file, 'a') as file:
        file.write("\\nyooooooooooooooou")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# Write a list of strings to file
myList = ["\\Ahmed\\n", "Maher\\n", "ali\\n"]

try:
    with open(input_file, 'a') as file:
        file.writelines(myList)
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

```

**Expected Output:**

```
File content after writing:
this is a new line
yooooooooooooooou
Ahmed
Maher
ali

```

### Seeking in Files

Seeking allows you to move the file pointer to a specific location in the file. This can be useful for random access to file content.

```python
# Create a sample file with some content
with open(input_file, 'w') as file:
    file.write("Line 1\\nLine 2\\nLine 3\\nLine 4\\nLine 5\\n")

# Open the file for reading
with open(input_file, 'r') as file:
    # Read the first line
    line = file.readline()
    print(f"First line: {line.strip()}")

    # Get the current position of the file pointer
    position = file.tell()
    print(f"Current position: {position}")

    # Move the file pointer to the beginning of the file
    file.seek(0)
    print("Moved to the beginning of the file")

    # Read the first line again
    line = file.readline()
    print(f"First line: {line.strip()}")

    # Move the file pointer to the third line (assume each line is 7 bytes including newline)
    file.seek(16)  # 2 lines * 7 bytes/line
    print("Moved to the third line")

    # Read the third line
    line = file.readline()
    print(f"Third line: {line.strip()}")

    # Move the file pointer to the end of the file
    file.seek(0, 2)
    print("

Moved to the end of the file")

    # Get the current position of the file pointer
    position = file.tell()
    print(f"Current position at the end: {position}")

```

**Expected Output:**

```
First line: Line 1
Current position: 7
Moved to the beginning of the file
First line: Line 1
Moved to the third line
Third line: Line 3
Moved to the end of the file
Current position at the end: 35

```

```python
# Create a sample file with content
with open(input_file, 'w') as file:
    file.write("Hello, World!\\nThis is a test file.\\nIt contains multiple lines.\\n")

# Open the file for reading
with open(input_file, 'r') as file:
    # Move to the 7th byte (0-based index)
    file.seek(7)
    print("After seeking to the 7th byte:")
    print(file.read())

    # Move to the beginning of the file
    file.seek(0)
    print("\\nAfter seeking to the beginning of the file:")
    print(file.read())

    # Move to the 14th byte (beginning of the second line)
    file.seek(14)
    print("\\nAfter seeking to the 14th byte:")
    print(file.read())

    # Move to the end of the file
    file.seek(0, 2)
    print("\\nAfter seeking to the end of the file:")
    position = file.tell()
    print(f"Position at the end: {position}")

```

**Expected Output:**

```
After seeking to the 7th byte:
World!
This is a test file.
It contains multiple lines.

After seeking to the beginning of the file:
Hello, World!
This is a test file.
It contains multiple lines.

After seeking to the 14th byte:
This is a test file.
It contains multiple lines.

After seeking to the end of the file:
Position at the end: 54

```

---

