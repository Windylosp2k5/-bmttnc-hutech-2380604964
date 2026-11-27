"""Câu 09 - Hàm kiểm tra số nguyên tố."""


def la_so_nguyen_to(so):
    if so < 2:
        return False
    uoc = 2
    while uoc * uoc <= so:
        if so % uoc == 0:
            return False
        uoc += 1
    return True


def main():
    so = int(input("Nhập một số nguyên: "))
    if la_so_nguyen_to(so):
        print(f"{so} là số nguyên tố.")
    else:
        print(f"{so} không phải là số nguyên tố.")


if __name__ == "__main__":
    main()
