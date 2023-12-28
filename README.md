# 독서모임 모집 플랫폼 gluv

&nbsp;이스트소프트에서 주관하는 백엔드 개발자 부트캠프 '오르미'에서 팀 프로젝트로 만든 서비스입니다.

&nbsp;글을 사랑하는 사람들의 모임 모집 플랫폼 gluv입니다. 모임 활동을 하고 싶은 사용자가 플랫폼을 사용해 모임을 만들고, 구성원들과 함께 대화할 수 있는 서비스를 구현하였습니다.  
모집글과 모임 정보를 통해 모임을 관리, 활동할 수 있으며 모든 사용자들이 커뮤니티 게시판을 통해 창작물을 올리고, 의견을 교환할 수 있는 장을 마련하였습니다.

&nbsp;Backend 서버와 Frontend 서버 별개로 개발되었으며, Backend는 Django, Frontend는 React를 사용하였습니다.

&nbsp;개발 기간은 12.8 ~ 12.28 총 21일이었으며 4인 1조의 협업으로 진행되었습니다.


GitHub Repository : https://github.com/OrmiFinal/gluv

FE Repository : https://github.com/OrmiFinal/gluv-FE

배포 URL : http://43.202.4.135/

### 팀원 소개
|김재민|이형섭|강성웅|김동완|
|:---:|:---:|:---:|:---:|
|<img src="https://github.com/OrmiFinal/gluv/assets/22714585/f7748427-537b-49e4-8e5f-d61539abb0e0" alt="김재민" width="150" height="150">|<img src="https://github.com/OrmiFinal/gluv/assets/22714585/118d18a1-8ddc-476c-9040-c7a9328039ae" alt="이형섭" width="150" height="150">|<img src="https://github.com/OrmiFinal/gluv/assets/22714585/ca2b462d-110f-4b38-820f-d5a34eeb604e" alt="강성웅" width="180" height="150">|<img src="https://github.com/OrmiFinal/gluv/assets/22714585/1851d9f7-6f31-49f3-9fcd-1a504b418992" alt="김동완" width="150" height="150">|
|<p align="left"> - 화면 설계 및 기능 명세 <br> - Recruit, Team, Schedule <br> - 프로젝트 진행 관리, <br> &nbsp;&nbsp; 작업 배분|<p align="left"> - URL 및 API 설계 <br> - Post, Book, Report, <br> &nbsp;&nbsp; Notification <br> - Swagger, Redis, ChatRoom <br> - 배포 리드 |<p align="left"> - 시퀀스 다이어그램 <br> - Like <br> - Frontend React 세팅 <br> - Design Layout 적용|<p align="left"> - WBS 작성 <br> - User, Comment <br> - Auth 구현 및 Token <br>&nbsp;&nbsp; 핸들링 <br> - API 호출 시 Error <br> &nbsp;&nbsp;핸들링|


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
<div>
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/>
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=white">
    <img src="https://img.shields.io/badge/Tailwind CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white"/>
    <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=white"/>
</div>

### [Backend]
<div>
    <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white"/>
    <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"/>
    <img src="https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white"/>
</div>

### [DB]
<img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white"/>

### [Deployment]
<div>
    <img src="https://img.shields.io/badge/NGINX-009639?style=flat-square&logo=nginx&logoColor=white"/>
    <img src="https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=Gunicorn&logoColor=white"/>
    <img src="https://img.shields.io/badge/Uvicorn-6428B4?style=flat-square&logo=Gunicorn&logoColor=white"/>
    <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"/>
    <img src="https://img.shields.io/badge/GitHub Actions-2088FF?style=flat-square&logo=GitHub Actions&logoColor=white"/>
    <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white"/>
</div>

### [Management]
<div>
    <img src="https://img.shields.io/badge/Discord-5865F2?style=flat-square&logo=discord&logoColor=white"/>
    <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white"/>
    <img src="https://img.shields.io/badge/Notion-000000?style=flat-square&logo=notion&logoColor=white"/>
</div>

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
|![image](https://github.com/OrmiFinal/gluv/assets/22714585/b6f9dd06-574c-4f35-a860-e2b760dc0859)|![image](https://github.com/OrmiFinal/gluv/assets/22714585/6c908c95-fd7b-404c-aa6b-e38026e1829e)|

- 크기 문제로 인해 일부만 표시합니다. 전체 내용은 Wiki 링크 첨부합니다.
- Backend : Django로 제작되었으며 12개의 앱으로 구성되어 있습니다.  
    chatrooms 앱은 웹소켓을 통한 채팅 구현을 위해 routing.py와 consumer.py가 추가되었습니다.  
    books 앱은 알라딘 API와의 통신을 위해 crawlers를 추가로 구현하였습니다.  
    gluv 프로젝트에는 celery를 통한 스케쥴러 기능을 위해 celery.py로 설정을 추가했습니다.  
    redis와 docker 설정을 위해 별개의 폴더로 관리하고 있습니다.  
- Frontend : React로 제작되었습니다.  
    각각의 페이지 표현을 위한 pages 파일들 외에, 재사용성을 위한 components와 context, API 호출을 관리하기 위한 API 폴더로 관리되고 있습니다.
- [Folder Tree GitHub Wiki](https://github.com/OrmiFinal/gluv/wiki/Folder-Tree)

### [Sequence Diagram]
![시퀀스다이어그램](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/fac8e544-d834-47b5-a872-00ef918ab2a2)  

- 크기 문제로 인해 일부만 표시합니다. 전체 내용은 Wiki 링크 첨부합니다.

- [시퀀스 다이어그램](https://app.diagrams.net/#G1-BYGlJ5SfI52E6yEfLoS7qUKThqh-JP_)  
- [시퀀스 다이어그램 GitHub Wiki](https://github.com/OrmiFinal/gluv/wiki/Sequence-Diagram)

### [WireFrame 및 기능설계]
|화면 설계|기능 설계|
|------|------|
|![wireframe](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/ff9a582e-8fd2-4ec9-9eed-b66467341c90)|![wireframe_with_memo](https://github.com/jmkim648/Ormi-Chatbot-BE/assets/22714585/6a03ae3b-b711-4133-b88a-a157669fd52b)|

- 크기 문제로 인해 일부만 표시합니다. 전체 내용은 링크 첨부합니다.
- WireFrame을 통해 화면설계를 진행하면서 메모를 사용해 기능설계를 겸했습니다. 기능별 요구사항을 정리하여 팀원들과 공유할 수 있도록 하였습니다.
- [카카오오븐 Wireframe](https://ovenapp.io/view/jTIlBYAvkFxRd4RxlPTLERLLyP2Sdwe1/B6a8N)


### [URL명세]
![image](https://github.com/OrmiFinal/gluv/assets/22714585/6019aa6f-5c81-4381-a1bb-ba109850fd6f)

- 크기 문제로 인해 일부만 표시합니다. 전체 내용은 Wiki 링크 첨부합니다.
- URL자원과 GET, POST, PUT, DELETE 등의 메소드 및 설명, 인증과 권한에 대한 정보를 명시하였습니다.
- [URL명세 GitHub Wiki](https://github.com/OrmiFinal/gluv/wiki/URL-%EB%AA%85%EC%84%B8)

### [WebSocket명세]
![image](https://github.com/OrmiFinal/gluv/assets/22714585/ade03e9f-9d76-473a-aa13-27cfbfa95bf6)
- 크기 문제로 인해 일부만 표시합니다. 전체 내용은 Wiki 링크 첨부합니다.
- WebSocket을 쓰면서 생소한 부분이 많았고 새롭게 배운 것도 많았습니다. 채팅기능을 구현하면서 WebSocket의 명세화 필요성을 느꼈습니다.
- [WebSocket명세 GitHub Wiki](https://github.com/OrmiFinal/gluv/wiki/ChatRoom-WebSocket-API-%EB%AC%B8%EC%84%9C)


### [서비스 아키텍처]

![아키텍처](https://github.com/OrmiFinal/gluv/assets/22714585/73e014c3-b8fe-4bb6-a2df-0b524a71739f)

<div align="right">

[목차로](#목차)

</div>

## <API 명세>

### [1차 API 설계]
![image](https://github.com/OrmiFinal/gluv/assets/22714585/269a1416-d5b5-450e-803d-27373913ecce)

### [2차 API 명세]
![image](https://github.com/OrmiFinal/gluv/assets/22714585/2e5108f2-0edf-4735-805d-3963c3be92d7)

### [최종 API 명세]
![image](https://github.com/OrmiFinal/gluv/assets/22714585/b6c242ba-e311-4c74-9854-e46a3aa1af6e)


- 크기 문제로 인해 일부만 표시합니다. 전체 내용은 Wiki 링크 첨부합니다.
- 기획 시 API설계를 진행하였습니다. 기능을 구현할 때 해당 설계를 참조하여 Endpoint, 반환 Data의 형태를 통일할 수 있도록 시도하였습니다.
- API의 초기 구현이 끝난 뒤 테스트를 거치면서 설계와 달라진 점을 반영, 2차로 API 명세를 만든 뒤 마지막으로 Swagger 기능을 통해 최종 API 명세를 만들었습니다.

- [1차 API 설계 GitHub Wiki](https://github.com/OrmiFinal/gluv/wiki/1%EC%B0%A8-API-%EB%AA%85%EC%84%B8) 
- [2차 API 명세 GitHub Wiki](https://github.com/OrmiFinal/gluv/wiki/2%EC%B0%A8-API-%EB%AA%85%EC%84%B8)
- [최종 API 명세 GitHub Wiki](https://github.com/OrmiFinal/gluv/wiki/3%EC%B0%A8-API-%EB%AA%85%EC%84%B8-(Swagger))

<div align="right">

[목차로](#목차)

</div>

## <주요 기능>

### [메인화면]
![image](https://github.com/OrmiFinal/gluv/assets/22714585/06c0a7ac-fc79-4656-a37b-7c26edec1c1e)
 - 메인화면의 UI입니다.
 
### [모집게시글 작성]
|모집게시글 작성|모임 상세정보 조회|
|---|---|
|![image](https://github.com/OrmiFinal/gluv/assets/22714585/e5573cca-44bc-4688-9ea4-6ee5d6dbef02)|![image](https://github.com/OrmiFinal/gluv/assets/22714585/b1f1787a-c85f-4386-a275-70dff8ac288e)|

|모임 상세정보 수정|모집게시글 반영|
|---|---|
|![image](https://github.com/OrmiFinal/gluv/assets/22714585/6871153f-ddd9-4d1c-a04e-04c8f6a69a19)|![image](https://github.com/OrmiFinal/gluv/assets/22714585/3dd17259-bf0d-494c-95ef-c9f940943938)|

 - 모임을 주최하고 싶은 사용자는 모집게시글을 작성해야합니다.
 - 모집 게시글을 작성하면 모임과 모임의 일정 Data가 같이 생성되며, 글을 쓴 사용자는 모임의 리더가 됩니다.
 - 모임의 리더는 일정, 모임의 이미지 등의 정보를 수정할 수 있으며, 이는 모집게시글에도 반영됩니다.
 - 모임의 일정에는 '주기(frequency)', '주(week)', '요일(day)' 속성이 있습니다. 이를 통해 모임의 빈도를 '매일/매주/매월'과 같이 설정할 수 있으며, 빈도가 매월일 경우 '첫번째 주', '두번째 주' '월요일', '화요일'과 같이 구체적으로 지정할 수 있습니다.

### [모집게시글 조회 및 검색]
|모집 게시글 조회|모집 게시글 검색|
|---|---|
|![image](https://github.com/OrmiFinal/gluv/assets/22714585/8f6559d9-113b-469e-a5ed-3fbcc072bc42)|![image](https://github.com/OrmiFinal/gluv/assets/22714585/b62fe2e0-1f4d-417e-990b-4edd7b853027)|
 - 모임에 참여하고 싶은 사용자는 모집게시글을 조회 후, 마음에 드는 모임에 가입신청을 해야합니다.
 - 모임 모집 게시판은 상단의 Navbar를 눌러 이동할 수 있으며, 카테고리 설정, 정렬순서 변경 등을 통해 list에 노출되는 게시글을 조절할 수 있습니다.
 - 하단의 Input창을 통해 게시물의 제목을 검색할 수 있습니다.


### [모임 가입 신청]

![image](https://github.com/OrmiFinal/gluv/assets/22714585/6b1561cf-d68a-4214-a438-e914c06d92d3)
- 사용자가 마음에드는 모집게시글을 찾았을 때, 우측 하단의 신청하기 버튼을 통해 모임에 가입 신청을 할 수 있습니다.
- 가입신청을 누르면 해당 모임의 TeamMember Instance가 생성됩니다. 이 Instance에는 is_approved 필드가 있어 값이 False일 경우에는 가입 신청중인 사용자, 값이 True일 경우에는 모임의 구성원으로 판단하게 됩니다.

### [모임 가입 신청 관리]

![image](https://github.com/OrmiFinal/gluv/assets/22714585/0df9b018-7730-4d2f-959c-64300bd59de4)
- 모임의 리더는 모임 정보의 '신청인원 관리' 메뉴에서 가입신청한 회원에 대한 승인과 거절을 할 수 있습니다.
- 모임의 리더가 신청을 승인하면 해당 사용자의 TeamMember Instance의 is_approved 값이 True로 바뀌며 모임의 구성원으로 인정됩니다.
- 신청을 거절한다면 해당 사용자의 TeamMember Instance가 삭제됩니다.

### [모임 구성원 관리]
![image](https://github.com/OrmiFinal/gluv/assets/22714585/0414a427-f552-4a36-a175-312f760512b1)
- 모임 정보 중 '구성원 관리' 메뉴에서는 모임의 구성원 목록을 확인 할 수 있습니다.
- 모임의 리더는 구성원에게 리더 권한을 이전할 수 있으며, 강퇴 또한 가능합니다.
- 모임장 이전 버튼을 누르면 해당 구성원의 TeamMember Instance의 속성 중 is_leader의 값이 True가 되며 리더로 바뀝니다. 기존의 리더의 is_leader 속성은 False가 되면 모임의 구성원으로 전환됩니다.
- 강퇴 버튼을 누르면 해당 구성원의 TeamMember Instance가 삭제되어 모임의 구성원으로 인정받지 못합니다.
- 모임의 리더가 모임을 탈퇴하면 리더의 역할을 할 구성원이 필요합니다. 따라서 is_leader의 값이 True인 구성원이 모임 탈퇴를 누를 경우 다음 index의 구성원을 찾아 is_leader의 값을 True로 변경합니다.
- 모임의 구성원이 리더 혼자일 경우 모임의 탈퇴가 불가능하며, 모임을 삭제해야합니다.

### [모임 단체 채팅]
|채팅방 입장|모임 채팅|
|---|---|
|![image](https://github.com/OrmiFinal/gluv/assets/22714585/81e61e49-4085-49bc-afe1-254e51e39ee0)|![image](https://github.com/OrmiFinal/gluv/assets/22714585/84900efe-c555-41d9-afe8-fd1b9f8bd676)|
- 모임의 구성원은 모임 정보 우측 하단의 '채팅방 입장' 버튼을 통해 모임의 채팅방에 입장할 수 있습니다.
- 채팅방의 좌측에는 로그인한 유저가 가입한 모든 모임의 채팅 list를 볼 수 있습니다. 모임의 이름을 클릭하면 해당 채팅방으로 이동할 수 있습니다.
- 채팅은 Django Channels를 사용하여 웹소켓을 구현하였습니다. Redis를 활용하여 채팅 기능 사용 시 DB의 데이터 대신 캐시에 저장된 메모리를 활용할 수 있도록 하였습니다.
- 사용자가 메시지를 송신할 때, 해당 유저가 모임의 구성원인지 파악하는 과정을 DB가 아니라 캐시에 저장된 메모리를 사용하도록 함으로써 더 빠른 응답속도를 기대할 수 있었습니다.  

<br>

![image](https://github.com/OrmiFinal/gluv/assets/22714585/0359a1f6-0d14-4491-a4c0-3c3f23400657)
- Django Channels를 사용하고 ASGI를 설정했을 때의 통신구조를 나타낸 그림입니다.
- Request, Response의 흐름을 channel의 layer를 지나는 Message의 형태로 변경하게 됩니다. 이 때 HTTP Request의 경우, layer를 거치지 않고 기존의 흐름을 유지하고 있습니다.

### [커뮤니티게시글 조회 및 검색]
![image](https://github.com/OrmiFinal/gluv/assets/22714585/39e61931-caf3-49db-84cd-114271fe5cf0)
 - 사용자는 모임 외에도 커뮤니티 게시글을 통해 글을 쓰고 소통할 수 있습니다.
 - 커뮤니티 게시글은 여러개의 카테고리로 구성되어 있으며 메뉴를 통해 해당 카테고리의 글만 조회할 수 있습니다.
 - 또한 하단의 Input을 통해 게시글의 제목을 검색할 수 있습니다.
 - 카테고리 게시글 list를 조회하는 Endpoint는 `/posts/?search={search}&category={category}&page={page}`입니다.
 - 'search' 파라미터를 통해 게시글의 제목을 필터링 해 찾아올 수 있으며, category 파라미터를 통해 원하는 카테고리의 글을 list해 가져옵니다.

### [댓글]
![image](https://github.com/OrmiFinal/gluv/assets/22714585/4eec4758-6d71-4a28-ad27-90a70855cd8c)
- 사용자는 게시글에서 댓글을 통해 의사소통할 수 있습니다.
- 댓글의 DB에는 대댓글을 표현할 속성으로 유저의 데이터를 담고 있습니다. 특정 댓글에 대한 대댓글을 구현하는 대신 원하는 사용자의 닉네임을 태그하는 형태로 구현하였습니다.
- 댓글 DB 내 대댓글 대상인 유저의 데이터가 없을 경우 일반 댓글이 작성되며, 데이터가 있을 경우에는 해당 유저의 닉네임을 태그해 당사자에게 남기는 댓글임을 명시합니다.

### [화제의 게시글, 최근 게시글]
|화제의 게시글|최근 게시글|
|---|---|
|![image](https://github.com/OrmiFinal/gluv/assets/22714585/1212e092-d20f-4b87-9d55-30918718b7d0)|![image](https://github.com/OrmiFinal/gluv/assets/22714585/c23c57a0-36a2-40ff-985a-97eb3a538258)|

- 메인화면과 일부 게시판에서는 화제의 게시글, 최근 게시글을 list하고 있습니다.
- 게시물의 속성 중 'created_at'과 'viewcount'를 조건으로 필터링하여 일정 개수를 반환해 출력합니다.

### [게시글 좋아요]
|좋아요|좋아요 취소|
|---|---|
|![image](https://github.com/OrmiFinal/gluv/assets/22714585/2eaad7f0-70f5-4f6e-8de3-cddf398fb515)|![image](https://github.com/OrmiFinal/gluv/assets/22714585/295fc008-203c-400f-8c84-25c90206638c)|
 
- 사용자는 마음에 든 모집 게시글과 커뮤니티 게시글에 좋아요를 줄 수 있습니다. 게시글 상세 페이지에서는 유저가 해당 게시글에 좋아요를 눌렀는지를 판단해 버튼의 종류를 다르게 보여줍니다.

### [신간 정보]
![image](https://github.com/OrmiFinal/gluv/assets/22714585/64ff3b5a-7adb-4be5-ba35-b23722c2951f)

- 메인화면의 상단에는 알라딘 API를 통해 전송받은 도서 정보를 통해 신간 정보를 출력합니다.
- 책의 이미지, 제목, 지은이를 출력하고 있으며 해당 항목을 클릭시 알라딘의 도서 판매 페이지로 이동합니다.
- 신간정보의 DB는 Book 앱 내부의 Task기능을 통해 일정 시간마다 알라딘 API를 호출받아 저장합니다.
- Task 기능은 Celery 패키지를 사용해 구현하였습니다.

### [알림, 신고]
|새 알림|전체 알림|읽은 알림|
|---|---|---|
|![image](https://github.com/OrmiFinal/gluv/assets/22714585/7f60d067-a72a-498c-8184-432bf6395068)|![image](https://github.com/OrmiFinal/gluv/assets/22714585/d9fd7aae-7165-484a-a50f-3db76803f0b5)|![image](https://github.com/OrmiFinal/gluv/assets/22714585/61268b7d-5bef-4cf0-81cd-17f78577b695)|

- 사용자가 가입한 모임의 일정이 변경되면 알림이 발송됩니다. 사용자가 헤더 우상단의 알림 버튼을 누르면 알림 모달창이 출력됩니다. 전체 알림 버튼을 누르면 전체 알림 모달이 출력됩니다.
- 새 알림은 사용자가 읽지 않은 알림을 필터하여 출력합니다. 전체 알림에서는 사용자가 읽은 알림은 흐리게 처리하여 읽지 않은 알림과 구분되도록 구현하였습니다.

<br>

![image](https://github.com/OrmiFinal/gluv/assets/22714585/e6ff4de9-5864-4109-855f-09ca38a4a151)
- 사용자는 모집 게시글이나 커뮤니티 게시글에서 문제를 발견했을 때 해당 유저를 신고할 수 있습니다.
- 게시글의 신고 버튼을 누르면 신고 내용의 data를 담은 instance가 생성됩니다.

<div align="right">

[목차로](#목차)

</div>

## <기능 시연>

### [회원가입, 로그인 및 프로필 확인]

![1](https://github.com/OrmiFinal/gluv/assets/22714585/e7af2ddd-1ba9-4e56-a17a-8ef67de4e84e)

- 로그인과 회원가입 페이지는 모달창으로 구현되었습니다.
- JWT토큰을 사용하여 사용자 로그인을 구현하였으며, 토큰은 local storage에 저장해 핸들링합니다.

### [모집글을 읽은 사용자가 가입 신청]

![2](https://github.com/OrmiFinal/gluv/assets/22714585/a4ac8b11-a193-47d0-9aaa-b5a7b428cbdd)

- 게시글의 우하단 신청하기 버튼을 통해 가입 신청을 할 수 있으며, 좌하단의 신청 확인을 누르면 알림 메시지로 사용자가 이미 신청을 했는지, 아닌지를 알려줍니다.

### [리더의 신청인원 가입 수락]

![3](https://github.com/OrmiFinal/gluv/assets/22714585/dc3eec82-64d7-48b5-a3c6-c02c649cf00e)

- 신청인원의 가입을 수락하면 해당 사용자는 모임의 구성원으로 인정되어 구성원 관리 메뉴에서 확인할 수 있게 됩니다.

### [모임 일정 변경]

![4](https://github.com/OrmiFinal/gluv/assets/22714585/3953f9e9-0267-492d-9247-4cd572961c34)

- 모임의 리더는 '모임 정보 수정' 메뉴에서 모임의 일정을 변경할 수 있습니다.

### [알림 확인 및 수신처리]

![5](https://github.com/OrmiFinal/gluv/assets/22714585/9b343196-c947-4259-aaed-4f0344e55265)

- 모임의 일정이 변경될 때마다 구성원에게 알림이 발송됩니다.

### [게시글 작성 및 댓글 작성]

![6](https://github.com/OrmiFinal/gluv/assets/22714585/058ad471-6810-4975-8b31-e94cc408151e)


### [커뮤니티 게시글 좋아요]

![7](https://github.com/OrmiFinal/gluv/assets/22714585/fa8f4e41-273d-4495-ac17-289d290170b7)

### [모집 게시글 추천]

![8](https://github.com/OrmiFinal/gluv/assets/22714585/b474e834-1c81-4848-890a-feb76e7816e9)

### [모임 구성원 강퇴]

![9](https://github.com/OrmiFinal/gluv/assets/22714585/fe73d087-75ca-4251-b803-d58fc7df2f0e)

### [모임 탈퇴]

![10](https://github.com/OrmiFinal/gluv/assets/22714585/7d6cf306-9025-498d-847a-2a1170707e61)


<div align="right">

[목차로](#목차)

</div>

## <개발 이슈>

### 1.get_object()의 반복으로 인한 쿼리 과다 호출 문제

- 현상 : 모임 상세 정보를 요청했을 때 반환까지 시간이 오래 걸리는 문제 발생
- 원인 : 모임 상세 정보는 모임의 정보 외에도 모집 게시글, 일정의 정보까지 조회할 필요가 있었습니다. 이 때 모임의 serializer에서 모집 게시글,  
    일정의 정보를 하나하나 get_object()설정을 해놓아 필요 이상의 쿼리가 발생하고 있었습니다. 
- 해결 : 리팩토링을 진행하여 related_data를 구성해 한번의 쿼리 요청으로 필요한 모든 정보를 받을 수 있도록 설정하였습니다.  
    반환까지의 시간이 1/3정도 단축되는 효과가 있었습니다. 

|결과1|결과2|
|---|---|
|![image](https://github.com/OrmiFinal/gluv/assets/22714585/efab6930-c745-488b-8654-4cf0a90b834e)|![image](https://github.com/OrmiFinal/gluv/assets/22714585/e83b86ce-468f-474f-8dae-a5bd5df9aaf5)|

### 2. 1:1:1 구조의 모델 data 생성 중 오류가 났을 시 DB의 무결성이 깨지는 문제

- 현상 : 모집 게시글, 모임, 일정 View를 구현한 뒤 테스트 중 DB에 손상된 파일이 생기며 읽을 수 없는 경우가 생기는 문제 발생
- 원인 : 모집 게시글을 작성할 시, 1:1관계를 가지는 모임, 일정 모델이 같이 생성됩니다. 이 때 생성되던 도중 오류가 발생하면 모집게시글 생성은 취소되지만 해당 과정 중  
    생성된 모임, 일정과 모임 구성원 Data가 무결성이 깨진 채로 남아있었습니다.
- 해결 : 모집 게시글 생성 View에 @transaction.atomic 데코레이터를 지정하여 원자성 부여, 오류가 생겼을 시 트랜잭션을 롤백할 수 있도록 설정하였습니다.

|오류|해결|
|---|---|
|![image](https://github.com/OrmiFinal/gluv/assets/22714585/c910cc6f-19f9-4164-a256-f055c7d4744d)|![image](https://github.com/OrmiFinal/gluv/assets/22714585/d33f877b-93f2-4a87-8945-977913898ef2)|

### 3. nginx에서 배포한 정적 파일에 접근할 수 없는 문제 

- 현상 : user 및 team의 디폴트 이미지를 Nginx 403 에러로 불러올 수 없는 문제 발생
- 원인 : Ubuntu 디렉토리 권한 설정 문제로 nginx가 Media 디렉토리에 접근할 수 없어 이미지를 가져올 수 없었습니다.
- 해결 : nginx가 접근 가능한 디렉토리에 media 디렉토리를 마운트하여 접근할 수 있도록 조치했습니다.

|오류|해결|
|---|---|
|![image](https://github.com/OrmiFinal/gluv/assets/22714585/d193a664-0037-475f-a7f2-8614a9fa880b)|![image](https://github.com/OrmiFinal/gluv/assets/22714585/a099f3af-f602-4549-89a9-b7bb97146f22)|


### 4. FE에서 페이지 별, 기능 별 API 요청이 반복되던 문제

 - 현상 : 특정 기능에서 API 호출 오류가 발생했을 때 수정하는데 많은 시간과 공수가 들어가는 문제
 - 원인 : 모든 페이지 파일에서 별개의 fetch를 작성하면서 코드의 재사용성이 떨어지는 상황이었습니다. 문제를 개선하기 위해 fetch를 모듈로 빼 (api/*.js) 작성했으나,  
    아직도 반복작업이 많음을 느끼고 API요청을 공통 모듈로 빼는 작업을 가졌습니다(api/api.js).
 - 해결 : 구현과 배포 후 버그 수정과정에서 시간과 공수를 아낄 수 있었으며, 이후 fetch를 인터셉트해 예외처리 하는 부분을 상대적으로 빠르고 쉽게 구현할 수 있었습니다.

|api.js|api 호출 시|
|---|---|
|![image](https://github.com/OrmiFinal/gluv/assets/22714585/1935c9a9-9f4f-480f-9010-19671fb4bbb7)|![image](https://github.com/OrmiFinal/gluv/assets/22714585/12715063-2441-4f77-91a9-6a96b68c213d)|

### 5. 웹소켓 통신 시 인증 구현 문제

 - 현상 : 웹소켓 연결 시 헤더를 설정할 수 없어 JWT 토큰을 사용한 인증 구현 불가
 - 원인 : 사전조사를 할 때 기존 일부 웹소켓 서비스들이 연결 시 JWT 토큰을 사용하여 사용자 인증을 구현하고 있음을 파악했습니다.  
    하지만 MDN 문서를 살펴보니 본 프로젝트에서 사용하고 있던 웹소켓은 연결 시 헤더를 설정할 수 없다는 것을 확인했습니다.
 - 해결 : 웹소켓 통신 내에서 사용자 인증을 구현하는 방식으로 전환하였습니다.

![image](https://github.com/OrmiFinal/gluv/assets/22714585/ab824663-2049-4c55-957f-9de89dfa0b70)

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
