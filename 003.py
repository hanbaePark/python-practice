'''num =  input(int("숫자를 입력하세요"))

if num % 2 == 1:
    print("홀수입니다")
else:
    print("짝수입니다")
    
a =  int(input("미세먼지 수치를 이야기해주세요"))

if a>151:
    print("매우안좋음")
elif a>=81 and a<=150:
    print("나쁨입니다")
elif a>=30 and a<=80:
    print("보통입니다")
else:
    print("좋아요!")
'''
a = []
b = []
for i in range(1,11):
    if i % 2 == 1:
        a.append(i)
    else:
        b.append(i)
print(a)
print(b)
    
