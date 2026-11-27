"""Câu 10 - Hàm trả về chuỗi đảo ngược."""


def dao_nguoc(chuoi):
    return chuoi[::-1]


def main():
    chuoi = input("Nhập một chuỗi: ")
    print("Chuỗi đảo ngược:", dao_nguoc(chuoi))


if __name__ == "__main__":
    main()
