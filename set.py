
print("--- set 생성 ---")
s = {1, 2, 3, 2, 3, 4}
print(s, type(s))


print("--- 기본연산 ---")
print(len(s))
print(2 in s)
print(2 not in s)


print("--- list의 중복성을 제거할 때 유용 ---")
nums = [1, 2, 3, 4, 2, 2, 5, 5]
s = set(nums)
print(s)
nums2 = list(s)
print(nums2)


print("--- 객체함수 ---")
s.add(8)
print(s)

s.discard(2)
print(s)

s.remove(3) # 없는 걸 제거하려고하면 에러
print(s)


s.update({0, 9})
print(s)

s.clear()
print(s)


print("--- 수학 집합 관련 함수 ---")
s1 = {1, 22, 33, 4, 5, 6, 7, 8, 9, 10}
s2 = {11, 22, 33}
s3 = s1.union(s2)
print(s3)
s4 = s1.intersection(s2)
print(s4)

s5 = s1.difference(s2)
print(s5)

s6 = s1.symmetric_difference(s2)
print(s6)

print(s1.issuperset(s4))
print(s5.issuperset(s1))
print(s2.issubset(s3)) # 부분집합이냐?
