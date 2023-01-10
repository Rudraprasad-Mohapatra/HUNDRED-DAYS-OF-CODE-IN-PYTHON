#Importing in python is the process of loading code from python module into the current script
# import pandas
# pandas.read_csv()

"""
import math
print(math.floor(4.3234))
print(math.sqrt(9)) """

# "from" Keyword
'''Let we want to import only one function from entire module so we have to use from keyword '''
"""
from math import sqrt,pi
result=sqrt(9)

print(result,result*pi) #output 3.0 9.42477796076938 """

# from math import * #we are importing everything from math module,This not use generally Because of arrise of confusion 

# "as" keyword
"""
from math import sqrt as S
result=S(9.9)
print(result) """

"""dir function"""
# It is used to print all the function and all things inside a module
import math
print(dir(math)) #First import the module in script and then use dir(module_name) for the response 
"""
Output will be:-

['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 
'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

"""
print(math.nan,type(math.nan))

# We can import a variables as well as functions from a python file present in our folder to another file. 
"""
# Go to the file name "import_Explanation44_1" for next understanding of import
#Here import_Explanation44_1 is the name of the file "import_Explanation44_1.py" present in the folder

from import_Explanation44_1 import welcome,harry #or we can write " from import_Explanation44_1 import * "for imporing all. Here welcome() is the function and harry is a variable inside the file name as  "import_Explanation44_1.py"
welcome()
print(harry) """

import import_Explanation44_1 as imp
imp.welcome()
print(imp.harry)

