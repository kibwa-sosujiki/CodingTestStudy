import sys

N = int(sys.stdin.readline())
fruits = list(map(int, sys.stdin.readline().split()))

fruit_count = {} 
left = 0
max_length = 0

for right in range(N):
    fruit = fruits[right]
    
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1

    # 과일 종류가 2개 초과하면 왼쪽 포인터 이동
    while len(fruit_count) > 2:
        left_fruit = fruits[left]
        fruit_count[left_fruit] -= 1 #하나씩 줄여야하는 이유는 dic으로 한번에 빼면 순서를 고려하지 않은게 됨
        if fruit_count[left_fruit] == 0:
            del fruit_count[left_fruit]
        left += 1

    # 최대 길이 갱신
    max_length = max(max_length, right - left + 1)

print(max_length)
