"""Câu 03 - Kiểm tra số chẵn."""


def main():
    so = int(input("Nhập một số nguyên: "))
    if so % 2 == 0:
        print(f"{so} là số chẵn.")
    else:
        print(f"{so} là số lẻ.")


if __name__ == "__main__":
    main()
