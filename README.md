# MathParse
Parse strings as Mathematical expressions in Python  
A much safer alternative to parsing using the `eval()` method which is a security concern.

## Installation
MathParse is available in the Python Package Repository  
 ```
 >> pip install mathparse
 
 import mathparse
 mathparse.evaluate('1+2*(6+9/3)*4')
  >> 73
 ```
 __MathParse might not always be correct with negative numbers yet__
