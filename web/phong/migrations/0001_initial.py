# Generated by Django 3.2.23 on 2024-10-11 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaoCao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=100)),
                ('mo_ta', models.TextField(blank=True)),
                ('tai_lieu', models.CharField(blank=True, max_length=1000, null=True)),
                ('trang_thai', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoPhan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=255)),
                ('mo_ta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Buoc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten_buoc', models.CharField(max_length=100)),
                ('thu_tu', models.IntegerField(blank=True, null=True)),
                ('tai_lieu_mo_ta', models.CharField(blank=True, max_length=255, null=True)),
                ('yeu_cau', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChucVu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=100)),
                ('mo_ta', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChuyenGia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('so_hieu_cg', models.CharField(max_length=255)),
                ('ten', models.CharField(max_length=255)),
                ('don_vi_cong_tac', models.CharField(max_length=255)),
                ('bang_cap', models.CharField(max_length=255)),
                ('mo_ta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CongCu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=100)),
                ('mo_ta', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DauViec',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=100)),
                ('mo_ta', models.TextField(blank=True)),
                ('ngay_lap', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DoiTuongDanhGia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=100)),
                ('mo_ta', models.TextField(blank=True)),
                ('tai_lieu', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DuAn',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('mo_ta', models.TextField(blank=True, null=True)),
                ('bo_phan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phong.bophan')),
            ],
        ),
        migrations.CreateModel(
            name='LoaiQuyTrinh',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=100)),
                ('mo_ta', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoaiRuiRo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('mo_ta', models.TextField(blank=True, null=True)),
                ('the', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoaiXuLy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('mo_ta', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MayTinhKetNoi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('ip', models.CharField(blank=True, max_length=15, null=True)),
                ('mac', models.CharField(blank=True, max_length=17, null=True)),
                ('mo_ta', models.TextField(blank=True, null=True)),
                ('khoa', models.CharField(blank=True, max_length=255, null=True)),
                ('ngay_het_han_khoa', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NgheNghiep',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=255)),
                ('mo_ta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NguoiDung',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten_nguoi_dung', models.CharField(max_length=255, null=True)),
                ('mat_khau', models.CharField(max_length=255, null=True)),
                ('ghi_chu', models.CharField(max_length=255, null=True)),
                ('trang_thai', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NhomChiaSe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=100)),
                ('mo_ta', models.TextField(blank=True)),
                ('id_NguoiLap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung')),
            ],
        ),
        migrations.CreateModel(
            name='NhomNhanBaoCao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=255)),
                ('mo_ta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NhomQuyen',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=100)),
                ('mo_ta', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhienBanDuAn',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('mo_ta', models.TextField(blank=True, null=True)),
                ('du_an', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.duan')),
            ],
        ),
        migrations.CreateModel(
            name='Phong',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=255)),
                ('phan_cap', models.CharField(max_length=100)),
                ('mo_ta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QuyTrinh',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten_quy_trinh', models.CharField(blank=True, max_length=255, null=True)),
                ('mo_ta', models.TextField(blank=True, null=True)),
                ('is_phe_duyet', models.BooleanField(default=False)),
                ('is_chia_se', models.BooleanField(default=False)),
                ('loai_quy_trinh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phong.loaiquytrinh')),
                ('nguoi_duyet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung')),
                ('phong', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phong.phong')),
            ],
        ),
        migrations.CreateModel(
            name='RuiRo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('mo_ta', models.TextField(blank=True, null=True)),
                ('du_an', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.duan')),
                ('loai_rui_ro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.loairuiro')),
                ('nguoi_lap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung')),
            ],
        ),
        migrations.CreateModel(
            name='XuLyRuiRo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('mo_ta', models.TextField(blank=True, null=True)),
                ('loai_xu_ly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.loaixuly')),
            ],
        ),
        migrations.CreateModel(
            name='RuiRoXuLy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ngay_lap', models.DateTimeField(blank=True, null=True)),
                ('nguoi_lap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung')),
                ('rui_ro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.ruiro')),
                ('xu_ly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.xulyruiro')),
            ],
        ),
        migrations.CreateModel(
            name='QuyTrinhPhienBan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trang_thai_danh_gia', models.CharField(blank=True, max_length=255, null=True)),
                ('phien_ban', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.phienbanduan')),
                ('quy_trinh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.quytrinh')),
            ],
        ),
        migrations.CreateModel(
            name='QuyTrinhBuoc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_Buoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.buoc')),
                ('id_QuyTrinh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.quytrinh')),
            ],
        ),
        migrations.CreateModel(
            name='PhanTich',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=255)),
                ('tai_lieu', models.TextField()),
                ('mo_ta', models.TextField()),
                ('chi_tiet_dau_viec', models.TextField()),
                ('chuyen_gia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phong.chuyengia')),
            ],
        ),
        migrations.CreateModel(
            name='PhanCong',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vai_tro', models.CharField(max_length=255, null=True)),
                ('id_DauViec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.dauviec')),
                ('id_NguoiLap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung')),
            ],
        ),
        migrations.CreateModel(
            name='NhomNhanBaoCaoBaoCao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bao_cao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.baocao')),
                ('nhom_nhan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nhomnhanbaocao')),
            ],
        ),
        migrations.CreateModel(
            name='NhomChiaSeBaoCao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bao_cao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.baocao')),
                ('nguoi_chia_se', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung')),
                ('nhom_chia_se', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nhomchiase')),
            ],
        ),
        migrations.CreateModel(
            name='NhomBuoc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=100)),
                ('mo_ta', models.TextField(blank=True)),
                ('id_PhanCong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.phancong')),
            ],
        ),
        migrations.CreateModel(
            name='NhanVien',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ho_ten', models.CharField(max_length=255)),
                ('mo_ta', models.TextField()),
                ('bo_phan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phong.bophan')),
                ('chuc_vu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.chucvu')),
                ('nguoi_dung', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung')),
            ],
        ),
        migrations.AddField(
            model_name='nguoidung',
            name='id_NhomQuyen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nhomquyen'),
        ),
        migrations.CreateModel(
            name='MayTinhNhomNhan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('may_tinh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.maytinhketnoi')),
                ('nhom_nhan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nhomnhanbaocao')),
            ],
        ),
        migrations.CreateModel(
            name='MayTinhNhomChiaSe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('may_tinh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.maytinhketnoi')),
                ('nhom_chia_se', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nhomchiase')),
            ],
        ),
        migrations.AddField(
            model_name='maytinhketnoi',
            name='chu_so_huu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung'),
        ),
        migrations.AddField(
            model_name='maytinhketnoi',
            name='phong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.phong'),
        ),
        migrations.CreateModel(
            name='MauKichBan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=100)),
                ('mo_ta', models.TextField(blank=True)),
                ('tai_lieu', models.CharField(blank=True, max_length=1000, null=True)),
                ('id_NguoiLap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung')),
            ],
        ),
        migrations.CreateModel(
            name='KichBan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(max_length=100)),
                ('mo_ta', models.TextField(blank=True)),
                ('tai_lieu', models.CharField(blank=True, max_length=1000, null=True)),
                ('id_MauKichBan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.maukichban')),
                ('id_QuyTrinhPhienBan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.quytrinhphienban')),
            ],
        ),
        migrations.CreateModel(
            name='GhiChu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('mo_ta', models.TextField(blank=True, null=True)),
                ('nguoi_lap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung')),
                ('xu_ly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.xulyruiro')),
            ],
        ),
        migrations.AddField(
            model_name='duan',
            name='nhan_vien_lap',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung'),
        ),
        migrations.AddField(
            model_name='duan',
            name='phong',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phong.phong'),
        ),
        migrations.AddField(
            model_name='dauviec',
            name='id_NguoiLap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung'),
        ),
        migrations.AddField(
            model_name='chuyengia',
            name='nghe_nghiep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phong.nghenghiep'),
        ),
        migrations.AddField(
            model_name='chuyengia',
            name='nguoi_dung',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung'),
        ),
        migrations.AddField(
            model_name='chuyengia',
            name='phong',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phong.phong'),
        ),
        migrations.CreateModel(
            name='ChiTietNhomBuoc',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_Buoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.buoc')),
                ('id_NhomBuoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nhombuoc')),
            ],
        ),
        migrations.CreateModel(
            name='ChiTietMauKichBan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tai_lieu', models.CharField(blank=True, max_length=1000, null=True)),
                ('buoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.buoc')),
                ('mau_kich_ban', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.maukichban')),
            ],
        ),
        migrations.CreateModel(
            name='ChiTietKichBan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tai_lieu', models.CharField(blank=True, max_length=1000, null=True)),
                ('buoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.buoc')),
                ('kich_ban', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.kichban')),
            ],
        ),
        migrations.CreateModel(
            name='BuocXuLy',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ten', models.CharField(blank=True, max_length=255, null=True)),
                ('mo_ta', models.TextField(blank=True, null=True)),
                ('thu_tu', models.IntegerField(blank=True, null=True)),
                ('xu_ly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.xulyruiro')),
            ],
        ),
        migrations.CreateModel(
            name='BuocCongCu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_Buoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.buoc')),
                ('id_CongCu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.congcu')),
            ],
        ),
        migrations.CreateModel(
            name='BuocBaoCao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bao_cao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.baocao')),
                ('buoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.buoc')),
                ('id_NguoiLap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung')),
            ],
        ),
        migrations.AddField(
            model_name='buoc',
            name='id_DoiTuong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.doituongdanhgia'),
        ),
        migrations.AddField(
            model_name='bophan',
            name='phong',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phong.phong'),
        ),
        migrations.AddField(
            model_name='baocao',
            name='id_NguoiLap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phong.nguoidung'),
        ),
    ]
