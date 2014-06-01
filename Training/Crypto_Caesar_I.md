# Crypto - Caesar I
As on most challenge sites, there are some beginner cryptos, and often you get started with the good old caesar cipher.
I welcome you to the WeChall style of these training challenges :)

Enjoy!

JXU GKYSA RHEMD VEN ZKCFI ELUH JXU BQPO TEW EV SQUIQH QDT OEKH KDYGKU IEBKJYED YI XSTSWWYHREQY

## Solutin

```python
code = 'JXU GKYSA RHEMD VEN ZKCFI ELUH JXU BQPO TEW EV SQUIQH QDT OEKH KDYGKU IEBKJYED YI XSTSWWYHREQY' 
for i in range(1,26):
	''.join(' ' if x == ' ' else chr((ord(x) - ord('A') + 1 + i) % 26 + ord('A')) for x in code)

```

The answer is :
THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG OF CAESAR AND YOUR UNIQUE SOLUTION IS HCDCGGIRBOAI
