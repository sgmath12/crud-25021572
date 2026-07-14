from storage import load_data, save_data


def next_id(data):
    if not data:
        return 1
    return max(item["id"] for item in data) + 1


def create_item():
    data = load_data()
    name = input("이름: ").strip()
    value = input("값: ").strip()
    item = {"id": next_id(data), "name": name, "value": value}
    data.append(item)
    save_data(data)
    print(f"생성 완료 (id={item['id']})")


def read_all():
    data = load_data()
    if not data:
        print("데이터가 없습니다.")
        return
    for item in data:
        print(item)


def find_item(data, key):
    if key.isdigit():
        target_id = int(key)
        for item in data:
            if item["id"] == target_id:
                return item
    for item in data:
        if item["name"] == key:
            return item
    return None


def read_one():
    data = load_data()
    key = input("검색할 ID 또는 이름: ").strip()
    item = find_item(data, key)
    if item is None:
        print("일치하는 데이터가 없습니다.")
    else:
        print(item)


def update_item():
    data = load_data()
    key = input("수정할 ID 또는 이름: ").strip()
    item = find_item(data, key)
    if item is None:
        print("일치하는 데이터가 없습니다.")
        return

    field = input(f"수정할 필드 ({', '.join(k for k in item if k != 'id')}): ").strip()
    if field not in item or field == "id":
        print("존재하지 않는 필드입니다.")
        return

    new_value = input("새 값: ").strip()
    item[field] = new_value
    save_data(data)
    print("수정 완료")


def delete_item():
    data = load_data()
    key = input("삭제할 ID 또는 이름: ").strip()
    item = find_item(data, key)
    if item is None:
        print("일치하는 데이터가 없습니다.")
        return

    confirm = input(f"정말 삭제하시겠습니까? {item} (y/n): ").strip().lower()
    if confirm != "y":
        print("삭제가 취소되었습니다.")
        return

    data.remove(item)
    save_data(data)
    print("삭제 완료")


MENU = """
==== CRUD 콘솔 애플리케이션 ====
1. Create
2. Read (전체 목록)
3. Read (검색)
4. Update
5. Delete
0. 종료
"""


def main():
    actions = {
        "1": create_item,
        "2": read_all,
        "3": read_one,
        "4": update_item,
        "5": delete_item,
    }

    while True:
        print(MENU)
        choice = input("선택: ").strip()
        if choice == "0":
            print("종료합니다.")
            break
        action = actions.get(choice)
        if action is None:
            print("잘못된 선택입니다.")
            continue
        action()


if __name__ == "__main__":
    main()
