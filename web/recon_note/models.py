from django.db import models
from startScan.models import *
from dashboard.models import Project
from phong.models import *

class TodoNote(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    scan_history = models.ForeignKey(
        ScanHistory,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    subdomain = models.ForeignKey(
        Subdomain,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    is_done = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class NguonLoHong(models.Model):
    id = models.AutoField(primary_key=True)
    ten_nguon = models.CharField(max_length=255)
    ky_hieu = models.CharField(max_length=50)
    mo_ta = models.TextField(null=True, blank=True)
    duong_dan = models.URLField(max_length=300)

    def __str__(self):
        return self.ten_nguon

class LoaiLoHong(models.Model):
    id = models.AutoField(primary_key=True)
    ten_loai = models.CharField(max_length=255)
    mo_ta = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ten_loai

class BienPhap(models.Model):
    id = models.AutoField(primary_key=True)
    ten_bien_phap = models.CharField(max_length=255)
    mo_ta = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ten_bien_phap

class LoHong(models.Model):
    id = models.AutoField(primary_key=True)
    ten_lo_hong = models.CharField(max_length=255)
    mo_ta = models.TextField(null=True, blank=True)
    muc_do = models.CharField(max_length=255)
    id_LoaiLoHong = models.ForeignKey(LoaiLoHong, on_delete=models.CASCADE)
    id_NguonLoHong = models.ForeignKey(NguonLoHong, on_delete=models.CASCADE)
    id_BienPhap = models.ForeignKey(BienPhap, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten_lo_hong

class LoaiBienPhap(models.Model):
    id = models.AutoField(primary_key=True)
    ten_loai_bien_phap = models.CharField(max_length=255)
    mo_ta = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ten_loai_bien_phap

class ChiTietBienPhap(models.Model):
    id = models.AutoField(primary_key=True)
    ten_loai_bien_phap = models.CharField(max_length=255)
    mo_ta = models.TextField(null=True, blank=True)
    tai_lieu = models.CharField(max_length=2000, blank=True)
    id_NguoiLap = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
    id_BienPhap = models.ForeignKey(BienPhap, on_delete=models.CASCADE)
    id_LoaiBienPhap = models.ForeignKey(LoaiBienPhap, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten_loai_bien_phap

class GiaiDoanPhatTrien(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)

    def __str__(self):
        return self.ten

class PhienBanGiaiDoan(models.Model):
    id = models.AutoField(primary_key=True)
    phien_ban = models.ForeignKey(PhienBanDuAn, on_delete=models.CASCADE)
    giai_doan = models.ForeignKey(GiaiDoanPhatTrien, on_delete=models.CASCADE)
    mo_ta = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.phien_ban} - {self.giai_doan}"

class PhienBanThietKe(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)
    so_phien_ban = models.CharField(max_length=50, null=True, blank=True)
    trang_thai = models.CharField(max_length=255, null=True, blank=True)
    du_an = models.ForeignKey(DuAn, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

class NenTangPhatTrien(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=100)
    mo_ta = models.TextField(blank=True)

    def __str__(self):
        return self.ten

class DuAnNenTang(models.Model):
    id = models.AutoField(primary_key=True)
    mo_ta = models.TextField(null=True, blank=True)
    ghi_chu = models.CharField(null=True, blank=True, max_length=255)
    thuoc_bo_tieu_chuan = models.CharField(null=True, max_length=1000)
    du_an = models.ForeignKey(DuAn, on_delete=models.CASCADE)
    nen_tang = models.ForeignKey(NenTangPhatTrien, on_delete=models.CASCADE)

class HoSoPhanMem(models.Model):
    id = models.AutoField(primary_key=True)
    nguoi_them = models.CharField(max_length=100)
    phien_ban = models.CharField(max_length=50)
    giai_doan = models.ForeignKey(GiaiDoanPhatTrien, on_delete=models.CASCADE)
    nen_tang = models.ForeignKey(NenTangPhatTrien, on_delete=models.CASCADE)
    mo_ta = models.TextField(blank=True)
    tai_lieu = models.FileField(upload_to='file_upload/', blank=True)  # FileField for file uploads

    def __str__(self):
        return f"{self.nguoi_them} - {self.phien_ban}"

class HoSoThietKe(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)
    phien_ban_thiet_ke = models.ForeignKey(PhienBanThietKe, on_delete=models.CASCADE)
    nguoi_tai_len = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten

class TaiLieuThietKe(models.Model):
    id = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=255, null=True, blank=True)
    mo_ta = models.TextField(null=True, blank=True)
    duong_dan = models.CharField(max_length=255, null=True, blank=True)
    trang_thai = models.CharField(max_length=255, null=True, blank=True)
    phien_ban_thiet_ke = models.ForeignKey(PhienBanThietKe, on_delete=models.CASCADE)

    def __str__(self):
        return self.ten