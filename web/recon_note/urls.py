from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('<slug:slug>/themnentang', views.themnentang, name='themnentang'),
    path('<slug:slug>/themgiaidoan', views.themgiaidoan, name='themgiaidoan'),
    path(
        '<slug:slug>/list_note',
        views.list_note,
        name='list_note'),
    path(
        '<slug:slug>/list_note_2',
        views.list_note_2,
        name='list_note_2'),
    path(
        '<slug:slug>/quanlyquytrinh',
        views.quanlyquytrinh,
        name='quanlyquytrinh'),
    path(
        '<slug:slug>/quanlyquytrinhthuchien',
        views.quanlyquytrinhthuchien,
        name='quanlyquytrinhthuchien'),
    path(
        '<slug:slug>/quanlygiaidoanphattrien',
        views.quanlygiaidoanphattrien,
        name='quanlygiaidoanphattrien'),
    path(
        '<slug:slug>/danhmucnguonlohong',
        views.danhmucnguonlohong,
        name='danhmucnguonlohong'),
    path(
        '<slug:slug>/danhmuclohong',
        views.danhmuclohong,
        name='danhmuclohong'),
    path(
        '<slug:slug>/danhmucloailohong',
        views.danhmucloailohong,
        name='danhmucloailohong'),
    path(
        '<slug:slug>/themnguonlohong',
        views.themnguonlohong,
        name='themnguonlohong'),
    path(
        '<slug:slug>/sua/nguonlohong/<int:id>',
        views.suanguonlohong,
        name='suanguonlohong'),
    path(
        '<slug:slug>/xoa/nguonlohong/<int:id>',
        views.xoanguonlohong,
        name='xoanguonlohong'),
    path(
        '<slug:slug>/themhosophanmem',
        views.themhosophanmem,
        name='themhosophanmem'),
    path(
        '<slug:slug>/themphienban',
        views.themphienban,
        name='themphienban'),
    # path(
    #     '<slug:slug>/themkichban',
    #     views.themkichban,
    #     name='themkichban'),
    path(
        '<slug:slug>/themphienbanphanmem',
        views.themphienbanphanmem,
        name='themphienbanphanmem'),
    path(
        '<slug:slug>/themloailohong',
        views.themloailohong,
        name='themloailohong'),
    path(
        '<slug:slug>/xoa/loailohong/<int:id>',
        views.xoaloailohong,
        name='xoaloailohong'),
    path(
        '<slug:slug>/themlohong',
        views.themlohong,
        name='themlohong'),
    path(
        '<slug:slug>/thembienphap',
        views.thembienphap,
        name='thembienphap'),
    path(
        'flip_todo_status',
        views.flip_todo_status,
        name='flip_todo_status'),
    path(
        'flip_important_status',
        views.flip_important_status,
        name='flip_important_status'),
    path(
        'delete_note',
        views.delete_note,
        name='delete_note'),
    path(
        '<slug:slug>/danhsach_hosophanmem',
        views.danhsach_hosophanmem,
        name='danhsach_hosophanmem'),
]
