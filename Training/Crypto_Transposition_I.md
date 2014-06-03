# Crypto - Transposition I 

It seems that the simple substitution ciphers are too easy for you.
From my own experience I can tell that [transposition ciphers] are more difficult to attack.
However, in this training challenge you should have not much problems to reveal the plaintext.

oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wm lsacemloah.p

```python

code = 'oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wm lsacemloah.p'

''.join(code[i+1] + code[i] for i in range(0,len(code),2))

```

The answer is :  

Wonderful. You can read the message way better when the letters are in correct order. I think you would like to see your password now: mslcameolhap.
