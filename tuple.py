print("--- 튜플 생성 ---")
t = () # 빈 튜플
print(t, type(t))

t = (1, 2, 3, 4, 5, 6) # 항목이 하나일 때는 반드시 콤마 (1, )
t1 = (1, 2, 3)
print(t1, type(t1))

# -----------------------------
# sequence: str, list, tuple
# mutable : list, set, dic
# -----------------------------


print("--- <sequence형 연산> ---")
print("--- 1. 인덱싱 ---")
print(t[-3], t[-2], t[-1], t[0], t[1], t[2])

print("--- 2. 슬라이싱 ---")
print(t[1:3])
print(t[:])

print("--- 3. 반복 (*) ---")
t2 = t*3
print(t2)


print("--- 4. 연결 (+) ---")
t3 = t + (7,8,9)
print(t3)


print("--- 5. 길이 ---")
print(len(t3))



print("--- 6. 확인 ---")
print(5 in t3)


print("--- 7. tuple은 변경불가능 (immutable)한 스퀸스형이다 ---")
# t = ('apple', 'banana', 10, 20)
# t[2] = t[2] + 90
# print(t)


print("--- 8. 튜플을 이용해서 좌우변 여러개의 값을 대입(치환) 가능 ---")
x, y, z = 1, 2, 3
print(x, y, z)


print("--- 9. swap도 가능 ---")
x, y = 10, 20
print(x, y)
x, y = y, x;
print(x, y)


print("--- 10. 객체 함수 : list에 비해 많지가 않다 (immutable이기 때문) ---")
t = (20, 30, 10, 20)
print(t.index(20))
print(t.count(20))


print("--- 11. 변환: list, tuple, set은 서로서로 변환 가능---")
t = (1, 2, 3, 3)
print(t, type(t))

s = set(t)
print(s, type(s)) # 중복 사라지면서 set으로 변환

l = list(t)
print(l, type(l)) # 3 유지하면서 list로 변환

t = tuple(l)
print(t, type(t))


