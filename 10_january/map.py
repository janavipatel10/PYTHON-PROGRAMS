#map() used

def map_fun(a):
	return a*a

a = [2, 3, 4, 5]
x = list(map(map_fun, a))
print(x)

