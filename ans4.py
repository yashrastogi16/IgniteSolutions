a=1
b=2
c = 0
print a
print b
while(c < 4000000):
  c = a + b
  if(c < 4000000):
    print c, " "
  a = b
  b = c
