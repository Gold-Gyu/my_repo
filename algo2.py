T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())

    if A < B:
        print("#%d <" %tc)
    elif A == B:
        print("#%d =" %tc)
    else:
        print("#%d >" %tc)  