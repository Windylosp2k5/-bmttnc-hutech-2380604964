"""Câu 01 - Nhập họ tên, tuổi và in lời chào."""


def main():
    ho_ten = input("Nhập họ tên của bạn: ").strip()
    tuoi = input("Nhập tuổi của bạn: ").strip()

    print(f"Xin chào {ho_ten}, bạn {tuoi} tuổi. Chúc bạn học Python vui vẻ!")


if __name__ == "__main__":
    main()
