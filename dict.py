

print("--- 사전 생성 ---")
# key는 객체면 됨

d = {}       # 공사전
d = dict()   # 생성자 함수 호출

d = dict(one=1, two=2, three=3)   # 생성자 함수에 parameter쓸 수 있음
print(d)

d = dict([("one", 1), ("two", 2), ("three", 3)]) # 키와 값을 tuple로 싼 tuple list
print(d)

d = {"basketball":5, "baseball":9}
print(d, type(d))


print("--- 인덱싱대신 키로 접근해야한다 ---")
print(d["baseball"])
print(d["basketball"])


print("--- 연결(+)은 지원하지 않음 (squence형이 아님) ---")
# print(d + {"valleyball":6})
# print(d * 3)

print("--- mutable이다 ---")
d["valleyball"] = 6
print(d)
d["soccer"] = 100
print(d)
d["swimming"] = 4
print(d)


print("--- 길이(크기) ---")
print(len(d))


print("--- 확인 : 키로만 가능하다 ---")
print("soccer" in d)
print("asdf" in d)


print("--- 다양한 key 타입 ---")
d = {} # java script에서는 객체 하나 만든 거
print(d)
d[True] = "true"
d[10] = "100"
d["apple"] = 20
d[(1, 2, 3)] ="6"
print(d)

# 오류 : mutable 객체를 key로 사용했을 때
# d[[1, 2, 3]]          # [      [             리스트[]] 키에 접근하는[]]
# print(d)
# ===== TypeError: unhashable type: 'list'

print("--- keys()함수 ---")
keys = d.keys()
print(keys, type(keys))


for key in keys: # keys에서는 sequence타입이 와야 함!
    print(key, d[key], sep=" => ")


print("--- values() 함수 ---")
values = d.values()
for value in values:
    print(value)    # 값만 출력


print("--- items() 함수 ---")
items = d.items()
for item in items:
    print(item)
