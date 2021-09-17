from random import randint

s = 0
v = [0]*100
for i in range (100):
    v[i] = randint(100,999)
    s = s + v[i]

m = s/100
ab = ig = ac = 0
for i in range (100):
    if v[i] < m:
        ab += 1
    elif v[i] > m:
        ac += 1
    else:
        ig += 1
    
print (ab, ig, ac)
print(v)
print("soma= ",s)
print("media= ", m)
