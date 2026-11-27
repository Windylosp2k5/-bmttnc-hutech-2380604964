"""Các thao tác quản lý danh sách sinh viên."""

try:
    from .SinhVien import SinhVien
except ImportError:  # Cho phép chạy Main.py trực tiếp trong VS Code.
    from SinhVien import SinhVien


class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []

    def them(self, ten, gioi_tinh, chuyen_nganh, diem):
        sinh_vien = SinhVien(ten, gioi_tinh, chuyen_nganh, diem)
        self.danh_sach.append(sinh_vien)
        return sinh_vien

    def tim_theo_id(self, ma_id):
        return next((sv for sv in self.danh_sach if sv.id == ma_id), None)

    def cap_nhat(self, ma_id, ten, gioi_tinh, chuyen_nganh, diem):
        sinh_vien = self.tim_theo_id(ma_id)
        if sinh_vien is None:
            return False
        sinh_vien.ten = ten.strip()
        sinh_vien.gioi_tinh = gioi_tinh.strip()
        sinh_vien.chuyen_nganh = chuyen_nganh.strip()
        sinh_vien.diem_trung_binh = float(diem)
        return True

    def xoa(self, ma_id):
        sinh_vien = self.tim_theo_id(ma_id)
        if sinh_vien is None:
            return False
        self.danh_sach.remove(sinh_vien)
        return True

    def tim_theo_ten(self, tu_khoa):
        tu_khoa = tu_khoa.casefold().strip()
        return [sv for sv in self.danh_sach if tu_khoa in sv.ten.casefold()]

    def sap_xep_theo_diem(self):
        return sorted(self.danh_sach, key=lambda sv: sv.diem_trung_binh, reverse=True)

    def sap_xep_theo_chuyen_nganh(self):
        return sorted(self.danh_sach, key=lambda sv: sv.chuyen_nganh.casefold())

    def hien_thi(self, danh_sach=None):
        danh_sach = self.danh_sach if danh_sach is None else danh_sach
        if not danh_sach:
            print("Danh sách sinh viên đang trống.")
            return
        print(f"{'ID':<4} {'Họ tên':<24} {'Giới tính':<12} {'Chuyên ngành':<22} {'Điểm TB':<8} Học lực")
        print("-" * 88)
        for sinh_vien in danh_sach:
            print(sinh_vien)
