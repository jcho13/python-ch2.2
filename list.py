
print("--- list 생성----")
l1 = []
l1 = [1,2,'python']

print("--- indexing ----")
print(l1[-3], l1[-2], l1[-1], l1[0], l1[1], l1[2])


print("--- slicing ----")
print(l1[1:2])
print(l1[1:])
print(l1[:])
print(l1[len(l1)-1:])
print(l1[len(l1)::-1]) # list를 역순으로 뒤집기


print("--- 반복(*) ----")
l2 = l1 * 3
print(l2)


print("--- 연결(+) ----")
l3 = l1 + [9, 9, 9]
print(l3)


print("--- 길이 ----")
print(len(l3))



print("--- 확인 ----")
print(5 in l3)



print("--- 삭제 ----")
del l3[0]
print(l3)


print("--- 변경가능한 시퀀스 자료형 ----")
a = ["apple", "banana", 100, "orange"]
a[2] = a[2] + 20
print(a)


print("--- 슬라이싱을 통한 치환 ----")
a = [1, 12, 123, 1234, 12345]
a[0:3] = [5, 55]
print(a)

a[0:2] = [10]
print(a)

a[1:2] = [20] # a[1] = 20
print(a)

a[1:3] = [20, 30]
print(a)


print("--- 슬라이싱을 통한 삭제 ----")
a = [1, 12, 123, 1234, 12345]
a[1:2] = []
print(a)
a[0:] = []
print(a)


print("--- 슬라이싱을 통한 삽입 ----")
a = [1, 12, 123, 1234, 12345]


print("--- 중간 삽입 ----")
a[1:1] = ['a']
print(a)


print("--- 여러개 삽입 ----")
a[2:2] = ['b', 'c']
print(a)


print("--- 마지막에 삽입 ----")
a[8:] = ['z']
print(a)


print("--- 처음에 삽입 ----")
a[:0] = [0]
print(a)



print("--- list 객체함수를 통한 삽입 ----")
a = [1,3,4]
a.insert(1, 2) # 1자리에 2삽입
print(a)

a.append(5) # 맨 뒤에 삽입
print(a)

a.insert(0, 0)
print(a)


print("--- reverse 메소드 ----")
a.reverse()
print(a)


print("--- 값 제거 ----")
a.remove(4) # 4라는 그 값 자체가 제거됨
print(a)


print("--- 스택으로 사용하기 ----")
stack = []
stack.append(10) # 맨 밑에 깔림
stack.append(20)
stack.append(30) # 맨 위에 깔림
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

print("--- 큐로 사용하기 ----")
qu = [1,2]
qu.append(3)
qu.append(4)
qu.append(5)
qu.append(6)
print(qu)
print(qu.pop())
print(qu.pop())


print("--- sort() : list객체함수 : 내장된 소팅 알고리즘 ----")
l4 = [1,30,4,54,3,5,7,8,2]
l4.sort()
print(l4)

l4.sort(reverse=True)
print(l4)

l5=[99,2,33,24,5,68,21,7,83]
l5.sort(key=str) # string으로 보고 정렬
print(l5)
l5.sort(key=int) # int로 보고 정렬
print(l5)


print("--- 내장 전역 함수 : sorted ----")
l6 = [12,34,21,456,68,7,9]
print(sorted(l6))

l6 = [12,34,21,456,68,7,9]
print(sorted(l6, reverse=True))


########## key함수를 만들어 전달할 수 있다 ###########


def f(i):
    return i % 10


l9 = sorted(l6, key=f, reverse=False)
print(l9)

