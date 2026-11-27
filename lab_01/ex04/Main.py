"""Menu chạy chương trình quản lý sinh viên."""

try:
    from .QuanLySinhVien import QuanLySinhVien
except ImportError:  # Cho phép nhấn Run Python File trên Main.py.
    from QuanLySinhVien import QuanLySinhVien


def nhap_diem():
    while True:
        try:
            diem = float(input("Điểm trung bình (0-10): "))
            if 0 <= diem <= 10:
                return diem
            print("Điểm phải nằm trong khoảng 0 đến 10.")
        except ValueError:
            print("Vui lòng nhập một số.")


def nhap_id():
    while True:
        try:
            return int(input("Mã sinh viên (ID): "))
        except ValueError:
            print("ID phải là số nguyên.")


def main():
    quan_ly = QuanLySinhVien()
    while True:
        print("\n=== QUẢN LÝ SINH VIÊN ===")
        print("1. Thêm sinh viên")
        print("2. Cập nhật sinh viên theo ID")
        print("3. Xóa sinh viên theo ID")
        print("4. Tìm sinh viên theo tên")
        print("5. Sắp xếp theo điểm trung bình")
        print("6. Sắp xếp theo chuyên ngành")
        print("7. Hiển thị danh sách")
        print("0. Thoát")
        lua_chon = input("Chọn chức năng: ").strip()

        if lua_chon == "1":
            ten = input("Họ tên: ")
            gioi_tinh = input("Giới tính: ")
            chuyen_nganh = input("Chuyên ngành: ")
            sinh_vien = quan_ly.them(ten, gioi_tinh, chuyen_nganh, nhap_diem())
            print(f"Đã thêm sinh viên với ID {sinh_vien.id}.")
        elif lua_chon == "2":
            ma_id = nhap_id()
            if quan_ly.tim_theo_id(ma_id) is None:
                print("Không tìm thấy sinh viên.")
                continue
            ten = input("Họ tên mới: ")
            gioi_tinh = input("Giới tính mới: ")
            chuyen_nganh = input("Chuyên ngành mới: ")
            diem = nhap_diem()
            quan_ly.cap_nhat(ma_id, ten, gioi_tinh, chuyen_nganh, diem)
            print("Đã cập nhật thông tin.")
        elif lua_chon == "3":
            if quan_ly.xoa(nhap_id()):
                print("Đã xóa sinh viên.")
            else:
                print("Không tìm thấy sinh viên.")
        elif lua_chon == "4":
            quan_ly.hien_thi(quan_ly.tim_theo_ten(input("Nhập tên cần tìm: ")))
        elif lua_chon == "5":
            quan_ly.hien_thi(quan_ly.sap_xep_theo_diem())
        elif lua_chon == "6":
            quan_ly.hien_thi(quan_ly.sap_xep_theo_chuyen_nganh())
        elif lua_chon == "7":
            quan_ly.hien_thi()
        elif lua_chon == "0":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy chọn lại.")


if __name__ == "__main__":
    main()
