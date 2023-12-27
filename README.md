# 독서모임 모집 플랫폼 gluv

&nbsp;이스트소프트에서 주관하는 백엔드 개발자 부트캠프 '오르미'에서 팀 프로젝트로 만든 서비스입니다.

서비스 설명, 조이름 설명



&nbsp;개발 기간은 12.8 ~ 12.28 총 21일이었으며 4인 1조의 협업으로 진행되었습니다.


GitHub Repository : https://github.com/OrmiFinal/gluv

FE Repository : https://github.com/OrmiFinal/gluv-FE

배포 URL

테스트 계정

팀원 소개
|김재민|이형섭|강성웅|김동완|
|:---:|:---:|:---:|:---:|
|내용|내용|내용|내용|
|내용|내용|내용|내용|

## <목차>
[1. 요구사항 명세](#요구사항-명세)

[2. 개발기술 및 환경](#개발기술-및-환경)

[3. 프로젝트 구조 및 개발일정](#프로젝트-구조-및-개발일정)

[4. API 명세](#api-명세)

[5. 주요 기능](#주요-기능)

[6. 기능 설명](#기능-설명)

[7. 개발 이슈](#개발-이슈)

[8. 개발 회고](#개발-회고)

## <요구사항 명세>
### [기본 요구사항]
- 회원 관련 기능을 구현
- 회원 관련 기능 포함 최소 3가지 이상의 기능을 구현
- 발표와 시연에 필요한 수준의 UI 구현
- ERD, API 명세서 작성
- README 외에도 발표자료 작성

### [선택 요구사항]
- 모놀리식, 마이크로식, FBV와 CBV의 적절한 사용 등 Django를 적절히 사용
- DB 설계 고도화 (복잡도, 적절성 고려)
- 서비스 배포 : nginx, gunicorn, django 등 적절한 연계를 통한 배포
- 설계와 구현 복잡도 고려 (요구사항 작성, 와이어프레임, 설계에 따른 구현도 등)
- 외부 라이브러리 사용

### [팀 내 작업 방침]
 - 기능 별, 모듈 별 담당을 정해 개발하는 것이 아닌 Task 별 단기 목표 설정, 역할 분배
 - 분업과 코드리뷰 위주의 협업 중시
    - GitHub의 Issue 기능 사용, Pull Request 시 적극적인 Review 유도
 - 서로 이해할 수 있는 코드, 알기 쉬운 변수/함수 명명과 주석 작성
    - [컨벤션] 문서를 작성해 필요 시 참고하면서 작성
 - 진척사항 공유와 다음 작업할 Task 선정을 위해 매일 일정 시간에 모여 회의
    - GitHub Wiki에 [회의록]을 작성해 진척사항과 필요한 내용 기록, 필요할 때 다시 파악

[컨벤션]: https://github.com/OrmiFinal/gluv/wiki/%EC%BB%A8%EB%B2%A4%EC%85%98-%EC%A0%95%EB%A6%AC
[회의록]: https://github.com/OrmiFinal/gluv/wiki/%ED%9A%8C%EC%9D%98%EB%A1%9D

<div align="right">

[목차로](#목차)

</div>

## <개발기술 및 환경>
Uvicorn - 배포

<img src="https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"/>


<img src="https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub Actions-2088FF?style=flat-square&logo=GitHub Actions&logoColor=white"/>
<img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white"/>

### [Frontend]
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=white">
<img src="https://img.shields.io/badge/Tailwind CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white"/>
<img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=white"/>

### [Backend]
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/>

### [DB]
<img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white"/>

### [Deployment]
<img src="https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=nginx&logoColor=white"/>

### [Management]
<img src="https://img.shields.io/badge/Discord-5865F2?style=flat-square&logo=discord&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white"/>
<img src="https://img.shields.io/badge/Notion-000000?style=flat-square&logo=notion&logoColor=white"/>

<div align="right">

[목차로](#목차)

</div>

## <프로젝트 구조 및 개발일정>

### [WBS]
![WBS](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/c308179e-848e-4753-8b7f-c9145cfcd28d)

### [Mindmap]
![mindmap](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/bea6795d-f04a-4f37-9743-4a3f1b99e0a2)

### [ERD]
![erd](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/dd137cc6-827c-44b6-b549-244ac58755a1)

### [Folder Tree]
추후 작성

### [Sequence Diagram]
![시퀀스다이어그램](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/fac8e544-d834-47b5-a872-00ef918ab2a2)
위키 작성 후 링크 추가

### [WireFrame 및 기능설계]
|화면 설계|기능 설계|
|------|------|
|![wireframe](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/ff9a582e-8fd2-4ec9-9eed-b66467341c90)|![wireframe_with_memo](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/6a03ae3b-b711-4133-b88a-a157669fd52b)|

[카카오오븐](https://ovenapp.io/view/jTIlBYAvkFxRd4RxlPTLERLLyP2Sdwe1/B6a8N)링크


### [URL명세]
![image](https://github.com/OrmiFinal/gluv/assets/22714585/6019aa6f-5c81-4381-a1bb-ba109850fd6f)

[URL명세 GitHub Wiki](https://github.com/OrmiFinal/gluv/wiki/URL-%EB%AA%85%EC%84%B8)

### [서비스 아키텍처]

- 내용

<div align="right">

[목차로](#목차)

</div>

## <API 명세>
![image](https://github.com/OrmiFinal/gluv/assets/22714585/269a1416-d5b5-450e-803d-27373913ecce)
1차 [API 설계](https://github.com/OrmiFinal/gluv/wiki/1%EC%B0%A8-API-%EB%AA%85%EC%84%B8),  

![image](https://github.com/OrmiFinal/gluv/assets/22714585/2e5108f2-0edf-4735-805d-3963c3be92d7)

2차 테스트 중 만든 [2차 API 명세](https://github.com/OrmiFinal/gluv/wiki/2%EC%B0%A8-API-%EB%AA%85%EC%84%B8),   
3차 [스웨거]()를 활용한 최종본

- 내용

<div align="right">

[목차로](#목차)

</div>

## <주요 기능>

### [메인화면]

 - 내용
 
### [모집게시글 작성]

 - 내용

### [모임, 일정 관리]

 - 내용

### [모집게시글 조회 및 검색]

 - 내용

### [모임 가입 신청]

 - 내용

### [모임 가입 신청 관리]

 - 내용

### [모임 구성원 관리]

 - 내용

### [모임 단체 채팅]

 - 내용

### [커뮤니티게시글 조회 및 검색]

 - 내용

### [커뮤니티게시글 작성]

 - 내용

### [게시글 좋아요, 신고]

 - 내용

### [알림]

 - 내용


<div align="right">

[목차로](#목차)

</div>

## <기능 시연>

### [회원가입, 로그인 및 프로필 확인]

- 내용

### [모임을 만들 사용자가 모집글 작성]

- 내용

### [모임의 리더가 모임 정보 수정]

- 내용

### [신청할 사용자가 모집글을 읽고 가입 신청]

- 내용

### [모임의 리더가 신청인원 관리 메뉴에서 가입을 수락]

- 내용

### [모임 채팅방에서 채팅]

- 내용

### [커뮤니티 글 작성, 댓글 작성]

- 내용

### [게시글 추천]

- 내용

### [모임의 구성원 강퇴 및 모임 삭제]


<div align="right">

[목차로](#목차)

</div>

## <개발 이슈>

### 1.

### 2.

### 3.

### 4.


<div align="right">

[목차로](#목차)

</div>

## <개발 회고>

### [김재민]

### [이형섭]

### [강성웅]

### [김동완]


<div align="right">

[목차로](#목차)

</div>


