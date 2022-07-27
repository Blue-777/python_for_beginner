myStr = 'python is fun. I only study python everyday. :)'
strPosList = []
index = 0

while True:
    try:
        index = myStr.index('python', index)
        strPosList.append(index)
        index = index + 1   # 다음 위치부터 찾음
    except:
        break

print('python letter position -->', strPosList)