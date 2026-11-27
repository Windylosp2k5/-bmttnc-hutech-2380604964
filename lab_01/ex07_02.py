"""Bài tập mở rộng 02 - Cộng riêng các số nguyên dương và âm trong chuỗi."""

import re


def tinh_tong_so_duong_am(chuoi):
    cac_so = [int(so) for so in re.findall(r"[+-]?\d+", chuoi)]
    tong_duong = sum(so for so in cac_so if so > 0)
    tong_am = sum(so for so in cac_so if so < 0)
    return tong_duong, tong_am


def main():
    chuoi = input("Nhập chuỗi có chứa các số nguyên: ")
    tong_duong, tong_am = tinh_tong_so_duong_am(chuoi)
    print(f"Giá trị dương: {tong_duong}")
    print(f"Giá trị âm: {tong_am}")


if __name__ == "__main__":
    main()
