def sum(num_list, n):
    tempSum = 0 # 대입 연산

    for num in num_list: # num_list의 수 (n번 만큼 반복)
        tempSum += num # 사칙 연산
    
    return tempSum

print(sum([1,2,3,4,5], 5))
