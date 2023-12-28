# 독서모임 모집 플랫폼 gluv

&nbsp;이스트소프트에서 주관하는 백엔드 개발자 부트캠프 '오르미'에서 팀 프로젝트로 만든 서비스입니다.

&nbsp;글을 사랑하는 사람들의 모임 모집 플랫폼 gluv입니다. 모임 활동을 하고 싶은 사용자가 플랫폼을 사용해 모임을 만들고, 구성원들과 함께 대화할 수 있는 서비스를 구현하였습니다.  
모집글과 모임 정보를 통해 모임을 관리, 활동할 수 있으며 모든 사용자들이 커뮤니티 게시판을 통해 창작물을 올리고, 의견을 교환할 수 있는 장을 마련하였습니다.

&nbsp;Backend 서버와 Frontend 서버 별개로 개발되었으며, Backend는 Django, Frontend는 React를 사용하였습니다.

&nbsp;개발 기간은 12.8 ~ 12.28 총 21일이었으며 4인 1조의 협업으로 진행되었습니다.


GitHub Repository : https://github.com/OrmiFinal/gluv

FE Repository : https://github.com/OrmiFinal/gluv-FE

배포 URL : http://43.202.4.135/

팀원 소개
|김재민|이형섭|강성웅|김동완|
|:---:|:---:|:---:|:---:|
|![김재민](https://github.com/jmkim648/test/assets/22714585/ff9898bf-9f26-405a-8648-d513ff850bbc)|![강성웅님](https://github.com/jmkim648/test/assets/22714585/19910939-ee10-4ff9-b91a-17a9ab974025)|내용|
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

### [Frontend]
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=white">
<img src="https://img.shields.io/badge/Tailwind CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white"/>
<img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=white"/>

### [Backend]
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/>
<img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"/>
<img src="https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white"/>

### [DB]
<img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white"/>

### [Deployment]
<img src="https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=nginx&logoColor=white"/>
<img src="https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=Gunicorn&logoColor=white"/>
<img src="https://img.shields.io/badge/Uvicorn-6428B4?style=flat-square&logo=Gunicorn&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub Actions-2088FF?style=flat-square&logo=GitHub Actions&logoColor=white"/>
<img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white"/>

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
|Backend|Frontend|
|---|---|
|![image](https://github.com/jmkim648/test/assets/22714585/76bf158c-cf25-47d9-88ff-9c2c75df141b)|![image](https://github.com/jmkim648/test/assets/22714585/9bc70f86-ec93-4878-a271-3946fcbb7b81)|

### [Sequence Diagram]
![시퀀스다이어그램](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/fac8e544-d834-47b5-a872-00ef918ab2a2)
[시퀀스 다이어그램](https://app.diagrams.net/#G1-BYGlJ5SfI52E6yEfLoS7qUKThqh-JP_)
[시퀀스 다이어그램 Wiki](https://github.com/OrmiFinal/gluv/wiki/Sequence-Diagram)

### [WireFrame 및 기능설계]
|화면 설계|기능 설계|
|------|------|
|![wireframe](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/ff9a582e-8fd2-4ec9-9eed-b66467341c90)|![wireframe_with_memo](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/6a03ae3b-b711-4133-b88a-a157669fd52b)|

[카카오오븐 Wireframe](https://ovenapp.io/view/jTIlBYAvkFxRd4RxlPTLERLLyP2Sdwe1/B6a8N)


### [URL명세]
![image](https://github.com/OrmiFinal/gluv/assets/22714585/6019aa6f-5c81-4381-a1bb-ba109850fd6f)

[URL명세 GitHub Wiki](https://github.com/OrmiFinal/gluv/wiki/URL-%EB%AA%85%EC%84%B8)

### [서비스 아키텍처]

![아키텍처](https://github.com/OrmiFinal/gluv/assets/22714585/73e014c3-b8fe-4bb6-a2df-0b524a71739f)

<div align="right">

[목차로](#목차)

</div>

## <API 명세>
![image](https://github.com/OrmiFinal/gluv/assets/22714585/269a1416-d5b5-450e-803d-27373913ecce)
1차 [API 설계](https://github.com/OrmiFinal/gluv/wiki/1%EC%B0%A8-API-%EB%AA%85%EC%84%B8) 

![image](https://github.com/OrmiFinal/gluv/assets/22714585/2e5108f2-0edf-4735-805d-3963c3be92d7)
2차 테스트 중 만든 [2차 API 명세](https://github.com/OrmiFinal/gluv/wiki/2%EC%B0%A8-API-%EB%AA%85%EC%84%B8)

![image](https://github.com/jmkim648/test/assets/22714585/3ea9174b-36d1-4ab1-8241-f1cb8af49dd1)
3차 스웨거를 활용한 [최종 API 명세](https://github.com/OrmiFinal/gluv/wiki/3%EC%B0%A8-API-%EB%AA%85%EC%84%B8-(Swagger))

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
```
 팀원분의 작업이 끝나면 다음으로 해야 할 것을 배분해드리는 일을 하면서 고민이 많았습니다. 지금 맡은 작업이 버겁거나 오래걸릴 것 같지는 않은 지, 해당 기능에 대한 요구사항이 제대로 전달되었는지 확신이 들지 않았습니다. 프로젝트가 끝나갈 때쯤 되어서야 이 분이 어떤 작업에 더 편하고 능숙하신 지 파악하고, 보다 더 명확한 요구사항을 전달할 수 있게 되었습니다. 협업을 할 때는 의사소통이 가장 중요하다는 것, 유능한 관리자가 있어야 한다는 것을 실감한 좋은 기회였습니다.

 혼자서 프로젝트를 진행할 때는 ‘와, 이 기능을 써봤다! 익숙해졌다!’정도의 배움이었다면, 협업을 하면서 그 이상의 것을 배웠다고 생각합니다. 제가 생각했던 것과는 다른 방향으로 구현되는 기능들이나, 더 효율적인 코드들을 보고 습득하는 것은 이전에 느껴보지 못했던 새로운 즐거움이었습니다.
```

### [이형섭]
```
 프로젝트를 시작하기 전에는 수업을 통해 지식을 배우고 프로젝트를 통해 실제로 직접 개발을 경험하며 많은 것을 배울 수 있었습니다.

 서비스 설계부터 구현, 테스트, 배포까지의 과정을 거치면서 각 단계마다 직면하는 문제들을 해결하고 성장할 수 있었습니다.
```

### [강성웅]
```
 요구 사항 정의, 설계, 구현, 테스트, 배포 등의 단계를 경험하면서 전반 적인 개발을 이해할 수 있었습니다.

 프로젝트 중 깃을 사용하면서 주로 병합 시 버그가 발생하는 어려움이 있었습니다. 이부분은 다른 팀원들에게 배워서 더욱 좋아졌습니다.
```

### [김동완]
```
 이번 팀 프로젝트를 통해 잊고 있던 개발의 재미를 다시 한 번 느꼈습니다. 설계부터 배포까지 협업의 과정을 통해 성장할 수 있었습니다. 그리고 그 모든 과정에 함께해주신 팀원 분들과 강사님들께 감사드립니다. DRF의 능력을 작게나마 시험해본 경험을 양분삼아 더 많이 오래 개발해나가고 싶습니다.
```


<div align="right">

[목차로](#목차)

</div>


