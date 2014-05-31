# ASCII 
In a computer, you can only work with numbers.
In this challenge you have to decode the following message, which is in ASCII.

84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 108, 112, 101, 115, 108, 99, 110, 104, 100, 102, 110, 114

## Solutin

```python
code = '84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 108, 112, 101, 115, 108, 99, 110, 104, 100, 102, 110, 114'
''.join(chr(int(x)) for x in code.split(',')

```
