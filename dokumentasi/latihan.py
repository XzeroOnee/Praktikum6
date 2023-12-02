import math

a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args) / len(args)
d = lambda s: "".join(set(s))

#fungsi a 
print('-'*20)
result_a = a(5)
print(result_a)

#fungsi b
print('-'*20)
result_b = b(2, 5)
print(result_b)

#fungsi c
print('-'*20)
result_c = c(2,3,6,5,6)
print(result_c)

#fungsi d
print('-'*20)
result_d = d("hallo")
print(*result_d," ")