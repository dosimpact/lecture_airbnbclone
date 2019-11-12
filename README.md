# 에어비엔비 클론 코딩

## 환경설치

- 아나콘다 + VS code

```
conda create djangostack python==3.7
conda activate djangostack
pip install Django
pip list
```

```
vs code -> 컨트롤 쉬프트 P => select python interpretor djangostack ~
```

## Django VS

- Flask vs Django
  Flask나 Pyrmaid 매우 간단하고 쉽게 웹 어플리케이션을 만들 수 있다.
  Flask는 웹서버 만드는 것을 많이 도와준다. 하지만 reinvent the wheel 데이터베이스 유저인증 form 로그인 로그아웃, 관리자 패널 등등  
  다시 직접 만들어야 하는 많은 부분이 있다.  
  Django는 거대한 프레임 워크라서 공통적으로 필요한것들을 전부 넣었다. 그래서 처음부터 많은것들이 포함되어 있다.  
  컨텐츠관리기능, 이미 관리자 패널이 있다. 사용자 인증도 사이트맵도. 이미 만들어진 form들을 가지고 쉽게 메일인증도 할 수 있다.  
  배워야하는 큰 박스이다. 한번 배운순간 생산성이 급격히 올라간다.

airbnb에 사용하는 수많은 기능들을 django가 많이 지원하기 때문에 좋다.
