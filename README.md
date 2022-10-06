# Algorithm-study

## How to

```
1. repository를 fork 후, clone합니다. (초기 1회만) 
2. fork한 repository 최신화 방법
 2-1. git remote add upstream https://github.com/Teecher-3rd-gen-study/Algorithm-study.git (초기 1회만)
 2-2. git remote -v ( 연결 확인 용도 )
 
 2-3. git fetch upstream ( 원본과 동기화 작업 )
 2-4. gir merge upstream/main ( 본인 레포에 적용 )
 
2. fork한 저장소의 각 주차에 해당되는 과제 폴더에 소스 코드를 commit 후 push 합니다. 
  파일명은 문제번호_이름으로 합니다. ex) 정길연_12311.py
  commit 메세지는 다음과 같이 합니다. **"[이름] 주차 문제번호 유형", des : 특이사항**
  유형 : 문제풀이미완, 문제풀이, 리뷰피드백
  ex)  [정길연] 1주차 12311번 리뷰피드백
    des : 변수 이름 변경 (000님의 리뷰 반영)

3. PR을 보낸 후, code review를 기다립니다. 
 PR 제목은 **"[이름] O주차 (0000번) 과제 제출"** 로 합니다. 
 일부 문제만 풀었을 경우 번호를 꼭 붙여줍시다. 
 ex) [정길연] 1주차 12311번 과제 제출, [정길연]1주차 과제 제출 
```
