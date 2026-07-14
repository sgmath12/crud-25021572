# 구현 내용

## 개요

참고할 기존 PoC 코드가 로컬 및 GitHub 저장소 어디에도 존재하지 않아, 표준적인 Python 콘솔 구조로 CRUD 애플리케이션을 새로 설계·구현했다. 데이터는 `data.json` 파일에 JSON 배열 형태로 저장한다.

## 파일 구조

```
crud/
├── main.py       # 메뉴 루프 및 CRUD 로직
├── storage.py    # JSON 파일 read/write 헬퍼
├── data.json     # 데이터 저장 파일
└── .gitignore
```

## storage.py

- `load_data()`: `data.json`이 없거나 비어 있으면 빈 리스트를 반환하고, 그렇지 않으면 JSON을 파싱해 리스트로 반환.
- `save_data(data)`: 리스트를 `data.json`에 UTF-8, 들여쓰기 2칸으로 저장 (`ensure_ascii=False`로 한글 그대로 저장).

## main.py

각 데이터 항목은 `{"id": int, "name": str, "value": str}` 형태의 딕셔너리이며, `id`는 `next_id()`로 기존 최대 id + 1을 부여해 자동 생성한다.

- **Create** (`create_item`): 이름/값을 입력받아 새 id를 부여한 뒤 `data.json`에 추가.
- **Read**
  - `read_all()`: 저장된 전체 목록을 출력.
  - `read_one()`: 입력한 값이 숫자면 id로, 아니면 name으로 검색(`find_item`)하여 출력.
- **Update** (`update_item`): id 또는 name으로 대상을 찾은 뒤, 수정할 필드명과 새 값을 입력받아 반영. `id` 필드는 수정 불가.
- **Delete** (`delete_item`): id 또는 name으로 대상을 찾은 뒤, `y` 확인을 받아야 실제로 삭제(안전한 삭제를 위한 확인 절차).

메뉴는 `main()`의 while 루프에서 번호 입력에 따라 각 함수를 호출하며, `0`을 입력하면 종료한다.

## 검증

Windows 콘솔/Git Bash의 UTF-8 stdin 인코딩 이슈로 인해, `input()`을 모킹한 Python 스크립트로 각 함수(create/read_all/read_one/update/delete)를 직접 호출하여 정상 동작을 확인했다.
