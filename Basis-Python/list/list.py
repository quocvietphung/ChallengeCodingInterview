xs = [3, 1, 2]
print(xs, xs[2])
print(xs[-1])
xs[2] = 'foo'
print(xs) # Prints "[3, 1, 'foo']"
xs.append('bar')
print(xs) # Prints "[3, 1, 'foo', 'bar']"
x = xs.pop()
print(x, xs) # Prints "bar [3, 1, 'foo']"