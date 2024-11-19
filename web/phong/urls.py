from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('<slug:slug>/agent/', views.agent_receive, name='agent_receive'),
    path('get_bophan_by_phong/', views.get_bophan_by_phong, name='get_bophan_by_phong'),
    path('get_bophan_by_phong_number/', views.get_bophan_by_phong_number, name='get_bophan_by_phong_number'),
    path('get_nhanvien_by_bophan/', views.get_nhanvien_by_bophan, name='get_nhanvien_by_bophan'),
    path('get-nhanvien-by-phong/', views.get_nhanvien_by_phong, name='get_nhanvien_by_phong'),
    path(
        '<slug:slug>/chuyengia',
        views.chuyengia,
        name='chuyengia'),
    path(
        '<slug:slug>/themmaytinhchiasebaocao',
        views.themmaytinhchiasebaocao,
        name='themmaytinhchiasebaocao'),
    path(
        '<slug:slug>/danhsachnhomchiasebaocao',
        views.danhsachnhomchiasebaocao,
        name='danhsachnhomchiasebaocao'),
    path(
        '<slug:slug>/danhsachnhomnhanbaocao',
        views.danhsachnhomnhanbaocao,
        name='danhsachnhomnhanbaocao'),
    path(
        '<slug:slug>/chonnhomchiase',
        views.chonnhomchiase,
        name='chonnhomchiase'),
    path(
        '<slug:slug>/themchuyengia',
        views.themchuyengia,
        name='themchuyengia'),
    path(
        '<slug:slug>/danhsachchuyengia',
        views.danhsachchuyengia,
        name='danhsachchuyengia'),
    path(
        '<slug:slug>/dangkyhotro',
        views.dangkyhotro,
        name='dangkyhotro'),
    path(
        '<slug:slug>/themruiro',
        views.themruiro,
        name='themruiro'),
    path(
        '<slug:slug>/quanlyruiro',
        views.quanlyruiro,
        name='quanlyruiro'),
    path(
        '<slug:slug>/themnhanvien',
        views.themnhanvien,
        name='themnhanvien'),
    path(
        '<slug:slug>/sua/nhanvien/<int:id>',
        views.suanhanvien,
        name='suanhanvien'),
    path(
        '<slug:slug>/themphong',
        views.themphong,
        name='themphong'),
    path(
        '<slug:slug>/sua/phong/<int:id>',
        views.suaphong,
        name='suaphong'),
    path(
        '<slug:slug>/thembophan',
        views.thembophan,
        name='thembophan'),
    path(
        '<slug:slug>/sua/bophan/<int:id>',
        views.suabophan,
        name='suabophan'),
    path(
        '<slug:slug>/themvaitro',
        views.themvaitro,
        name='themvaitro'),
    path(
        '<slug:slug>/danhsachphong',
        views.danhsachphong,
        name='danhsachphong'),
    path(
        '<slug:slug>/danhsachbophan',
        views.danhsachbophan,
        name='danhsachbophan'),
    path(
        '<slug:slug>/danhsachbophan/<int:id>',
        views.danhsachbophan_phong,
        name='danhsachbophan_phong'),
    path(
        '<slug:slug>/danhsachnhanvien',
        views.danhsachnhanvien,
        name='danhsachnhanvien'),
    path(
        '<slug:slug>/danhsachnhanvien/<int:phong_id>/<int:bophan_id>',
        views.danhsachnhanvien_phong_bophan,
        name='danhsachnhanvien_phong_bophan'),
    path(
        '<slug:slug>/suanhanvien/<int:id>',
        views.suanhanvien,
        name='suanhanvien'),
    path(
        '<slug:slug>/xoanhanvien/<int:id>',
        views.xoanhanvien,
        name='xoanhanvien'),
    path(
        '<slug:slug>/themnghenghiep/',
        views.themnghenghiep,
        name='themnghenghiep'),
    path(
        '<slug:slug>/xoaphong/<int:id>',
        views.xoaphong,
        name='xoaphong'),
    path(
        '<slug:slug>/xoabophan/<int:id>',
        views.xoabophan,
        name='xoabophan'),
    path(
        '<slug:slug>/suachuyengia/<int:id>',
        views.suachuyengia,
        name='suachuyengia'),
    path(
        '<slug:slug>/xoachuyengia/<int:id>',
        views.xoachuyengia,
        name='xoachuyengia'),
    path(
        '<slug:slug>/themnhomchiase',
        views.themnhomchiase,
        name='themnhomchiase'),
    path(
        '<slug:slug>/themnhomnhan',
        views.themnhomnhan,
        name='themnhomnhan'),
    path(
        '<slug:slug>/suanhomchiase/<int:id>',
        views.suanhomchiase,
        name='suanhomchiase'),
    path(
        '<slug:slug>/suanhomnhan/<int:id>',
        views.suanhomnhan,
        name='suanhomnhan'),
    path(
        '<slug:slug>/themmaytinhnhanbaocao',
        views.themmaytinhnhanbaocao,
        name='themmaytinhnhanbaocao'),
    # path(
    #     '<slug:slug>/danhsachmaytinhchiasebaocao',
    #     views.danhsachmaytinhchiasebaocao,
    #     name='danhsachmaytinhchiasebaocao'),
    # path('<slug:slug>/danhsachmaytinhnhanbaocao',
    #         views.danhsachmaytinhnhanbaocao,
    #         name='danhsachmaytinhnhanbaocao'),
    path('<slug:slug>/danhsachmaytinhketnoi',
            views.danhsachmaytinhketnoi,
            name='danhsachmaytinhketnoi'),
    path('<slug:slug>/themmaytinhketnoi',
            views.themmaytinhketnoi,
            name='themmaytinhketnoi'),
    path('<slug:slug>/suamaytinhketnoi/<int:id>',
            views.suamaytinhketnoi,
            name='suamaytinhketnoi'),
    path('<slug:slug>/xoamaytinhketnoi/<int:id>', views.xoamaytinhketnoi, name='xoamaytinhketnoi'),
    path('<slug:slug>/danhsachchucvu', views.danhsachchucvu, name='danhsachchucvu'),
    path('<slug:slug>/them-chuc-vu', views.themchucvu, name='themchucvu'),
    path('<slug:slug>/sua-chuc-vu/<int:id>', views.suachucvu, name='suachucvu'),
    path('<slug:slug>/xoa-chuc-vu/<int:id>', views.xoachucvu, name='xoachucvu'),
    # path(
    #     '<slug:slug>/danhsachbophan?phong_id=<int:phong_id>',
    #     views.danhsachbophan,
    #     name='danhsachbophan'),
    path(
        '<slug:slug>/taoquytrinhdanhgia',
        views.taoquytrinhdanhgia,
        name='taoquytrinhdanhgia'),
    path(
        '<slug:slug>/quanlyquytrinhdanhgia',
        views.quanlyquytrinhdanhgia,
        name='quanlyquytrinhdanhgia'),
    path(
        '<slug:slug>/quanlythongtinduan',
        views.quanlythongtinduan,
        name='quanlythongtinduan'),
    path(
        '<slug:slug>/danhmucbuocdanhgia',
        views.danhmucbuocdanhgia,
        name='danhmucbuocdanhgia'),
    path(
        '<slug:slug>/thembuoc',
        views.thembuoc,
        name='thembuoc'),
    path(
        '<slug:slug>/giamsatquytrinh',
        views.giamsatquytrinh,
        name='giamsatquytrinh'),
    path(
        '<slug:slug>/themquytrinhbuoc',
        views.themquytrinhbuoc,
        name='themquytrinhbuoc'),
    path(
        '<slug:slug>/themkichban',
        views.themkichban,
        name='themkichban'),
    path(
        '<slug:slug>/quanlykichban',
        views.quanlykichban,
        name='quanlykichban'),
]
