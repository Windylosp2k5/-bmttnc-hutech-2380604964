"""Câu 04 - In phần tử đầu tiên và cuối cùng của Tuple."""


def main():
    bo_tuple = tuple(x.strip() for x in input("Nhập các phần tử, cách nhau bởi dấu phẩy: ").split(",") if x.strip())
    if not bo_tuple:
        print("Tuple rỗng, không có phần tử đầu/cuối.")
        return
    print("Phần tử đầu tiên:", bo_tuple[0])
    print("Phần tử cuối cùng:", bo_tuple[-1])


if __name__ == "__main__":
    main()
