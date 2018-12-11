
print("--- packing은 tuple로만 가능 ---")
t = 10, 20, 30, 'apple'
print(t, type(t))


print("--- unpacking ---")
a, b, c, s = t
print(a, b, c, s)
# 오류 - 패킹되어있는 객체가 더 많은 경우
# a, b, c = t


print("--- unpacking extends ---")
t = (1,2,3,4,5)

# a에는 하나만 담고 나머지를 b에 list로 담음
a, *b = t
print(a, b)

# b,c에는 하나만 담고 나머지를 a에 list로 담음
*a, b, c = t
print(a, b, c)

a, *b, c = t
print(a, b, c)
