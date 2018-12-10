# 복소수 = 실수부 + 허수부
# 허수부 j, J를 숫자 뒤에 붙힌다

a = 4 + 5j
print(a, type(a))
print(isinstance(a, complex))

b = 7 - 2j
print(a+b)

# complex 형 변환
p = 2.5
q = -3
print(complex(p, q))
