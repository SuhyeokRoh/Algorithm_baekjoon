import sys

number1 = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
num_dict = {number: 0 for number in num}
# 가지고 있는 숫자 카드를 dictionary의 key로 설정
# for문을 사용해 iterable 객체 안에 요소가 있는지 확인할 때,
# dict가 더 빠르기 때문에

number2 = int(sys.stdin.readline())
compare_num = list(map(int,sys.stdin.readline().split()))

result = []

for number in compare_num:
    if number in num_dict.keys():
        result.append(1)
    else:
        result.append(0)

for n in result:
    print(n, end=' ')