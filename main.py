
def func_1():
  a = input("enter a string ")
  l = ""
  for i in range(len(a)):
    if i % 2 == 0:
      l += a[i].lower()
    else:
      l += a[i].upper()
  print(l)
func_1()
