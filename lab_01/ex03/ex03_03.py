"""Câu 03 - Tạo Tuple từ danh sách nhập vào."""


def main():
    danh_sach = [x.strip() for x in input("Nhập các phần tử, cách nhau bởi dấu phẩy: ").split(",")]
    bo_tuple = tuple(danh_sach)
    print("Tuple:", bo_tuple)


if __name__ == "__main__":
    main()
