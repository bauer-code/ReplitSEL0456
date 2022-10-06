print("Hello World 2")

print("Hello World 2")

a = 1
b = 2
c = 2
d = 4


def f(a,b, v = 3, z = 4):
  global d
  c = a + b + d + v + z
  return c
  


print(f(2, 3, z = 2))

print(f"a={a} b={b}")
#comment