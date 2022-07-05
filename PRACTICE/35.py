pairs = [[2, 1], [-2, -1]]
new_pairs = map(lambda p: sorted(p), pairs) # map: sort 각자 // lambda: 하나씩 꺼내 담아주는 역할 (매개 변수: 표현식) // sorted: [][] 봐꿈 // map(sorted): []안 내부 요소 변경
print(list(new_pairs)[0][0])
# ap(sorted)만 있기 때문에 []대갈호 안에 요소들만 봐꿔줌. 고로 [1,2][-2,-1]이므로 [0][0] = 1이 된다
