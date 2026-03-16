# [Silver III] 두 수의 합 - 3273 

[문제 링크](https://www.acmicpc.net/problem/3273) 

### 성능 요약

메모리: 42660 KB, 시간: 80 ms

### 분류

정렬, 두 포인터

### 제출 일자

2026년 3월 16일 23:20:45

### 문제 설명

<p>n개의 서로 다른 양의 정수 a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>으로 이루어진 수열이 있다. a<sub>i</sub>의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 자연수 x가 주어졌을 때, a<sub>i</sub> + a<sub>j</sub> = x (1 ≤ i < j ≤ n)을 만족하는 (a<sub>i</sub>, a<sub>j</sub>)쌍의 수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수열의 크기 n이 주어진다. 다음 줄에는 수열에 포함되는 수가 주어진다. 셋째 줄에는 x가 주어진다. (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)</p>

### 출력 

 <p>문제의 조건을 만족하는 쌍의 개수를 출력한다.</p>

### sudo 코드 - 생각 1

```
S = 갯수 입력
A 리스트 입력
x 숫자 입력
L = A[i]-x 들 리스트

for i in A:
    #A[i]-x 리스트에 A[i] 숫자가 있는지 체크
```

### sudo 코드 - 생각 2 : 시간 복잡도 줄이는 버전

```
n 입력
A 리스트 입력
x 입력
A 정렬
count = 0
left = 0
right = n-1

while left < right:
    if A[left] + A[right] == x:
        count++
        left++
        right--
    elif A[left] + A[right] < x:
        left++
    else:
        right--

print(count)
```

-> 투 포인터 (O(n log n))

- 정렬 후 양 끝에서 포인터를 좁혀가며 탐색
- 합이 x면 count 증가, 양쪽 포인터 이동
- 합이 x보다 작으면 left를 오른쪽으로 (합을 키움)
- 합이 x보다 크면 right를 왼쪽으로 (합을 줄임)

생각 1 O(n²) vs 생각 2 O(n log n) (정렬) + O(n) (탐색)
