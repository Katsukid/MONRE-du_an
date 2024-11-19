import json
import traceback
import logging

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django import http
from django.urls import reverse
from django.views.decorators.http import require_POST

from recon_note.models import *
from recon_note.forms import *
from startScan.models import *
from scanEngine.forms import *

logger = logging.getLogger(__name__)

def list_note(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'note/index.html', context)

def list_note_2(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'note/quytrinh.html', context)

def quanlyquytrinh(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'note/quanlyquytrinh.html', context)

def quanlyquytrinhthuchien(request, slug):
    context = {'scan_engine_nav_active': 'active', 'file_li': 'active'}
    form = AddUploadFile(request.POST or None, request.FILES or None, project=slug)
    if request.method == "POST":
        if form.is_valid() and 'upload_file' in request.FILES:
            tar_file = request.FILES['upload_file']
            project = Project.objects.get(slug=slug)
            if tar_file.content_type == 'application/x-tar':
                file_path = '/usr/src/app/file_upload/' + form.cleaned_data['short_name'] + '.tar'
                with open(file_path, 'wb+') as destination:
                    for chunk in tar_file.chunks():
                        destination.write(chunk)
                UploadFile.objects.create(
                    name=form.cleaned_data['name'],
                    short_name=form.cleaned_data['short_name'],
                    project=project)
                messages.add_message(
                    request,
                    messages.INFO,
                    'File upload ' + form.cleaned_data['name'] +
                    ' added successfully')
                return http.HttpResponseRedirect(reverse('file_list', kwargs={'slug': slug}))
    context['form'] = form
    context['recon_note_active'] = 'active'
    return render(request, 'note/quanlyquytrinhthuchien.html', context)

def danhmucnguonlohong(request, slug):
    nguonLoHongs = NguonLoHong.objects.all()
    context = {
        'recon_note_active': 'active',
        'nguonLoHongs': nguonLoHongs
    }
    return render(request, 'note/danhmucnguonlohong.html', context)

def danhmuclohong(request, slug):
    loHongs = LoHong.objects.all()
    context = {
        'recon_note_active': 'active',
        'loHongs': loHongs
    }
    return render(request, 'note/danhmuclohong.html', context)

def danhmucloailohong(request, slug):
    loaiLoHongs = LoaiLoHong.objects.all()
    context = {
        'recon_note_active': 'active',
        'loaiLoHongs': loaiLoHongs
    }
    return render(request, 'note/danhmucloailohong.html', context)

def themnguonlohong(request, slug):
    form = ThemNguonLoHongForm(request.POST or None, project=slug)
    if request.method == "POST":
        if form.is_valid():
            try:
                data = form.cleaned_data
                nguonLoHong = NguonLoHong.objects.create(
                    ten_nguon=data['ten_nguon'],
                    ky_hieu=data['ky_hieu'],
                    mo_ta=data['mo_ta'],
                    duong_dan=data['duong_dan'])
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Thêm nguồn {data["ten_nguon"]} thành công')
            except Exception as e:
                responseData = {'status': False, 'error': str(e)}
                print(responseData)
                messages.add_message(request, messages.ERROR, f'An unexpected error occurred: {str(e)}')
            return HttpResponseRedirect(reverse('danhmucnguonlohong', kwargs={'slug': slug}))
    context = {
        "recon_note_active": "active",
        "form": form
    }
    return render(request, 'note/themnguonlohong.html', context)

def suanguonlohong(request, slug, id):
    try:
        nguonlohong = get_object_or_404(NguonLoHong, id=id)
        form = SuaNguonLoHongForm()
        if request.method == 'POST':
            form = SuaNguonLoHongForm(request.POST, instance=nguonlohong)
            if form.is_valid():
                    data = form.cleaned_data
                    nguonlohong_obj = NguonLoHong.objects.filter(id=id)
                    nguonlohong_obj.update(
                        ten_nguon = data['ten_nguon'],
                        ky_hieu = data['ky_hieu'],
                        mo_ta = data['mo_ta'],
                        duong_dan = data['duong_dan']
                    )
                    msg = f'Nguồn lỗ hổng {nguonlohong.ten_nguon} đã được thay đổi !'
                    logger.info(msg)
                    messages.add_message(
                        request,
                        messages.INFO,
                        msg
                    )
                    return HttpResponseRedirect(reverse('danhmucnguonlohong', kwargs={'slug': slug}))
        else:
            form.set_value(nguonlohong.ten_nguon, nguonlohong.ky_hieu, nguonlohong.mo_ta, nguonlohong.duong_dan)
        context = {
            'nguonlohong': nguonlohong,
            'form': form,
            "recon_note_active": "active",
        }
        return render(request, 'note/suanguonlohong.html', context)
    except Exception as e:
        print(traceback.format_exc())
        logger.error(f'Đã xảy ra lỗi không mong đợi: {str(e)}')
        messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi không mong đợi: {str(e)}')

def xoanguonlohong(request, slug, id):
    if request.method == "POST":
        obj = get_object_or_404(NguonLoHong, id=id)
        obj.delete()
        responseData = {'status': 'true'}
        messages.add_message(
            request,
            messages.INFO,
            'NguonLoHong successfully deleted!')
    else:
        responseData = {'status': 'false'}
        messages.add_message(
            request,
            messages.ERROR,
            'Oops! NguonLoHong could not be deleted!')
    return JsonResponse(responseData)

def themhosophanmem(request, slug):
    # Tạo ngữ cảnh để truyền vào template
    context = {'recon_note_active': 'active'}
    try:
        # Khởi tạo form với POST và FILES (nếu có)
        form = HoSoPhanMemForm(request.POST or None, request.FILES or None)
        error = str(form.errors)
        if request.method == "POST":
            if form.is_valid():
                error = 'tai_lieu is not in request.FILES'
                if 'tai_lieu' in request.FILES:  # Kiểm tra tính hợp lệ và xem có tệp tải lên không
                    tai_lieu = request.FILES['tai_lieu']  # Lấy tệp từ form
                    error = "No error"  # Đặt lại thông báo lỗi
                    # Kiểm tra định dạng tệp (chỉ cho phép pdf hoặc zip)
                    if tai_lieu.content_type in ['application/pdf', 'application/zip']:
                        # Đọc nội dung tệp nếu cần (hoặc lưu trực tiếp tệp)
                        file_content = tai_lieu.read()
                        
                        # Lưu tệp vào đường dẫn cố định hoặc theo MEDIA_ROOT (nếu cần xử lý tùy chỉnh)
                        with open(f'/usr/src/app/upload_file/{form.cleaned_data["phien_ban"]}_{tai_lieu.name}', 'wb') as f:
                            f.write(file_content)
                        
                        # Lưu thông tin vào cơ sở dữ liệu
                        HoSoPhanMem.objects.create(
                            nguoi_them=form.cleaned_data['nguoi_them'],
                            phien_ban=form.cleaned_data['phien_ban'],
                            giai_doan=form.cleaned_data['giai_doan'],
                            nen_tang=form.cleaned_data['nen_tang'],
                            mo_ta=form.cleaned_data['mo_ta'],
                            tai_lieu=tai_lieu  # Lưu đối tượng FileField trong cơ sở dữ liệu
                        )
                        
                        # Thông báo thành công cho người dùng
                        messages.add_message(
                            request,
                            messages.INFO,
                            f'Hồ sơ phần mềm {form.cleaned_data["phien_ban"]} được thêm thành công!'
                        )
                        
                        # Chuyển hướng tới trang khác sau khi hoàn thành
                        return HttpResponseRedirect(reverse('danhmucnguonlohong', kwargs={'slug': slug}))
        
        # Khởi tạo các form phụ nếu cần
        formGiaiDoan = GiaiDoanPhatTrienForm()
        formNenTang = NenTangPhatTrienForm()
        
        # Thêm form vào ngữ cảnh
        context['form'] = form
        context['formGiaiDoan'] = formGiaiDoan
        context['formNenTang'] = formNenTang
        context['error'] = error
        
        # Render trang với các form và ngữ cảnh
        return render(request, 'note/themhosophanmem.html', context)
    except Exception as e:
        return JsonResponse({'status': False, 'error': str(e)}, status=500)

def themphienban(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'note/themphienban.html', context)

def themkichban(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'note/themkichban.html', context)

def themphienbanphanmem(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'note/themphienbanphanmem.html', context)

def themloailohong(request, slug):
    form = ThemLoaiLoHongForm(request.POST or None, project=slug)
    if request.method == "POST":
        if form.is_valid():
            try:
                data = form.cleaned_data
                loaiLoHong = LoaiLoHong.objects.create(
                    ten_loai=data['ten_loai'],
                    mo_ta=data['mo_ta'])
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Thêm loại {data["ten_loai"]} thành công')
            except Exception as e:
                responseData = {'status': False, 'error': str(e)}
                print(responseData)
                messages.add_message(request, messages.ERROR, f'An unexpected error occurred: {str(e)}')
            return HttpResponseRedirect(reverse('danhmucloailohong', kwargs={'slug': slug}))
    context = {
        "recon_note_active": "active",
        "form": form
    }
    return render(request, 'note/themloailohong.html', context)

def xoaloailohong(request, slug, id):
    if request.method == "POST":
        obj = get_object_or_404(LoaiLoHong, id=id)
        obj.delete()
        responseData = {'status': 'true'}
        messages.add_message(
            request,
            messages.INFO,
            'LoaiLoHong successfully deleted!')
    else:
        responseData = {'status': 'false'}
        messages.add_message(
            request,
            messages.ERROR,
            'Oops! LoaiLoHong could not be deleted!')
    return JsonResponse(responseData)

def themlohong(request, slug):
    form = ThemLoHongForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                data = form.cleaned_data
                loHong = LoHong.objects.create(
                    ten_lo_hong=data['ten_lo_hong'],
                    mo_ta=data['mo_ta'],
                    muc_do=data['muc_do'],
                    id_LoaiLoHong=data['id_LoaiLoHong'],
                    id_NguonLoHong=data['id_NguonLoHong'],
                    id_BienPhap=data['id_BienPhap'])
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Thêm lỗ hổng {data["ten_lo_hong"]} thành công')
            except Exception as e:
                responseData = {'status': False, 'error': str(e)}
                print(responseData)
                messages.add_message(request, messages.ERROR, f'An unexpected error occurred: {str(e)}')
            return HttpResponseRedirect(reverse('danhmuclohong', kwargs={'slug': slug}))
    formBienPhap = ThemBienPhapForm()
    context = {
        "recon_note_active": "active",
        "form": form,
        "formBienPhap": formBienPhap
    }
    return render(request, 'note/themlohong.html', context)

@require_POST
def thembienphap(request, slug):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        form = ThemBienPhapForm(body)
        if form.is_valid():
            data = form.cleaned_data
            bien_phap = BienPhap.objects.create(
                ten_bien_phap=data['ten_bien_phap'],
                mo_ta=data['mo_ta']
            )
            messages.add_message(
                request,
                messages.INFO,
                f'Thêm biện pháp {data["ten_bien_phap"]} thành công'
            )
            return JsonResponse({'success': True, 'id': bien_phap.id, 'ten_bien_phap': bien_phap.ten_bien_phap})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    except Exception as e:
        messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

def flip_todo_status(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        note = TodoNote.objects.get(id=body['id'])
        note.is_done = not note.is_done
        note.save()

    return JsonResponse({'status': True})

def flip_important_status(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        note = TodoNote.objects.get(id=body['id'])
        note.is_important = not note.is_important
        note.save()

    return JsonResponse({'status': True})

def delete_note(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        TodoNote.objects.filter(id=body['id']).delete()

    return JsonResponse({'status': True})

@require_POST
def themnentang(request, slug):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        form = NenTangPhatTrienForm(body)
        if form.is_valid():
            data = form.cleaned_data
            nen_tang = NenTangPhatTrien.objects.create(
                ten=data['ten'],
                mo_ta=data['mo_ta']
            )
            messages.add_message(
                request,
                messages.INFO,
                f'Thêm nền tảng {data["ten"]} thành công'
            )
            return JsonResponse({'success': True, 'id': nen_tang.id, 'ten': nen_tang.ten})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    except Exception as e:
        messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

@require_POST
def themgiaidoan(request, slug):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        form = GiaiDoanPhatTrienForm(body)
        if form.is_valid():
            data = form.cleaned_data
            giai_doan = GiaiDoanPhatTrien.objects.create(
                ten=data['ten'],
                mo_ta=data['mo_ta']
            )
            messages.add_message(
                request,
                messages.INFO,
                f'Thêm giai đoạn {data["ten"]} thành công'
            )
            return JsonResponse({'success': True, 'id': giai_doan.id, 'ten': giai_doan.ten})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    except Exception as e:
        messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

def quanlygiaidoanphattrien(request, slug):
    giaiDoanPhatTriens = GiaiDoanPhatTrien.objects.all()
    context = {
        'recon_note_active': 'active',
        'giaiDoanPhatTriens': giaiDoanPhatTriens
    }
    return render(request, 'note/quanlygiaidoanphattrien.html', context)

def danhsach_hosophanmem(request, slug):
    try:
        hosos = HoSoPhanMem.objects.all()
        context = {
            'recon_note_active': 'active',
            'hosos': hosos
        }
        return render(request, 'hosophanmem/danhsach_hosophanmem.html', context)
    except Exception as e:
        messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
        return JsonResponse({'success': False, 'error': str(e)}, status=500)