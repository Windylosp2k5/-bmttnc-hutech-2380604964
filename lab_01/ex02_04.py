"""Câu 04 - Liệt kê số chia hết cho 7 nhưng không chia hết cho 5."""


def main():
    cac_so = [str(so) for so in range(2000, 3201)
              if so % 7 == 0 and so % 5 != 0]
    print(",".join(cac_so))


if __name__ == "__main__":
    main()
