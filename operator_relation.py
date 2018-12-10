print("---객체의 대소비교---")
print(4 <= 5)
print(4 == 5)
print(4 >= 5)
print(4 != 5)

print("---복합관계식---")
a = 6
# print(0<a && a <3) 불가능
print(0 < a and a < 3)
print(0 < a < 3)

print("---수치형 이외의 다른 타입의 객체 비교---")
print("abcd" > "abc")
print("abcd" > "abd")
print((1,2,3) < (1,2,6))
print([1,2,3] < [1,2,6])

print("---동질성 비교(==) : 안에 내용 비교 / 동일성 비교(is) : 같은 객체냐---")
a=10
b=20
c=a
print(a == b)
print(a is b)
print(a == c)
print(a is c)
