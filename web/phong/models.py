from django.db import models
from startScan.models import *
from dashboard.models import Project
from recon_note.models import *

# Phong model (Department)
class Phong(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255)
    phan_cap = models.CharField(max_length=100)
    mo_ta = models.TextField()

    def __str__(self):
        return self.ten


# BoPhan model (Division)
class BoPhan(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255)
    mo_ta = models.TextField()
    phong = models.ForeignKey(Phong, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.ten

# NhomQuyen model
class NhomQuyen(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)

    def __str__(self):
        return self.ten

# NguoiDung model (User)
class NguoiDung(models.Model):
    id = models.AutoField(primary_key=True)
    ten_nguoi_dung = models.CharField(max_length=255, null=True)
    mat_khau = models.CharField(max_length=255, null=True)
    ghi_chu = models.CharField(max_length=255, null=True)
    trang_thai = models.CharField(max_length=255)
    id_NhomQuyen = models.ForeignKey(NhomQuyen, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten_nguoi_dung

class ChucVu(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)

    def __str__(self):
        return self.ten

# NhanVien model (Employee)
class NhanVien(models.Model):
    id = models.AutoField(primary_key=True)
    ho_ten = models.CharField(max_length=255)
    mo_ta = models.TextField()
    chuc_vu = models.ForeignKey(ChucVu, on_delete=models.CASCADE)
    bo_phan = models.ForeignKey(BoPhan, on_delete=models.CASCADE, null=True, blank=True)
    nguoi_dung = models.ForeignKey(NguoiDung, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.ho_ten

class DuAn(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)
    bo_phan = models.ForeignKey(BoPhan, on_delete=models.CASCADE, null=True, blank=True)
    phong = models.ForeignKey(Phong, on_delete=models.CASCADE, null=True, blank=True)
    nhan_vien_lap = models.ForeignKey(NhanVien, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.ten

class PhienBanDuAn(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)
    du_an = models.ForeignKey(DuAn, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

class DauViec(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)
    ngay_lap = models.DateTimeField(null=True)
    id_NguoiLap = models.ForeignKey(NhanVien, on_delete=models.CASCADE)
    # con nua

    def __str__(self):
        return self.ten

class PhanCong(models.Model):
    id = models.AutoField(primary_key=True)
    vai_tro = models.CharField(max_length=255, null=True)
    id_NguoiLap = models.ForeignKey(NhanVien, on_delete=models.CASCADE)
    id_DauViec = models.ForeignKey(DauViec, on_delete=models.CASCADE)

class LoaiQuyTrinh(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)

    def __str__(self):
        return self.ten

class QuyTrinh(models.Model):
    id = models.AutoField(primary_key=True)
    ten_quy_trinh = models.CharField(max_length=255, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)
    is_phe_duyet = models.BooleanField(default=False)
    is_chia_se = models.BooleanField(default=False)
    loai_quy_trinh = models.ForeignKey(LoaiQuyTrinh, on_delete=models.CASCADE, null=True, blank=True)
    nguoi_duyet = models.ForeignKey(NhanVien, on_delete=models.CASCADE, null=True, blank=True)
    phong = models.ForeignKey(Phong, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.ten_quy_trinh

class QuyTrinhPhienBan(models.Model):
    id = models.AutoField(primary_key=True)
    quy_trinh = models.ForeignKey(QuyTrinh, on_delete=models.CASCADE)
    phien_ban = models.ForeignKey(PhienBanDuAn, on_delete=models.CASCADE)
    trang_thai_danh_gia = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return f"{self.quy_trinh} - {self.phien_ban}"

class DoiTuongDanhGia(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)
    tai_lieu = models.CharField(null=True, blank=True, max_length=1000)

    def __str__(self):
        return self.ten

class Buoc(models.Model):
    id = models.AutoField(primary_key=True)
    ten_buoc = models.CharField(max_length=100)
    thu_tu = models.IntegerField(blank=True, null=True)
    tai_lieu_mo_ta = models.CharField(null=True, blank=True, max_length=255)
    yeu_cau = models.CharField(null=True, blank=True, max_length=255)
    id_DoiTuong = models.ForeignKey(DoiTuongDanhGia, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten_buoc

class QuyTrinhBuoc(models.Model):
    id = models.AutoField(primary_key=True)
    id_QuyTrinh = models.ForeignKey(QuyTrinh, on_delete=models.CASCADE)
    id_Buoc = models.ForeignKey(Buoc, on_delete=models.CASCADE)

class CongCu(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)

    def __str__(self):
        return self.ten

class BuocCongCu(models.Model):
    id = models.AutoField(primary_key=True)
    id_CongCu = models.ForeignKey(CongCu, on_delete=models.CASCADE)
    id_Buoc = models.ForeignKey(Buoc, on_delete=models.CASCADE)

class NhomBuoc(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)
    id_PhanCong = models.ForeignKey(PhanCong, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

class ChiTietNhomBuoc(models.Model):
    id = models.AutoField(primary_key=True)
    id_Buoc = models.ForeignKey(Buoc, on_delete=models.CASCADE)
    id_NhomBuoc = models.ForeignKey(NhomBuoc, on_delete=models.CASCADE)

class MauKichBan(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)
    tai_lieu = models.CharField(null=True, blank=True, max_length=1000)
    id_NguoiLap = models.ForeignKey(NhanVien, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

class KichBan(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)
    tai_lieu = models.CharField(null=True, blank=True, max_length=1000)
    id_QuyTrinhPhienBan = models.ForeignKey(QuyTrinhPhienBan, on_delete=models.CASCADE)
    id_MauKichBan = models.ForeignKey(MauKichBan, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

class ChiTietKichBan(models.Model):
    id = models.AutoField(primary_key=True)
    tai_lieu = models.CharField(null=True, blank=True, max_length=1000)
    kich_ban = models.ForeignKey(KichBan, on_delete=models.CASCADE)
    buoc = models.ForeignKey(Buoc, on_delete=models.CASCADE)

class ChiTietMauKichBan(models.Model):
    id = models.AutoField(primary_key=True)
    tai_lieu = models.CharField(null=True, blank=True, max_length=1000)
    mau_kich_ban = models.ForeignKey(MauKichBan, on_delete=models.CASCADE)
    buoc = models.ForeignKey(Buoc, on_delete=models.CASCADE)

# NgheNghiep model (Profession)
class NgheNghiep(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255)
    mo_ta = models.TextField()

    def __str__(self):
        return self.ten


# ChuyenGia model (Expert)
class ChuyenGia(models.Model):
    id = models.AutoField(primary_key=True)
    so_hieu_cg = models.CharField(max_length=255)
    ten = models.CharField(max_length=255)
    don_vi_cong_tac = models.CharField(max_length=255)
    bang_cap = models.CharField(max_length=255)
    mo_ta = models.TextField()
    phong = models.ForeignKey(Phong, on_delete=models.CASCADE, null=True, blank=True)
    nguoi_dung = models.ForeignKey(NguoiDung, on_delete=models.CASCADE, null=True, blank=True)
    nghe_nghiep = models.ForeignKey(NgheNghiep, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return { "so_hieu_cg": self.so_hieu_cg, "ten": self.ten, "don_vi_cong_tac": self.don_vi_cong_tac }


# PhanTich model (Analysis)
class PhanTich(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255)
    tai_lieu = models.TextField()
    mo_ta = models.TextField()
    chuyen_gia = models.ForeignKey(ChuyenGia, on_delete=models.CASCADE, null=True, blank=True)
    chi_tiet_dau_viec = models.TextField()

    def __str__(self):
        return self.ten


# BaoCao model (Report)
class BaoCao(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)
    tai_lieu = models.CharField(null=True, blank=True, max_length=1000)
    trang_thai = models.CharField(null=True, max_length=255)
    id_NguoiLap = models.ForeignKey(NhanVien, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

class BuocBaoCao(models.Model):
    id = models.AutoField(primary_key=True)
    id_NguoiLap = models.ForeignKey(NhanVien, on_delete=models.CASCADE)
    buoc = models.ForeignKey(Buoc, on_delete=models.CASCADE)
    bao_cao = models.ForeignKey(BaoCao, on_delete=models.CASCADE)

class MayTinhKetNoi(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255, null=True, blank=True)
    ip = models.CharField(max_length=15, null=True, blank=True)
    mac = models.CharField(max_length=17, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)
    khoa = models.CharField(max_length=255, null=True, blank=True)
    ngay_het_han_khoa = models.DateTimeField(null=True, blank=True)
    phong = models.ForeignKey(Phong, on_delete=models.CASCADE)
    chu_so_huu = models.ForeignKey(NhanVien, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

class NhomChiaSe(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)
    id_NguoiLap = models.ForeignKey(NhanVien, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

class NhomChiaSeBaoCao(models.Model):
    id = models.AutoField(primary_key=True)
    nguoi_chia_se = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
    nhom_chia_se = models.ForeignKey(NhomChiaSe, on_delete=models.CASCADE)
    bao_cao = models.ForeignKey(BaoCao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nhom_chia_se} - {self.bao_cao}"

class MayTinhNhomChiaSe(models.Model):
    id = models.AutoField(primary_key=True)
    may_tinh = models.ForeignKey(MayTinhKetNoi, on_delete=models.CASCADE)
    nhom_chia_se = models.ForeignKey(NhomChiaSe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.may_tinh} - {self.nhom_chia_se}"

class NhomNhanBaoCao(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255)
    mo_ta = models.TextField()

    def __str__(self):
        return self.ten

class MayTinhNhomNhan(models.Model):
    id = models.AutoField(primary_key=True)
    may_tinh = models.ForeignKey(MayTinhKetNoi, on_delete=models.CASCADE)
    nhom_nhan = models.ForeignKey(NhomNhanBaoCao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.may_tinh} - {self.nhom_nhan}"

class NhomNhanBaoCaoBaoCao(models.Model):
    id = models.AutoField(primary_key=True)
    nhom_nhan = models.ForeignKey(NhomNhanBaoCao, on_delete=models.CASCADE)
    bao_cao = models.ForeignKey(BaoCao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nhom_nhan} - {self.bao_cao}"

class LoaiRuiRo(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)
    the = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.ten

class RuiRo(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)
    nguoi_lap = models.ForeignKey(NhanVien, on_delete=models.CASCADE)
    loai_rui_ro = models.ForeignKey(LoaiRuiRo, on_delete=models.CASCADE)
    du_an = models.ForeignKey(DuAn, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

class LoaiXuLy(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ten

class XuLyRuiRo(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)
    loai_xu_ly = models.ForeignKey(LoaiXuLy, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

class RuiRoXuLy(models.Model):
    id = models.AutoField(primary_key=True)
    ngay_lap = models.DateTimeField(null=True, blank=True)
    nguoi_lap = models.ForeignKey(NhanVien, on_delete=models.CASCADE)
    rui_ro = models.ForeignKey(RuiRo, on_delete=models.CASCADE)
    xu_ly = models.ForeignKey(XuLyRuiRo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rui_ro} - {self.xu_ly}"

class BuocXuLy(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)
    thu_tu = models.IntegerField(null=True, blank=True)
    xu_ly = models.ForeignKey(XuLyRuiRo, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

class GhiChu(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)
    xu_ly = models.ForeignKey(XuLyRuiRo, on_delete=models.CASCADE)
    nguoi_lap = models.ForeignKey(NhanVien, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten