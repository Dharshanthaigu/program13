def odd_num_integer(a,b):
  for i in range(a+1,b):
    if(i%2!=0):
      print(i)
d,c=input().split()
d=int(d)
c=int(c)
odd_num_integer(d,c)
