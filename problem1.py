
T = int(input())

for tc in range(1, T+1):
    num_list = list(map(int,input().split()))

    ans = 0


    for num in num_list:
        if num % 2 == 1:
            ans = ans + num

    print(f"#{tc} {ans}")

