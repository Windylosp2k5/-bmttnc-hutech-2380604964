"""Câu 02 - Tính diện tích hình tròn với Pi = 3.14."""


def main():
    ban_kinh = float(input("Nhập bán kính hình tròn: "))
    pi = 3.14
    dien_tich = pi * ban_kinh**2

    print(f"Diện tích hình tròn là: {dien_tich:.2f}")


if __name__ == "__main__":
    main()
