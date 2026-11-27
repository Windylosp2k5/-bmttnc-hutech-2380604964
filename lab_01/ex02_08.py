"""Câu 08 - Lọc các số nhị phân 4 chữ số chia hết cho 5."""


def main():
    dau_vao = input("Nhập các số nhị phân 4 chữ số, cách nhau bởi dấu phẩy: ")
    cac_so = [so.strip().strip("'\" ") for so in dau_vao.split(",")]
    hop_le = []

    for so in cac_so:
        if len(so) != 4 or any(ky_tu not in "01" for ky_tu in so):
            print(f"Bỏ qua giá trị không hợp lệ: {so}")
            continue
        if int(so, 2) % 5 == 0:
            hop_le.append(so)

    print(",".join(hop_le))


if __name__ == "__main__":
    main()
