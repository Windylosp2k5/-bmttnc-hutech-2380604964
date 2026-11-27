"""Câu 05 - Đếm số lần xuất hiện của từng phần tử trong List."""


def main():
    danh_sach = [x.strip() for x in input("Nhập các phần tử, cách nhau bởi dấu phẩy: ").split(",")]
    so_lan = {}
    for phan_tu in danh_sach:
        so_lan[phan_tu] = so_lan.get(phan_tu, 0) + 1
    print("Dictionary đếm:", so_lan)


if __name__ == "__main__":
    main()
