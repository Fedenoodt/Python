"""a = open('a.txt', 'a')
a.write("Don't trust anybody")
a.close()

b = open('a.txt', 'r')
print(b.read())"""

def control():
    r = open('list.txt', 'r')
    print(r.read())
    r.close()

a = open('list.txt', 'a')
a.write('lista = [a, b, c, d, e, f]')
a.close()

control()

