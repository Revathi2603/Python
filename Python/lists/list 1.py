n1 = ['Python','Flask','Django','Tkinter']
n2=n1
n3=n1[:2]

n2[0] = 'Scipy'
n3[1] = 'Numpy'

s=10
for i in (n1, n2, n3):
    if i[0] == 'Python':
        s +=1
    if i[1] == 'Python':
        s += 2
print(s)