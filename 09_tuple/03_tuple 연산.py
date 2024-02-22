# 복수개 자료 치환

(a, b), (c, d) = (1, 2), (10, 11)
print(a,b,c,d)

# 패킹(packing)
t = 1,2,'hello'
print(t)

# 언패킹(unpacking)
x,y,z = t
print(x,y,z,type(x),type(y),type(z))

t2 = 1,2,3,4,5
a, *b, c= t2   #*b = 나머지 요소를 집합으로
print(a,b,c, type(a),type(b),type(c))
