"""Câu 05 - Tính lương tuần, giờ làm thêm được trả 150%."""


def main():
    so_gio = float(input("Nhập số giờ làm trong tuần: "))
    luong_gio = float(input("Nhập mức lương tiêu chuẩn mỗi giờ: "))
    if so_gio < 0 or luong_gio < 0:
        print("Số giờ và mức lương không được âm.")
        return

    gio_tieu_chuan = min(so_gio, 44)
    gio_lam_them = max(so_gio - 44, 0)
    tien_luong = gio_tieu_chuan * luong_gio + gio_lam_them * luong_gio * 1.5
    print(f"Lương thực nhận: {tien_luong:,.2f}")
    print(f"Trong đó: {gio_tieu_chuan:g} giờ tiêu chuẩn, {gio_lam_them:g} giờ làm thêm.")


if __name__ == "__main__":
    main()
