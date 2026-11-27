"""Câu 06 - Xóa phần tử trong Dictionary theo key."""


def main():
    dictionary = {}
    print("Nhập các cặp key=value; để trống key để kết thúc.")
    while True:
        key = input("Key: ").strip()
        if not key:
            break
        dictionary[key] = input("Value: ").strip()

    key_can_xoa = input("Nhập key cần xóa: ").strip()
    if key_can_xoa in dictionary:
        del dictionary[key_can_xoa]
        print(f"Đã xóa key '{key_can_xoa}'.")
    else:
        print(f"Không tìm thấy key '{key_can_xoa}'.")
    print("Dictionary hiện tại:", dictionary)


if __name__ == "__main__":
    main()
