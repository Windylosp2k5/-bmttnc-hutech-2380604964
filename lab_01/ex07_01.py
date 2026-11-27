"""Bài tập mở rộng 01 - In tất cả hoán vị của [1, 2, 3]."""

from itertools import permutations


def main():
    danh_sach = [1, 2, 3]
    for hoan_vi in permutations(danh_sach):
        print(hoan_vi)


if __name__ == "__main__":
    main()
