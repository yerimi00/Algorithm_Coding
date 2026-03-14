# [Bronze V] 문자열 - 9086 

[문제 링크](https://www.acmicpc.net/problem/9086) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

구현, 문자열

### 제출 일자

2026년 3월 15일 01:53:47

### 문제 설명

<p>문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다. 각 테스트 케이스는 한 줄에 하나의 문자열이 주어진다. 문자열은 알파벳 A~Z 대문자로 이루어지며 알파벳 사이에 공백은 없으며 문자열의 길이는 1000보다 작다.</p>

### 출력 

 <p>각 테스트 케이스에 대해서 주어진 문자열의 첫 글자와 마지막 글자를 연속하여 출력한다.</p>


### sudo 코드

```
n 숫자
for i in range(n):
    str = input()
    print(str 슬라이스 첫글자)
    print(str 슬라이스 마지막 글자)

```

### 내가 쓴 코드와 틀린 이유

```
# n = int(input())


# for i in range(n):
#     str[i] = input()

# for i in range(n):
#     print(str[i][0]+""+str[i][-1])

n = int(input())
arr = []

for i in range(n):
    arr.append(input())

for i in range(n):
    print(arr[i][0]+""+arr[i][-1])

```
- str이 뭔지
  str은 파이썬 내장 함수(문자열 변환 함수)
  원래 이렇게 쓴다:
    ```
    str(123)  # → "123"
    ```
    그래서 str[i] = ... 처럼 인덱싱하면 내장 함수를 덮어쓰려는 거라 에러가 난다.

- 왜 append를 써야 하는지
  arr = []는 빈 리스트. 빈 리스트에 arr[0], arr[1] 처럼 인덱스로 바로 접근하면 존재하지 않는 칸이라 에러가 난다.

   ```
   arr = []
   arr[0] = "hello"  # ❌ IndexError
   ```

  append는 리스트 끝에 새 항목을 추가하는 함수라 빈 리스트에도 쓸 수 있다:
  ```
   arr = []
   arr.append("hello")  # ✅ arr = ["hello"]
   arr.append("world")  # ✅ arr = ["hello", "world"]
  ```
