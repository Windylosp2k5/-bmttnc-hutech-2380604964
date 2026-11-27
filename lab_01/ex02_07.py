"""Câu 07 - Đổi từng dòng nhập vào thành chữ hoa (Enter trên dòng trống để dừng)."""


def main():
    print("Nhập các dòng văn bản; nhấn Enter trên dòng trống để kết thúc:")
    cac_dong = []
    while True:
        dong = input()
        if dong == "":
            break
        cac_dong.append(dong.upper())

    print("Kết quả:")
    for dong in cac_dong:
        print(dong)


if __name__ == "__main__":
    main()
