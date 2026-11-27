"""Câu 06 - Tạo ma trận với phần tử ở hàng i, cột j bằng i * j."""


def main():
    x = int(input("Nhập X (số hàng): "))
    y = int(input("Nhập Y (số cột): "))
    if x < 0 or y < 0:
        print("X và Y phải không âm.")
        return

    ma_tran = [[i * j for j in range(y)] for i in range(x)]
    print(ma_tran)


if __name__ == "__main__":
    main()
