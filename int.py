# 2진, 8진, 10진, 16진 Literal (값을 표현하는 문자?!)
a = 23
print(type(a))

b = 0b1101
o = 0o23
h = 0x23

print(b, o, h)

# 3.x버전에서는 int와 long이 합쳐졌다 => 표현범위 무한대
# 자승? power?
print("---자승?---")
e = 2**1024
print(e, type(e))
print(e.bit_length())

# 변환함수
print("---변환함수---")
print(oct(38))
print(hex(38))
print(bin(38))
