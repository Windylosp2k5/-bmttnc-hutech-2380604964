"""Câu 02 - Đảo ngược thứ tự phần tử trong List."""


def main():
    danh_sach = [x.strip() for x in input("Nhập các phần tử, cách nhau bởi dấu phẩy: ").split(",")]
    print("Danh sách đảo ngược:", danh_sach[::-1])


if __name__ == "__main__":
    main()
