# for - else 문
```
while 1:
    for i in range(1, V + 1):
        # 다음에 갈 지점을 찾고, 방문하지 않은 곳에 닿으면
        if arr[start][i] == 1 and visited[i] == 0:
            # 스택에 쌓음
            stack.append(start)
            # 다음 위치로 옮김
            start = i
            # 방문 표시
            visited[start] = 1
            break

    # 다음에 갈 지점 못찾거나 방문한 정점이면
    else:
        # stack이 길이가 존재할때
        if len(stack) != 0:
            # pop
            start = stack.pop()
        # 스택이 없으면 다 돈거니까 탈출~
        else:
            break
# 방문 리스트 리턴
return visited
```

- 반복문 안에 있을때, for문에서 break로 나오지 못한 경우가 else로 가서 돈다. break로 나온 경우는 수행하지 않음. 
- -> 이중 반복문일때 잘 쓰일테니 기억해둘것