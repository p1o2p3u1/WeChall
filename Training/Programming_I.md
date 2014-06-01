# Programming 1

When you visit [this link](http://www.wechall.net/challenge/training/programming1/index.php?action=request) you receive a message.

Submit the same message back to http://www.wechall.net/challenge/training/programming1/index.php?answer=the_message

Your timelimit is 1.337 seconds

## Solution

```python
import urllib2;

request = urllib2.Request('http://www.wechall.net/challenge/training/programming1/index.php?action=request');

request.add_header('Cookie','WC=7326764-10727-GO6vlEtF1gaDd9dS');

response = urllib2.urlopen(request);

message = response.read();

request = urllib2.Request('http://www.wechall.net/challenge/training/programming1/index.php?answer=%s' % message);

request.add_header('Cookie','WC=7326764-10727-GO6vlEtF1gaDd9dS');

response = urllib2.urlopen(request);

print response.read();

```

