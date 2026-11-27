"""Câu 01 - Tính tổng các số chẵn trong một List."""


def main():
    danh_sach = [int(x.strip()) for x in input("Nhập các số, cách nhau bởi dấu phẩy: ").split(",") if x.strip()]
    tong_chan = sum(so for so in danh_sach if so % 2 == 0)
    print("Tổng các số chẵn:", tong_chan)


if __name__ == "__main__":
    main()
