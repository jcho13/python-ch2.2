print("--- 한 줄 문제열 정의 ---")
s = ''
str1 = 'hello world'
str2 = "hello world2"

print(type(s), type(str1), type(str2))

print("--- 여러 줄 문제열 정의 ---")
str3 ="""ㅎㅎ
여러줄
꺅
하하
하하하하하하
"""
print(str3)

print("--- 여러줄 주석? 아래같은 경우는 만들어졌다가 바로 사라질 것임 ---")
"""
주석1
주석2
주석3
"""
print("--- 개행(escape) ---")
print("hello\nworld")
print("a\nb \"하핳\"")

print("--- [문자열 연산] ---")
str1 ="First String"
str2 ="Second String"

print("--- 1. 인덱싱 ---")
print(str1[0], str1[1], str1[2])

print("--- 2. 슬라이싱 ---")
str3 = str2[2:5]
print(str3)
print(str2[2:])

print("--- 3. 연결(+) / +는 리터럴일때 생략 가능 ---")
print(str1 + " " + str2)
str3 = "AAAfff" " ^_^ " "33333"
print(str3)

print("--- 3. 주의 (1) 문자열 객체와 정수형 객체는 + 연결을 할 수 없다 ---")
name="쏠미"
age=20
# print(name + age)
print(name + str(age))

print("--- 4. 반복(*) ---")
print(str1*3 )

print("--- 5. len함수 ---")
print(len(str2))

print("--- 6. in, not in ---")
print("S" in str2) # 있냐
print("s" not in str2) # 없냐

print("--- 7. 문자열 객체는 변경할 수 없다(immutable) ---")
# str1[0] ="F"

print("--- 8. 서식(formating) : format() 함수 ---")
print("name: " + name + "age: " + format(age, "d"))

print("--- 9. 튜플을 이용한 서식 ---")
f="name: %s, age: %d"
print(f)
print(f % (name, age))
print("name: %s, age: %d" % (name, age))

print("--- cf) C 스타일 ---")
# printf("name: %s, age: %d", name, age)

print("--- 10. 서식 - 딕션너리를 이용한 포매팅 ---")
f ="name:%(n)s, age:%(a)d"
print(f)
print(f % {"n" : "듈리", "a" : 33})
print(f % {"n" : "마이콜", "a" : 20})


print("======================================")


print("--- 대소문자와 관련된 객체 함수 ---")
s = "I like Python, I like Chicken!"
print(s.upper())
print(s.lower())
print(s.swapcase()) # 대소문자 변경
print(s.capitalize()) # 문장 맨 앞만 대문자
print(s.title()) # 단어 맨 앞글자만 대문자


print("--- 검색 관련 객체 함수 ----")
s = "I like Python, I like Chicken!"
print(s.count("like"))
print(s.find("like", 5))
print(s.find("@")) # find는 없는 걸 찾을 때 -1
print(s.rfind("Chicken"))
print(s.index("Python"))
# print(s.index("@")) # index는 없는 걸 찾을 때 exception일으킴
print(s.rindex("like"))
print(s.startswith("I like "))
print(s.startswith("like", 2)) # 두 번째가 like로 시작하니
print(s.endswith("Chicken!"))
print(s.endswith("like", 0, 26))


print("--- 편집과 치환 ----")
s = "   spam and ham    "
print("<" + s.strip() + ">") #앞, 뒤 공백 제거
print("<" + s.lstrip() + ">") #왼쪽 공백 제거 (반대: rstrip)

s = "<><abc><><defg><><>"
print(s.strip("<>")) # 양쪽에 있는 <, >만 없애줌 (abc><><defg)
s = "Hello Java"
print(s.replace("Java", "Python"))


print("--- 정렬 ----")
s = "King and Queen"
print("#######" + s.center(60) + "#######")
print(s.center(60, "#"))
print(s.ljust(60, "#")) # 왼쪽으로 정렬시키고 나머지에 #를 채움


print("--- 분리와 결합 ----")
s = "Spam And Ham" # 생략하면 space로 쪼갠다
token = s.split() # 자바는 배열에 담지만 파이썬은 투풀에다 담아서 줌
print(token)

token = s.split(" And ")
print(token)

s2 = "~~~".join(token)
print(s2)

s3 = "one:two:three:four:five"
print(s3.split(":"))
print(s3.split(":", 2))
print(s3.rsplit(":", 2))


print("--- 검색 관련 객체 함수 ----")
lines = """First line
second line
third line
fourth line"""
print(lines.split("\n"))
print(lines.splitlines())


print("--- 판별 ----")
print("1234".isdigit())
print("a3d2d".isdigit())
print("asdf".isalpha())
print("as33dd".isalpha())
print("asdf".islower())
print("ASDF".isupper())
print("   ".isspace())
print("\n\n".isspace())
print("\t".isspace())


print("--- 0 채우기 ----")
print("^^".zfill(5))
print("1234".zfill(5))


print("--- format str 객체 함수 ----")
f = "name:{}, age:{}"
print(f.format("둘리", 10))

print("name:{}, age:{}".format("둘리", 10))
print("name:{0}, age:{1}".format("둘리", 10))
print("name:{1}, age:{0}".format("둘리", 10)) # 순서 지정 가능

print("name:{name}, age:{age}".format({"age":10, "name":"둘리"}))



