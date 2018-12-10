print("--- 논리연산 ---")
a = 20
b = 30
print(not a < b)
print(a < b and a!=b)
print(a == b or a!=b)

# 이미 a!=b가 true니까 뒤에 a>b는 계산 안함
print(a != b or a>b)

print("--- True=>1, False=>0 ---")
print(True + 2)

print("--- bool 캐스팅 ---")
print(bool(3), bool(2.14),
      bool([1,2,3,]), bool([]),
      bool({"a":100}), bool({}),
      bool(None), bool(0)
      )

print("--- 논리식의 연산 순서 ---")
print([] or 'hello') # 앞이 False라 뒷부분 수행
print('hello' or 'world') # 앞이 True라 앞부분만 수행
print('' or '^_^?')
print(None and 1)

s = 'hello world'
print(s or print(s))
print(s and print(s))

z =''
z and print(z)


