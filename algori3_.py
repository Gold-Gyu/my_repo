T = int(input())

for tc in range(1, T+1):

    listA_ = list(map(int, input().split()))
    

    average = sum(listA_)/len(listA_)
    average = round(average)

    print(f"#{tc} {average}")
        

