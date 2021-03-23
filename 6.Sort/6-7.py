# p.176 sorted 소스코드
# sorted()는 퀵 정렬과 동작 방식이 비슷한 병합 정령을 기반으로 만들어짐
# 병합 정렬은 일반적으로 퀵 정렬보다 느리지만 최악의 경우에도 시간 복잡도 (NlogN)을 보장한다는 특징이 있다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

