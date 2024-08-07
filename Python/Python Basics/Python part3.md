

# Python Containers Documentation

## Table of Contents
1. [Lists](#lists)
   - [List Methods](#list-methods)
2. [Tuples](#tuples)
3. [Dictionaries](#dictionaries)
   - [Dictionary Methods](#dictionary-methods)
4. [Sets](#sets)
   - [Set Methods](#set-methods)
5. [Specialized Containers from `collections`](#specialized-containers-from-collections)
   - [`namedtuple`](#namedtuple)
   - [`deque`](#deque)
   - [`Counter`](#counter)
   - [`OrderedDict`](#ordereddict)
   - [`defaultdict`](#defaultdict)

---

## Lists
Lists are ordered, mutable collections of items. They can hold elements of any data type, and elements can be accessed using their index.

## Advantages and Disadvantages

### Advantages
- **Dynamic Size**: Lists can grow and shrink as needed, providing flexibility in size management.
- **Versatile**: Capable of storing elements of various data types within the same list.
- **Built-in Methods**: Equipped with many methods for easy manipulation, including sorting, appending, and removing elements.

### Disadvantages
- **Slower Performance**: For large datasets, lists can be slower compared to arrays due to overhead from dynamic resizing.
- **Memory Consumption**: Lists use more memory because they are dynamically resized, which can lead to increased memory usage.

## Applications
- **Storing Collections of Data**: Ideal for collections where the order of elements is important, such as lists of items or tasks.
- **Implementing Stacks and Queues**: Useful for implementing data structures like stacks and queues, where you need to add and remove items.
- **Operations**: Allows for various operations such as sorting, slicing, and appending, making it versatile for different use cases.


### List Methods
- **`append(item)`**: Adds `item` to the end of the list.
- **`extend(iterable)`**: Extends the list by appending elements from the `iterable`.
- **`insert(index, item)`**: Inserts `item` at the specified `index`.
- **`remove(item)`**: Removes the first occurrence of `item`.
- **`pop([index])`**: Removes and returns the item at `index` (default is the last item).
- **`clear()`**: Removes all items from the list.
- **`index(item, [start], [end])`**: Returns the index of the first occurrence of `item`.
- **`count(item)`**: Returns the count of `item` in the list.
- **`sort(key=None, reverse=False)`**: Sorts the list in ascending order.
- **`reverse()`**: Reverses the elements of the list.
- **`copy()`**: Returns a shallow copy of the list.

### Example
    # python
    my_list = [1, 2, 3, 4]
    my_list.append(5)          # [1, 2, 3, 4, 5]
    my_list.extend([6, 7])     # [1, 2, 3, 4, 5, 6, 7]
    my_list.insert(1, 1.5)     # [1, 1.5, 2, 3, 4, 5, 6, 7]
    my_list.remove(1.5)        # [1, 2, 3, 4, 5, 6, 7]
    popped_item = my_list.pop() # 7
    my_list.clear()            # []


## Tuples
Tuples are ordered, immutable collections of items. Once a tuple is created, its elements cannot be changed. Tuples can hold elements of any data type and are defined using parentheses.
## Advantages and Disadvantages

## Advantages

- **Immutable**: Once created, the data within a tuple cannot be altered, which helps ensure data integrity.
- **Faster Access**: Accessing elements in a tuple is generally faster than in a list, making tuples more efficient for read operations.
- **Dictionary Keys**: Tuples can be used as keys in dictionaries due to their immutability, unlike lists which are not hashable.

## Disadvantages

- **Non-modifiable**: You cannot change, add, or remove elements after a tuple is created. This can be limiting if you need to alter the data.
- **Limited Methods**: Tuples have fewer built-in methods for manipulation compared to lists, which can limit their flexibility in some cases.

## Applications

- **Storing Related Data**: Useful for grouping related pieces of data together. For example, coordinates or function return values.
- **Returning Multiple Values**: Ideal for returning multiple values from a function, as tuples can hold multiple items.
- **Dictionary Keys**: Can be used as keys in dictionaries when you need a composite key that remains constant.

### Example
    # python
    my_tuple = (1, 2, 3, 4)
    first_element = my_tuple[0]  # 1
    # Tuples are immutable, so you can't modify them directly
    # my_tuple[0] = 10  # This will raise an error
    

## Dictionaries
Dictionaries are unordered collections of key-value pairs. Keys must be unique and immutable, while values can be of any data type. Dictionaries are defined using curly braces.

## Advantages and Disadvantages

### Advantages
- **Fast Lookups and Inserts**: Dictionaries provide average O(1) time complexity for lookups and insertions, making them efficient for these operations.
- **Keys of Any Immutable Type**: Allows for a wide range of key types, including strings, numbers, and tuples.
- **Flexible and Dynamic**: Can dynamically grow and adapt as needed, and values can be of any type.

### Disadvantages
- **Unordered Before Python 3.7**: Dictionaries did not maintain insertion order before Python 3.7. Since Python 3.7, dictionaries preserve the insertion order.
- **Higher Memory Usage**: Generally consume more memory compared to lists and tuples due to the overhead of maintaining hash tables.

## Applications
- **Storing Data as Key-Value Pairs**: Useful for cases where data needs to be accessed via unique keys, such as user profiles or configuration settings.
- **Implementing Mappings and Caches**: Ideal for creating mappings from keys to values and for implementing caching mechanisms.
- **Building JSON-like Data Structures**: Often used to construct and manipulate data structures similar to JSON, which are commonly used in web APIs and data interchange.

### Dictionary Methods
- **`keys()`**: Returns a view object of the dictionary's keys.
- **`values()`**: Returns a view object of the dictionary's values.
- **`items()`**: Returns a view object of the dictionary's key-value pairs.
- **`get(key, [default])`**: Returns the value for `key` if `key` is in the dictionary, else `default`.
- **`pop(key, [default])`**: Removes and returns the value for `key` if `key` is in the dictionary, else `default`.
- **`popitem()`**: Removes and returns an arbitrary (key, value) pair from the dictionary.
- **`clear()`**: Removes all items from the dictionary.
- **`update([other])`**: Updates the dictionary with the key-value pairs from `other`, overwriting existing keys.

### Example
    # python
    my_dict = {'key1': 'value1', 'key2': 'value2'}
    my_dict['key3'] = 'value3'  # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    value = my_dict.get('key1') # 'value1'
    my_dict.pop('key2')         # {'key1': 'value1', 'key3': 'value3'}
    my_dict.clear()             # {}


## Sets
Sets are unordered collections of unique items. They are commonly used for membership testing, removing duplicates, and mathematical operations like union, intersection, difference, and symmetric difference. Sets are defined using curly braces.

## Advantages and Disadvantages

### Advantages
- **Fast Membership Testing**: Provides average O(1) time complexity for membership tests, making it quick to check if an item is present.
- **Automatically Removes Duplicates**: Ensures that all elements are unique, automatically removing duplicates when elements are added.
- **Supports Mathematical Operations**: Provides built-in support for set operations such as union, intersection, and difference.

### Disadvantages
- **Unordered**: Does not maintain any specific order of elements, which can be limiting if order matters.
- **Cannot Store Mutable Objects**: Elements must be immutable; therefore, mutable objects like lists cannot be stored within a set.

## Applications
- **Removing Duplicates from a List**: Useful for creating a collection of unique elements from a list with possible duplicates.
- **Membership Testing**: Efficiently checks for the presence of an item in a collection.
- **Performing Set Operations**: Ideal for operations like union, intersection, and difference, which are commonly needed in mathematical and data analysis tasks.

### Set Methods
- **`add(item)`**: Adds `item` to the set.
- **`remove(item)`**: Removes `item` from the set. Raises `KeyError` if `item` is not found.
- **`discard(item)`**: Removes `item` from the set if it is present.
- **`pop()`**: Removes and returns an arbitrary element from the set.
- **`clear()`**: Removes all elements from the set.
- **`union(*others)`**: Returns a new set with elements from the set and all `others`.
- **`intersection(*others)`**: Returns a new set with elements common to the set and all `others`.
- **`difference(*others)`**: Returns a new set with elements in the set that are not in the `others`.
- **`symmetric_difference(other)`**: Returns a new set with elements in either the set or `other` but not both.
- **`issubset(other)`**: Returns `True` if the set is a subset of `other`.
- **`issuperset(other)`**: Returns `True` if the set is a superset of `other`.
- **`isdisjoint(other)`**: Returns `True` if the set has no elements in common with `other`.

### Example
    # python
    my_set = {1, 2, 3, 4}
    my_set.add(5)            # {1, 2, 3, 4, 5}
    my_set.remove(3)         # {1, 2, 4, 5}
    union_set = my_set.union({6, 7})  # {1, 2, 4, 5, 6, 7}
    

## Specialized Containers from `collections`
The `collections` module provides additional container data types that are optimized for specific use cases.

### `namedtuple`
Factory function for creating tuple subclasses with named fields. Namedtuples are like regular tuples but with named fields, making them more readable and self-documenting.

### Example
    #python
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x)  # 1
    print(p.y)  # 2


### `deque`
List-like container with fast appends and pops on both ends. Deques are optimized for operations on both ends of the container and are useful for implementing queues and stacks.

### Example
    # python
    from collections import deque
    d = deque([1, 2, 3])
    d.append(4)          # deque([1, 2, 3, 4])
    d.appendleft(0)      # deque([0, 1, 2, 3, 4])
    d.pop()              # 4
    d.popleft()          # 0
    

### `Counter`
Dictionary subclass for counting hashable objects. Counters are useful for tallying or counting objects and come with various convenient methods for common operations.

### Example
    #python
    from collections import Counter
    c = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
    print(c)  # Counter({'a': 3, 'b': 2, 'c': 1})


### `OrderedDict`
Dictionary that remembers the order of insertion. OrderedDicts are useful when the order of items is important and should be preserved.

### Example
    # python
    from collections import OrderedDict
    od = OrderedDict()
    od['a'] = 1
    od['b'] = 2
    od['c'] = 3
    print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])
   

### `defaultdict`
Dictionary that provides default values for missing keys. defaultdicts are useful when you want to ensure that accessing a missing key returns a default value instead of raising a `KeyError`.

### Example
    # python
    from collections import defaultdict
    dd = defaultdict(int)
    dd['a'] += 1
    print(dd)  # defaultdict(<class 'int'>, {'a': 1})
    
--- 

# Comparison of Data Structures in Python

| Feature                | Lists                           | Tuples                          | Dictionaries                    | Sets                             |
|------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|
| **Order**              | Ordered                          | Ordered                          | Unordered (Python 3.7+)          | Unordered                        |
| **Mutability**         | Mutable                          | Immutable                        | Mutable                          | Mutable                          |
| **Duplicates**         | Allows duplicates                | Allows duplicates                | Keys must be unique              | No duplicates allowed            |
| **Indexing**           | Indexed by integers               | Indexed by integers               | Not indexed                       | Not indexed                       |
| **Element Type**       | Can be mixed types                | Can be mixed types                | Keys must be immutable            | Can be mixed types                |
| **Performance**        | Slower for large datasets        | Faster for access and iteration   | Fast lookups and inserts         | Fast membership testing          |
| **Memory Usage**       | Higher due to dynamic resizing    | Lower due to fixed size          | Higher due to hash table overhead | Higher due to hash table overhead |
| **Built-in Methods**   | Many for manipulation            | Few for manipulation              | Many for key-value manipulation  | Few for manipulation             |
| **Applications**       | Collections where order matters  | Storing fixed collections        | Storing key-value pairs          | Removing duplicates, set operations |



