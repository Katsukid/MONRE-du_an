import json
import traceback
import logging

from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.db.models import Count
from django.urls import reverse
from django.views.decorators.http import require_POST

from phong.models import *
from phong.forms import *
# from startScan.models import *
from phong.forms import *

logger = logging.getLogger(__name__)

def chuyengia(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'nhanvien/ChuyenGia.html', context)

def themnhomchiase(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'maytinh/themnhomchiase.html', context)

def themnhomnhan(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'maytinh/themnhomnhan.html', context)

def suanhomchiase(request, slug, id):
    nhomchiase = get_object_or_404(NhomChiaSe, id=id)
    form = SuaNhomChiaSeForm(request.POST or None, instance=nhomchiase)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Nhóm chia sẻ {nhomchiase.ten} đã được cập nhật thành công'
                )
            except Exception as e:
                messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
            return HttpResponseRedirect(reverse('danhsachnhomchiasebaocao', kwargs={'slug': slug}))
    
    context = {
        "form": form,
        "nhomchiase": nhomchiase
    }
    context['recon_note_active'] = 'active'
    return render(request, 'maytinh/suanhomchiase.html', context)

def suanhomnhan(request, slug, id):
    nhomnhan = get_object_or_404(NhomNhanBaoCao, id=id)
    form = SuaNhomNhanForm(request.POST or None, instance=nhomnhan)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Nhóm nhận {nhomnhan.ten} đã được cập nhật thành công'
                )
            except Exception as e:
                messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
            return HttpResponseRedirect(reverse('danhsachnhomnhanbaocao', kwargs={'slug': slug}))
    
    context = {
        "form": form,
        "nhomnhan": nhomnhan
    }
    context['recon_note_active'] = 'active'
    return render(request, 'maytinh/suanhomnhan.html', context)

def themmaytinhnhanbaocao(request, slug):
    form = ThemMayTinhNhanBaoCaoForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                data = form.cleaned_data
                maytinh = MayTinhNhomNhan.objects.create(
                    mo_ta=data['may_tinh'],
                    nhom_nhan=data['nhom_nhan']
                )
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Thêm máy tính {data["ten"]} thành công'
                )
            except Exception as e:
                messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
            return HttpResponseRedirect(reverse('danhsachnhomnhanbaocao', kwargs={'slug': slug}))
    
    context = {
        "form": form
    }
    context['recon_note_active'] = 'active'
    return render(request, 'maytinh/themmaytinhnhanbaocao.html', context)

def themmaytinhchiasebaocao(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'maytinh/themmaytinhchiasebaocao.html', context)

def danhsachnhomchiasebaocao(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'maytinh/danhsachnhomchiasebaocao.html', context)

def danhsachnhomnhanbaocao(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'maytinh/danhsachnhomnhanbaocao.html', context)

def chonnhomchiase(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'maytinh/chonnhomchiase.html', context)

def themchuyengia(request, slug):
    try:
        form = ChuyenGiaForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                try:
                    data = form.cleaned_data
                    chuyengia = ChuyenGia.objects.create(
                        ten=data['ten'],
                        so_hieu_cg=data['so_hieu_cg'],
                        don_vi_cong_tac=data['don_vi_cong_tac'],
                        bang_cap=data['bang_cap'],
                        nghe_nghiep=data['nghe_nghiep'],
                        mo_ta=data['mo_ta']
                    )
                    messages.add_message(
                        request,
                        messages.INFO,
                        f'Thêm chuyên gia {data["ten"]} thành công'
                    )
                except Exception as e:
                    messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)} {form.cleaned_data["so_hieu_cg"]}')
                return HttpResponseRedirect(reverse('danhsachchuyengia', kwargs={'slug': slug}))
        context = {}
        context['recon_note_active'] = 'active'
        context['formNgheNghiep'] = NgheNghiepForm()
        context['form'] = form
        return render(request, 'nhanvien/themchuyengia.html', context)
    except Exception as e:
        messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)} {form.cleaned_data["so_hieu_cg"]}')
        context = {}
        context['recon_note_active'] = 'active'
        context['formNgheNghiep'] = NgheNghiepForm()
        context['form'] = ChuyenGiaForm(request.POST or None)
        return render(request, 'nhanvien/themchuyengia.html', context)

def suachuyengia(request, slug, id):
    chuyengia = get_object_or_404(ChuyenGia, id=id)
    form = SuaChuyenGiaForm(request.POST or None, instance=chuyengia)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()  # Lưu thông tin chuyên gia được chỉnh sửa
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Chuyên gia {chuyengia.ten} đã được cập nhật thành công'
                )
            except Exception as e:
                messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
            return HttpResponseRedirect(reverse('danhsachchuyengia', kwargs={'slug': slug}))
    
    context = {
        "form": form,
        "chuyengia": chuyengia
    }
    context['recon_note_active'] = 'active'
    return render(request, 'nhanvien/suachuyengia.html', context)

def xoachuyengia(request, slug, id):
    chuyengia = get_object_or_404(ChuyenGia, id=id)
    if request.method == "POST":
        try:
            chuyengia.delete()
            messages.add_message(
                request,
                messages.INFO,
                f'Chuyên gia {chuyengia.ten} đã được xóa thành công'
            )
        except Exception as e:
            messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
        return HttpResponseRedirect(reverse('danhsachchuyengia', kwargs={'slug': slug}))

    context = {
        "chuyengia": chuyengia
    }
    context['recon_note_active'] = 'active'
    return render(request, 'nhanvien/xoachuyengia.html', context)

def danhsachchuyengia(request, slug):
    context = {}
    try:
        chuyengia_list = ChuyenGia.objects.all()
        chuyengias = []
        for phong in chuyengia_list:
            # phong.so_nhan_vien = phong_count_dict.get(phong.id, 0)
            chuyengias.append(phong)
            
        context = {
            'recon_note_active': 'active',
            'chuyengias': chuyengias
        }
    except Exception as e:
        context['error'] = str(e)
    return render(request, 'nhanvien/danhsachchuyengia.html', context)

def dangkyhotro(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'bophan/dangkyhotro.html', context)

def quanlyruiro(request, slug):
    ruiRos = RuiRo.objects.all()
    context = {
        'recon_note_active': 'active',
        'ruiRos': ruiRos
    }
    return render(request, 'bophan/quanlyruiro.html', context)

def themruiro(request, slug):
    form = ThemRuiRoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                data = form.cleaned_data
                ruiro = RuiRo.objects.create(
                    ten=data['ten'],
                    mo_ta=data['mo_ta'],
                    nguoi_lap=data['nguoi_lap'],
                    loai_rui_ro=data['loai_rui_ro'],
                    du_an=data['du_an']
                )
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Them rui ro {data["ten"]} thanh cong'
                )
            except Exception as e:
                responseData = {'status': False, 'error': str(e)}
                print(responseData)
                messages.add_message(request, messages.ERROR, f'Da xay ra loi: {str(e)}')
            return HttpResponseRedirect(reverse('quanlyruiro', kwargs={'slug': slug}))
    context = {
        "recon_note_active": "active",
        "form": form
    }
    return render(request, 'bophan/themruiro.html', context)

def themphong(request, slug):
    form = ThemPhongForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                data = form.cleaned_data
                phong = Phong.objects.create(
                    ten=data['ten'],
                    phan_cap=data['phan_cap'],
                    mo_ta=data['mo_ta']
                )
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Thêm phòng {data["ten"]} thành công'
                )
            except Exception as e:
                messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
            return HttpResponseRedirect(reverse('danhsachphong',kwargs={'slug': slug}))
    context = {
        "form": form
    }
    context['recon_note_active'] = 'active'
    return render(request, 'phong/themphong.html', context)

def suaphong(request, slug, id):
    phong = get_object_or_404(Phong, id=id)
    form = SuaPhongForm(request.POST or None, instance=phong)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()  # Lưu thông tin phòng được chỉnh sửa
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Phòng {phong.ten} đã được cập nhật thành công'
                )
            except Exception as e:
                messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
            return HttpResponseRedirect(reverse('danhsachphong', kwargs={'slug': slug}))
    
    context = {
        "form": form,
        "phong": phong
    }
    context['recon_note_active'] = 'active'
    return render(request, 'phong/suaphong.html', context)

def xoaphong(request, slug, id):
    phong = get_object_or_404(Phong, id=id)
    if request.method == "POST":
        try:
            phong.delete()
            messages.add_message(
                request,
                messages.INFO,
                f'Phòng {phong.ten} đã được xóa thành công'
            )
        except Exception as e:
            messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
        return HttpResponseRedirect(reverse('danhsachphong', kwargs={'slug': slug}))

    context = {
        "phong": phong
    }
    context['recon_note_active'] = 'active'
    return render(request, 'phong/xoaphong.html', context)

def thembophan(request, slug):
    form = ThemBoPhanForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                data = form.cleaned_data
                bophan = BoPhan.objects.create(
                    ten=data['ten'],
                    mo_ta=data['mo_ta'],
                    phong=data['phong']
                )
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Thêm phòng {data["ten"]} thành công'
                )
            except Exception as e:
                messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
            return HttpResponseRedirect(reverse('danhsachbophan',kwargs={'slug': slug}))
    context = {
        "form": form
    }
    context['recon_note_active'] = 'active'
    return render(request, 'bophan/thembophan.html', context)

def suabophan(request, slug, id):
    bophan = get_object_or_404(BoPhan, id=id)
    form = SuaBoPhanForm(request.POST or None, instance=bophan)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()  # Lưu thông tin bộ phận được chỉnh sửa
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Bộ phận {bophan.ten} đã được cập nhật thành công'
                )
            except Exception as e:
                messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
            return HttpResponseRedirect(reverse('danhsachbophan', kwargs={'slug': slug}))
    
    context = {
        "form": form,
        "bophan": bophan
    }
    context['recon_note_active'] = 'active'
    return render(request, 'bophan/suabophan.html', context)

def xoabophan(request, slug, id):
    bophan = get_object_or_404(BoPhan, id=id)
    if request.method == "POST":
        try:
            bophan.delete()
            messages.add_message(
                request,
                messages.INFO,
                f'Bộ phận {bophan.ten} đã được xóa thành công'
            )
        except Exception as e:
            messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
        return HttpResponseRedirect(reverse('danhsachbophan', kwargs={'slug': slug}))

    context = {
        "bophan": bophan
    }
    context['recon_note_active'] = 'active'
    return render(request, 'bophan/xoabophan.html', context)


def themnhanvien(request, slug):
    form = ThemNhanVienForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                data = form.cleaned_data
                nhanvien = NhanVien.objects.create(
                    ho_ten=data['ho_ten'],
                    mo_ta=data['mo_ta'],
                    chuc_vu=data['chuc_vu'],
                    bo_phan=data['bo_phan']
                )
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Thêm phòng {data["ho_ten"]} thành công'
                )
            except Exception as e:
                messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
            return HttpResponseRedirect(reverse('danhsachnhanvien',kwargs={'slug': slug}))
    context = {
        "form": form
    }
    context['recon_note_active'] = 'active'
    return render(request, 'nhanvien/themnhanvien.html', context)

def suanhanvien(request, slug, id):
    nhanvien = get_object_or_404(NhanVien, id=id)
    form = SuaNhanVienForm(request.POST or None, instance=nhanvien)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()  # Lưu thông tin nhân viên được chỉnh sửa
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Nhân viên {nhanvien.ho_ten} đã được cập nhật thành công'
                )
            except Exception as e:
                messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
            return HttpResponseRedirect(reverse('danhsachnhanvien', kwargs={'slug': slug}))
    
    context = {
        "form": form,
        "nhanvien": nhanvien
    }
    context['recon_note_active'] = 'active'
    return render(request, 'nhanvien/suanhanvien.html', context)

def xoanhanvien(request, slug, id):
    nhanvien = get_object_or_404(NhanVien, id=id)
    if request.method == "POST":
        try:
            nhanvien.delete()
            messages.add_message(
                request,
                messages.INFO,
                f'Nhân viên {nhanvien.ho_ten} đã được xóa thành công'
            )
        except Exception as e:
            messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
        return HttpResponseRedirect(reverse('danhsachnhanvien', kwargs={'slug': slug}))

    context = {
        "nhanvien": nhanvien
    }
    context['recon_note_active'] = 'active'
    return render(request, 'nhanvien/xoanhanvien.html', context)

def get_bophan_by_phong(request):
    phong_id = request.GET.get('phong_id')
    if phong_id:
        bophans = BoPhan.objects.filter(phong_id=phong_id).values('id', 'ten')
        bophan_list = list(bophans)
        return JsonResponse({'bophans': bophan_list})
    return JsonResponse({'error': 'Phòng không hợp lệ'}, status=400)

def get_bophan_by_phong_number(request):
    phong_id = request.GET.get('phong_id')
    if phong_id:
        bophans = BoPhan.objects.filter(phong_id=phong_id).values('id', 'ten')
        bophan_counts = NhanVien.objects.filter(bo_phan__phong_id=phong_id).values('bo_phan_id').annotate(count=Count('id'))
        bophan_count_dict = {item['bo_phan_id']: item['count'] for item in bophan_counts}
        
        bophan_list = []
        for bophan in bophans:
            bophan_id = bophan['id']
            bophan['so_nhan_vien'] = bophan_count_dict.get(bophan_id, 0)
            bophan_list.append(bophan)
        
        return JsonResponse({'bophans': bophan_list})
    
    return JsonResponse({'error': 'Phòng không hợp lệ'}, status=400)

def danhsachphong(request, slug):
    phong_list = Phong.objects.all()
    phong_counts = NhanVien.objects.values('bo_phan__phong_id').annotate(count=Count('id'))
    phong_count_dict = {item['bo_phan__phong_id']: item['count'] for item in phong_counts}
    phongs = []
    for phong in phong_list:
        phong.so_nhan_vien = phong_count_dict.get(phong.id, 0)
        phongs.append(phong)
        
    context = {
        'recon_note_active': 'active',
        'phongs': phongs
    }
    return render(request, 'phong/danhsachphong.html', context)

def danhsachbophan(request, slug):
    phongs = Phong.objects.all()
    context = {
        'recon_note_active': 'active',
        'phongs': phongs
    }
    return render(request, 'bophan/danhsachbophan.html', context)

def danhsachbophan_phong(request, slug, id):
    phongs = Phong.objects.all()
    context = {
        'recon_note_active': 'active',
        'phongs': phongs,
        'phong_id': id
    }
    return render(request, 'bophan/danhsachbophan.html', context)

def danhsachnhanvien_phong_bophan(request, slug, phong_id, bophan_id):
    phongs = Phong.objects.all()
    bophans = BoPhan.objects.filter(phong_id=phong_id).values('id', 'ten')
    # nhanviens = NhanVien.objects.filter(bo_phan_id__in=bophans.values_list('id', flat=True))
    context = {
        'recon_note_active': 'active',
        'phongs': phongs,
        'phong_id': phong_id,
        'bophans': bophans,
        'bophan_id': bophan_id
    }
    return render(request, 'nhanvien/danhsachnhanvien.html', context)

def get_nhanvien_by_bophan(request):
    bophan_id = request.GET.get('bophan_id')
    
    # Kiểm tra nếu bophan_id hợp lệ
    if bophan_id:
        try:
            # Kiểm tra xem bộ phận có tồn tại không
            bophan = BoPhan.objects.get(id=bophan_id)
            
            # Lấy danh sách nhân viên trong bộ phận đó
            nhanviens = NhanVien.objects.filter(bo_phan=bophan).values(
                'id', 'ho_ten', 'chuc_vu', 'bo_phan__ten'  # Lấy các trường cần thiết
            )
            
            # Chuyển danh sách nhân viên thành list
            nhanvien_list = list(nhanviens)
            
            return JsonResponse({'nhanviens': nhanvien_list})

        except BoPhan.DoesNotExist:
            # Trả về lỗi nếu bộ phận không tồn tại
            return JsonResponse({'error': 'Bộ phận không tồn tại'}, status=400)
    
    # Trường hợp không có bophan_id hợp lệ
    return JsonResponse({'error': 'Bộ phận không hợp lệ'}, status=400)

def get_nhanvien_by_phong(request):
    phong_id = request.GET.get('phong_id')
    # bophans = BoPhan.objects.filter(phong_id=phong_id).values('id', 'ten')
    # nhan_vien_list = []
    # for bo_phan in bophans:
    #     nhan_vien_list.append(list(NhanVien.objects.filter(bo_phan_id=bo_phan['id']).values('id', 'ho_ten')))
    nhan_vien_list = NhanVien.objects.filter(bo_phan__phong_id=phong_id).values('id', 'ho_ten')
    return JsonResponse({'nhan_vien_list': list(nhan_vien_list)})

def danhsachnhanvien(request, slug):
    nhanviens = NhanVien.objects.all()
    phongs = Phong.objects.all()
    context = {
        'recon_note_active': 'active',
        'nhanviens': nhanviens,
        'phongs': phongs
    }
    return render(request, 'nhanvien/danhsachnhanvien.html', context)

def themvaitro(request, slug):
    context = {}
    context['recon_note_active'] = 'active'
    return render(request, 'nhanvien/themvaitro.html', context)

@require_POST
def themnghenghiep(request, slug):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        form = NgheNghiepForm(body)
        if form.is_valid():
            data = form.cleaned_data
            giai_doan = NgheNghiep.objects.create(
                ten=data['ten'],
                mo_ta=data['mo_ta']
            )
            messages.add_message(
                request,
                messages.INFO,
                f'Thêm nghề nghiệp {data["ten"]} thành công'
            )
            return JsonResponse({'success': True, 'id': giai_doan.id, 'ten': giai_doan.ten})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    except Exception as e:
        messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

def themchucvu(request, slug):
    if request.method == 'POST':
        form = ThemChucVuForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            chuc_vu = ChucVu.objects.create(
                ten=data['ten'],
                mo_ta=data['mo_ta']
            )
            messages.success(request, 'Thêm chức vụ thành công!')
            return redirect('danhsachchucvu')  # Redirect to the list page or desired URL
    else:
        form = ThemChucVuForm()

    return render(request, 'chucvu/them_chucvu.html', {'form': form})

def suachucvu(request, slug, id):
    chuc_vu = get_object_or_404(ChucVu, id=id)
    
    if request.method == 'POST':
        form = SuaChucVuForm(request.POST, instance=chuc_vu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cập nhật chức vụ thành công!')
            return HttpResponseRedirect(reverse('danhsachchucvu', kwargs={'slug': slug}))
    else:
        form = SuaChucVuForm(instance=chuc_vu)

    return render(request, 'chucvu/sua_chucvu.html', {'form': form, 'chuc_vu': chuc_vu})

def xoachucvu(request, slug, id):
    # Get the ChucVu object, or return a 404 if not found
    chuc_vu = get_object_or_404(ChucVu, id=id)
    try:
        # Try to delete the ChucVu object
        chuc_vu.delete()
        messages.success(request, f'Chức vụ {chuc_vu.ten} đã được xóa thành công')
    except Exception as e:
        # Handle any error that occurs during deletion
        messages.error(request, f'Đã xảy ra lỗi: {str(e)}')
    
    # Redirect to the danh sách chức vụ page after deletion with messages
    return HttpResponseRedirect(reverse('danhsachchucvu', kwargs={'slug': slug}))

def danhsachchucvu(request, slug):
    chuc_vus = ChucVu.objects.all()  # Fetch all ChucVu entries
    context = {
        "chuc_vus": chuc_vus,
    }
    return render(request, 'chucvu/danhsach_chucvu.html', context)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import string
import random
# Tạo key access
@api_view(['POST'])
def generate_key_access(request):
    def generate_random_string(length=512):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    random_string = generate_random_string()
        
    response = HttpResponse(random_string, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=key.txt'
    return response

@api_view(['POST'])
@permission_classes([AllowAny]) 
def agent_receive(request, slug):
    try:
        # Lấy dữ liệu từ request
        mac_address = request.data.get('mac_address')
        ip_address = request.data.get('ip_address')
        hostname = request.data.get('hostname')
        key_hash = request.data.get('key_hash')

        # Kiểm tra các trường dữ liệu cần thiết
        if not all([mac_address, ip_address, hostname, key_hash]):
            return JsonResponse({'success': False, 'error': "Thiếu dữ liệu"}, status=505)

        # Xử lý hoặc lưu trữ dữ liệu tại đây
        # Ví dụ: lưu vào cơ sở dữ liệu, hoặc xử lý logic khác
        text_response = f"Nhận dữ liệu thành công từ {hostname} ({ip_address}) với MAC Address {mac_address}"
        return JsonResponse({'success': True, "message": text_response})

    except Exception as e:
        messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
        return JsonResponse({'success': False, 'error': str(e)}, status=504)


def danhsachmaytinhketnoi(request, slug):
    maytinhs = MayTinhKetNoi.objects.all()
    context = {
        'maytinhs': maytinhs
    }
    return render(request, 'maytinh/danhsachmaytinhketnoi.html', context)

def themmaytinhketnoi(request, slug):
    form = ThemMayTinhKetNoiForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            try:
                maytinh = form.save()
                messages.info(request, f'Thêm máy tính {maytinh.ten} thành công')
            except Exception as e:
                messages.error(request, f'Đã xảy ra lỗi: {str(e)}')
            return HttpResponseRedirect(reverse('danhsachmaytinhketnoi', kwargs={'slug': slug}))
        else:
            # Log the invalid fields and their errors
            for field, errors in form.errors.items():
                messages.error(request, f'Lỗi ở trường {field}: {", ".join(errors)}')
    
    context = {
        "form": form
    }
    return render(request, 'maytinh/themmaytinhketnoi.html', context)

def taoquytrinhdanhgia(request, slug):
    form = ThemQuyTrinhForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                data = form.cleaned_data
                quytrinh = QuyTrinh.objects.create(
                    ten_quy_trinh=data['ten_quy_trinh'],
                    mo_ta=data['mo_ta'],
                    loai_quy_trinh=data['loai_quy_trinh'],
                    nguoi_duyet=data['nguoi_duyet'],
                    phong=data['phong']
                )
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Them quy trinh {data["ten_quy_trinh"]} thanh cong'
                )
            except Exception as e:
                responseData = {'status': False, 'error': str(e)}
                print(responseData)
                messages.add_message(request, messages.ERROR, f'Da xay ra loi: {str(e)}')
            return HttpResponseRedirect(reverse('quanlyquytrinhdanhgia', kwargs={'slug': slug}))
    context = {
        "recon_note_active": "active",
        "form": form
    }
    return render(request, 'quytrinh/taoquytrinhdanhgia.html', context)

def quanlyquytrinhdanhgia(request, slug):
    quyTrinhs = QuyTrinh.objects.all()
    context = {
        'recon_note_active': 'active',
        'quyTrinhs': quyTrinhs
    }
    return render(request, 'quytrinh/quanlyquytrinhdanhgia.html', context)

def quanlythongtinduan(request, slug):
    duAns = DuAn.objects.all()
    context = {
        'recon_note_active': 'active',
        'duAns': duAns
    }
    return render(request, 'quytrinh/quanlythongtinduan.html', context)

def danhmucbuocdanhgia(request, slug):
    buocs = Buoc.objects.all()
    context = {
        'recon_note_active': 'active',
        'buocs': buocs
    }
    return render(request, 'quytrinh/danhmucbuocdanhgia.html', context)

def thembuoc(request, slug):
    form = ThemBuocForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                data = form.cleaned_data
                buoc = Buoc.objects.create(
                    ten_buoc = data['ten_buoc'],
                    thu_tu = data['thu_tu'],
                    tai_lieu_mo_ta=data['tai_lieu_mo_ta'],
                    yeu_cau=data['yeu_cau'],
                    id_DoiTuong=data['id_DoiTuong']
                )
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Them buoc {data["ten_buoc"]} thanh cong'
                )
            except Exception as e:
                responseData = {'status': False, 'error': str(e)}
                print(responseData)
                messages.add_message(request, messages.ERROR, f'Da xay ra loi: {str(e)}')
            return HttpResponseRedirect(reverse('danhmucbuocdanhgia', kwargs={'slug': slug}))
    context = {
        "recon_note_active": "active",
        "form": form
    }
    return render(request, 'quytrinh/thembuoc.html', context)

def giamsatquytrinh(request, slug):
    quyTrinhBuocs = QuyTrinhBuoc.objects.all()
    context = {
        'recon_note_active': 'active',
        'quyTrinhBuocs': quyTrinhBuocs
    }
    return render(request, 'quytrinh/giamsatquytrinh.html', context)

def themquytrinhbuoc(request, slug):
    form = ThemQuyTrinhBuocForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                data = form.cleaned_data
                quytrinhBuoc = QuyTrinhBuoc.objects.create(
                    id_QuyTrinh = data['id_QuyTrinh'],
                    id_Buoc = data['id_Buoc']
                )
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Them quy trinh - buoc moi thanh cong'
                )
            except Exception as e:
                responseData = {'status': False, 'error': str(e)}
                print(responseData)
                messages.add_message(request, messages.ERROR, f'Da xay ra loi: {str(e)}')
            return HttpResponseRedirect(reverse('giamsatquytrinh', kwargs={'slug': slug}))
    context = {
        "recon_note_active": "active",
        "form": form
    }
    return render(request, 'quytrinh/themquytrinhbuoc.html', context)

def suamaytinhketnoi(request, slug, id):
    maytinh = get_object_or_404(MayTinhKetNoi, id=id)
    form = SuaMayTinhKetNoiForm(request.POST or None, instance=maytinh)
    if request.method == "POST":
        if form.is_valid():
            try:
                form.save()
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Máy tính {maytinh.ten} đã được cập nhật thành công'
                )
            except Exception as e:
                messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
            return HttpResponseRedirect(reverse('danhsachmaytinhketnoi', kwargs={'slug': slug}))
    
    context = {
        "form": form,
        "maytinh": maytinh
    }
    context['recon_note_active'] = 'active'
    return render(request, 'maytinh/suamaytinhketnoi.html', context)

def xoamaytinhketnoi(request, slug, id):
    maytinh = get_object_or_404(MayTinhKetNoi, id=id)
    if request.method == "POST":
        try:
            maytinh.delete()
            messages.add_message(
                request,
                messages.INFO,
                f'Máy tính {maytinh.ten} đã được xóa thành công'
            )
        except Exception as e:
            messages.add_message(request, messages.ERROR, f'Đã xảy ra lỗi: {str(e)}')
        return HttpResponseRedirect(reverse('danhsachmaytinhketnoi', kwargs={'slug': slug}))

    context = {
        "maytinh": maytinh
    }
    context['recon_note_active'] = 'active'
    return render(request, 'maytinh/xoamaytinhketnoi.html', context)

def themkichban(request, slug):
    form = ThemKichBanForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                data = form.cleaned_data
                kichban = KichBan.objects.create(
                    ten=data['ten'],
                    mo_ta=data['mo_ta'],
                    tai_lieu=data['tai_lieu'],
                    id_QuyTrinhPhienBan=data['id_QuyTrinhPhienBan'],
                    id_MauKichBan=data['id_MauKichBan']
                )
                messages.add_message(
                    request,
                    messages.INFO,
                    f'Them kich ban {data["ten"]} thanh cong'
                )
            except Exception as e:
                responseData = {'status': False, 'error': str(e)}
                print(responseData)
                messages.add_message(request, messages.ERROR, f'Da xay ra loi: {str(e)}')
            return HttpResponseRedirect(reverse('quanlykichban', kwargs={'slug': slug}))
    context = {
        "recon_note_active": "active",
        "form": form
    }
    return render(request, 'quytrinh/themkichban.html', context)

def quanlykichban(request, slug):
    kichBans = KichBan.objects.all()
    context = {
        'recon_note_active': 'active',
        'kichBans': kichBans
    }
    return render(request, 'quytrinh/quanlykichban.html', context)