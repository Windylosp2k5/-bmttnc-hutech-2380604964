"""Lớp biểu diễn một sinh viên."""


class SinhVien:
    _id_tiep_theo = 1

    def __init__(self, ten, gioi_tinh, chuyen_nganh, diem_trung_binh):
        self.id = SinhVien._id_tiep_theo
        SinhVien._id_tiep_theo += 1
        self.ten = ten.strip()
        self.gioi_tinh = gioi_tinh.strip()
        self.chuyen_nganh = chuyen_nganh.strip()
        self.diem_trung_binh = float(diem_trung_binh)

    @property
    def hoc_luc(self):
        if self.diem_trung_binh >= 8:
            return "Giỏi"
        if self.diem_trung_binh >= 6.5:
            return "Khá"
        if self.diem_trung_binh >= 5:
            return "Trung bình"
        return "Yếu"

    def __str__(self):
        return (f"{self.id:<4} {self.ten:<24} {self.gioi_tinh:<12} "
                f"{self.chuyen_nganh:<22} {self.diem_trung_binh:<8.2f} {self.hoc_luc}")
