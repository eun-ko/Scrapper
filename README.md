# 무신사

#### product_csv

: get_items로 받아온 상품정보를 엑셀파일로 저장 (상품명,브랜드명,가격)  
`프로모션상품명 및 할인가 처리`

- [ ] 프로모션 상품명 정리
- [x] skirt
- [x] 뷰티 :  
       FileNotFoundError: [Errno 2] No such file or directory: '더마콜(DERMACOL) 티트리 파운데이션 (컨실러/파데 2in1).jpg'  
       ->상품명에 '/'포함시 경로로 인식해서 replace로 바꿈
- [x] 양말/레그웨어 :
      FileNotFoundError: [Errno 2] No such file or directory: '일오공칠(IL-O-GONG-CHIL) [10PACK] 1507 모노 트라우져 하프 삭스 \_ 화이트/블랙.jpg'  
       ->상품명에 '/'포함시 경로로 인식해서 replace로 바꿈

---

#### get_image

- [x] 이미지 해상도 높이기 - 상세페이지로 한번더 들어가게

---

#### get_image_by_brand

- [x] 브랜드별로 이미지 탐색할때는 다른 class에 img감싸져있음

---

#### size_csv

: 상세페이지에서 사이즈정보 크롤링해서 엑셀파일로 저장  
`사이즈정보 없음/분류 기준 상이한 것들 처리`

- [x] 아우터 (분류기준상이)
- [x] 상의

---

#### bottom_size_csv

: 카테고리-바지 사이즈정보 엑셀파일로 저장  
`table로 안되어있는것들`

- [ ] 상세정보 버튼 밑 글씨
- [ ] 이미지 형태

---

- [ ] 카테고리별 url자동화

###### 상의 001

- 반팔 : 001001
- 긴팔 : 001010
- 맨투맨/스웨트 : 001005
- 후드 : 001004

###### 아우터 002

- 후드집업 : 002022
- 블루종 : 002001
- 환절기코트 : 002008
- 레더/라이더재킷 : 002002
- 슈트/블레이저 재킷 : 002003

###### 바지 003

- 데님 : 003002
- 코튼 : 003007
- 트레이닝/조거 : 003004
