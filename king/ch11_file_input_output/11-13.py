myStr = 'ython everyday. :)'
strPosList = []
index = 0

# print(myStr.index('python', 29))

while True:
    index = myStr.index('python', index)
    print(index)
    strPosList.append(index)
    index = index + 1   # 다음 위치부터 찾음
    # print(index)
    
print('python letter position -->', strPosList)

# valueError가 나는 이유는 0번째와 28번째 python이 나온 이후로 더 이상 python이 없어서 