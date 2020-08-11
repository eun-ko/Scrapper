# 무신사 Scrapper

#### product_csv
get_items로 받아온 상품정보를 엑셀파일로 저장 (상품명,브랜드명,가격)  
`프로모션상품명 및 할인가 처리`
- [] 프로모션 상품명 정리
- [x] skirt
- [x] 뷰티 :  
       FileNotFoundError: [Errno 2] No such file or directory: '더마콜(DERMACOL) 티트리 파운데이션 (컨실러/파데 2in1).jpg'  
       ->상품명에 '/'포함시 경로로 인식해서 replace로 바꿈
- [x] 양말/레그웨어 :
      FileNotFoundError: [Errno 2] No such file or directory: '일오공칠(IL-O-GONG-CHIL) [10PACK] 1507 모노 트라우져 하프 삭스 \_ 화이트/블랙.jpg'  
      ->상품명에 '/'포함시 경로로 인식해서 replace로 바꿈
---
#### get_image

- [x] 이미지 해상도 높이기 - 상세페이지로 한번더 들어가게 (20200602)
---
#### size_csv
상세페이지에서 사이즈정보 크롤링해서 엑셀파일로 저장  
`사이즈정보 없음/분류 기준 상이한 것들 처리`
- [x] 아우터 (분류기준상이)
- [x] 상의
- [] 바지 

---
- [] 카테고리별 url자동화