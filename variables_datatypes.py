#Text types
var1="Hello, World!" #string

#Numeric types
var2=4 #integer
var3=3.5 #float
var4=complex(1, 2) #complex

#Sequence types
var5=[1, 2, 3] #list
var6=(1, 2, 3) #tuple
var7=range(5) #range

#Mapping type
var8={"name": "John", "age": 30} #dictionary

#Set types
var9={1, 2, 3} #set
var10=frozenset([1, 2, 3]) #frozenset

#Boolean type
var11=True #boolean

#Binary types
var12=bytes(5) #bytes
var13=bytearray(5) #bytearray
var14=memoryview(bytes(5)) #memoryview

#None type
var15=None #NoneType


#Printing the variables and their types
print("var1:", var1, "Type:", type(var1)) # Output: var1: Hello, World! Type: <class 'str'>
print("var2:", var2, "Type:", type(var2)) # Output: var2: 4 Type: <class 'int'>
print("var3:", var3, "Type:", type(var3)) # Output: var3: 3.5 Type: <class 'float'>
print("var4:", var4, "Type:", type(var4)) # Output: var4: (1+2j) Type: <class 'complex'>
print("var5:", var5, "Type:", type(var5)) # Output: var5: [1, 2, 3] Type: <class 'list'>
print("var6:", var6, "Type:", type(var6)) # Output: var6: (1, 2, 3) Type: <class 'tuple'>
print("var7:", var7, "Type:", type(var7)) # Output: var7: range(0, 5) Type: <class 'range'>
print("var8:", var8, "Type:", type(var8)) # Output: var8: {'name': 'John', 'age': 30} Type: <class 'dict'>
print("var9:", var9, "Type:", type(var9)) # Output: var9: {1, 2, 3} Type: <class 'set'>
print("var10:", var10, "Type:", type(var10)) # Output: var10: frozenset({1, 2, 3}) Type: <class 'frozenset'>
print("var11:", var11, "Type:", type(var11)) # Output: var11: True Type: <class 'bool'>
print("var12:", var12, "Type:", type(var12)) # Output: var12: b'\x00\x00\x00\x00\x00' Type: <class 'bytes'>
print("var13:", var13, "Type:", type(var13)) # Output: var13: bytearray(b'\x00\x00\x00\x00\x00') Type: <class 'bytearray'>
print("var14:", var14, "Type:", type(var14)) # Output: var14: <memory at 0x7f8b8c0c8d00> Type: <class 'memoryview'>
print("var15:", var15, "Type:", type(var15)) # Output: var15: None Type: <class 'NoneType'>