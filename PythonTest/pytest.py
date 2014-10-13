# -*- coding: cp949 -*-
from urllib.request import urlopen

# Print first four lines of this site.
i = 0
for line in urlopen("http://www.daum.net"):
    # Decode.
    line = line.decode()

    # Print.
    print(i, line, end="")

    # See if past limit.
    if i == 5:
        break
    i += 1


from urllib.parse import urlparse

# Parse this url.
result = urlparse("http://www.daum.net/")

# Get some values from the ParseResult.
scheme = result.scheme
loc = result.netloc
path = result.path

# Print our values.
print(scheme)
print(loc)
print(path)










s = "ȫ�浿1;ȫ�浿2;ȫ�浿3;ȫ�浿4;ȫ�浿5;ȫ�浿6;ȫ�浿7;ȫ�浿8;ȫ�浿9;ȫ�浿"
# s = "man1;man2;man3;man4;man5;man6;man7;man8;man9;man"

# Separate on semicolon.
# ... Split from the right, only split three.
cities = s.rsplit(";", 3)

# Loop and print.
for city in cities:
    print(city)




import time

# Input data.
s = "This is a split performance test"

print(s.split())
print(s.split(" "))

# Time 1
print(time.time())

# Default version.
i = 0
while i < 1000000:
    words = s.split()
    i += 1

# Time 2
print(time.time())

# Explicit space version.
i = 0
while i < 1000000:
    words = s.split(" ")
    i += 1

# Time 3
print(time.time())
