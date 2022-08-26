x, y, z = 1, 2, 4

def z_plus():
    global z
    z += 1
    return z

x += y if not y else z
if False and x == z_plus():
    y -= 1
elif x == z_plus():
    y -= 2
elif y == 0 or y == 2:
    y -= 3
else:
    y = 4

print("x = " + str(x))
print("y = " + str(y))
print("z = " + str(z))