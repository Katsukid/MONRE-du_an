from django import forms
from .models import *

class ThemPhongForm(forms.Form):
    ten = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "phongName",
                "placeholder": "Tên phòng"
            }
        )
    )
    PHAN_CAP_CHOICES = [
        ('chuyen_mon', 'Chuyên môn'),
        ('cong_nghe_thong_tin', 'Công nghệ thông tin'),
        ('nghiep_vu_sua_chua', 'Nghiệp vụ sửa chữa'),
    ]
    # Mutliple choice field: Chuyên môn, Công nghệ thông tin, Nghiệp vụ sửa chữa
    phan_cap = forms.CharField(
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "phongDescription",
                "placeholder": "Phân cấp phòng"
            },
            choices=PHAN_CAP_CHOICES
        )
    )
    
    mo_ta = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "phongDescription",
                "rows": 3,
                "placeholder": "Mô tả phòng"
            }
        )
    )

    def clean_ten(self):
        data = self.cleaned_data['ten']
        if Phong.objects.filter(ten=data).exists():
            raise forms.ValidationError(f"Tên phòng {data} đã tồn tại")
        return data

class SuaPhongForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SuaPhongForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Phong
        fields = ['ten', 'phan_cap', 'mo_ta']

    ten = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "phongName",
                "placeholder": "Tên phòng"
            }
        )
    )

    PHAN_CAP_CHOICES = [
        ('chuyen_mon', 'Chuyên môn'),
        ('cong_nghe_thong_tin', 'Công nghệ thông tin'),
        ('nghiep_vu_sua_chua', 'Nghiệp vụ sửa chữa'),
    ]
    # Mutliple choice field: Chuyên môn, Công nghệ thông tin, Nghiệp vụ sửa chữa
    phan_cap = forms.CharField(
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "phongDescription",
                "placeholder": "Phân cấp phòng"
            },
            choices=PHAN_CAP_CHOICES
        )
    )

    mo_ta = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "phongDescription",
                "rows": 3,
                "placeholder": "Mô tả phòng"
            }
        )
    )

    def set_value(self, ten_value, phan_cap_value, mo_ta_value):
        self.initial['ten'] = ten_value
        self.initial['phan_cap'] = phan_cap_value
        self.initial['mo_ta'] = mo_ta_value

class ThemBoPhanForm(forms.ModelForm):
    class Meta:
        model = BoPhan
        fields = ['ten', 'mo_ta', 'phong']

        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'boPhanName',
                'placeholder': 'Bộ phận 1'
            }),
            'mo_ta': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'description',
                'rows': 3,
                'placeholder': 'Mô tả bộ phận'
            }),
            'phong': forms.Select(attrs={
                'class': 'form-select',
                'id': 'phongSelect'
            })
        }

    # Optional: Validate if a division with the same name exists
    def clean_ten(self):
        data = self.cleaned_data['ten']
        if BoPhan.objects.filter(ten=data).exists():
            raise forms.ValidationError(f"Bộ phận với tên '{data}' đã tồn tại")
        return data

class SuaBoPhanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SuaBoPhanForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = BoPhan
        fields = ['ten', 'mo_ta', 'phong']

    ten = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "boPhanName",
                "placeholder": "Tên bộ phận"
            }
        )
    )

    mo_ta = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "boPhanDescription",
                "rows": 3,
                "placeholder": "Mô tả bộ phận"
            }
        )
    )

    phong = forms.ModelChoiceField(
        queryset=Phong.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "phongSelect"
            }
        )
    )

    def set_value(self, ten_value, mo_ta_value, phong_value):
        self.initial['ten'] = ten_value
        self.initial['mo_ta'] = mo_ta_value
        self.initial['phong'] = phong_value

class ThemNhanVienForm(forms.ModelForm):
    class Meta:
        model = NhanVien
        fields = ['ho_ten', 'mo_ta', 'bo_phan']

        widgets = {
            'ho_ten': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'nhanVienName',
                'placeholder': 'Họ tên nhân viên'
            }),
            'mo_ta': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'nhanVienDescription',
                'rows': 3,
                'placeholder': 'Mô tả nhân viên'
            }),
            'bo_phan': forms.Select(attrs={
                'class': 'form-select',
                'id': 'boPhanSelect',
                'placeholder': 'Chọn bộ phận'
            })
        }
    # PHONG_CHOICES = []
    # if Phong.objects.all().exists():
    PHONG_CHOICES = list(Phong.objects.all().values_list('id', 'ten'))
    PHONG_CHOICES.insert(0,("","Chọn phòng"))
    
    phong = forms.CharField(
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "phongSelect",
                "placeholder": "Chọn phòng"
            },
            choices= PHONG_CHOICES
        )
    )
    
    
    # CHUC_VU_CHOICES = [("","Chọn chức vụ"),
    #                    ("truong_phong", "Trưởng phòng"), 
    #                    ("pho_phong", "Phó phòng"), 
    #                    ("nhan_vien", "Nhân viên"), 
    #                    ("chuyen_vien", "Chuyên viên"), 
    #                    ("chuyen_gia", "Chuyên gia")]
    chuc_vu = forms.ModelChoiceField(
        queryset=ChucVu.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "chucvuSelect",
                "placeholder": "Chọn chức vụ"
            }
        )
    )
    
    # Optional: Validate if an employee with the same name exists
    def clean_ho_ten(self):
        data = self.cleaned_data['ho_ten']
        if NhanVien.objects.filter(ho_ten=data).exists():
            raise forms.ValidationError(f"Nhân viên với tên '{data}' đã tồn tại")
        return data
    
from django import forms
from .models import NhanVien, Phong, BoPhan

class SuaNhanVienForm(forms.ModelForm):
    # PHONG_CHOICES = []
    # if Phong.objects.all().exists():
    PHONG_CHOICES = list(Phong.objects.all().values_list('id', 'ten'))
    PHONG_CHOICES.insert(0,("","Chọn phòng"))

    CHUC_VU_CHOICES = [
        ("", "Chọn chức vụ"),
        ("truong_phong", "Trưởng phòng"), 
        ("pho_phong", "Phó phòng"), 
        ("nhan_vien", "Nhân viên"), 
        ("chuyen_vien", "Chuyên viên"), 
        ("chuyen_gia", "Chuyên gia")
    ]

    def __init__(self, *args, **kwargs):
        super(SuaNhanVienForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            instance = kwargs['instance']
            # Gán giá trị hiện tại của phòng vào phong nếu cần
            if instance.bo_phan and instance.bo_phan.phong:
                self.fields['phong'].initial = instance.bo_phan.phong.id
            # Gán giá trị hiện tại của chức vụ vào chuc_vu nếu cần
            self.fields['chuc_vu'].initial = instance.chuc_vu

    class Meta:
        model = NhanVien
        fields = ['ho_ten', 'chuc_vu', 'mo_ta', 'bo_phan']

    ho_ten = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "hoTen",
                "placeholder": "Họ tên nhân viên"
            }
        )
    )

    phong = forms.ChoiceField(
        required=True,
        choices=PHONG_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "phongSelect",
                "placeholder": "Chọn phòng"
            }
        )
    )

    chuc_vu = forms.ChoiceField(
        required=True,
        choices=CHUC_VU_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "chucvuSelect",
                "placeholder": "Chọn chức vụ"
            }
        )
    )

    mo_ta = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "moTa",
                "rows": 3,
                "placeholder": "Mô tả nhân viên"
            }
        )
    )

    bo_phan = forms.ModelChoiceField(
        queryset=BoPhan.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "boPhanSelect"
            }
        )
    )
    

class NgheNghiepForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NgheNghiepForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = NgheNghiep
        fields = ['ten', 'mo_ta']
    
    ten = forms.CharField(
        label='Nghề nghiệp',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'ten',  # id matches for JS
            'placeholder': 'Giai đoạn phát triển'
        })
    )
    
    mo_ta = forms.CharField(
        label='Mô tả',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'mo',  # id matches for JS
            'rows': 3,
            'placeholder': 'Mô tả nghề nghiệp'
        }),
        required=False
    )

class ChuyenGiaForm(forms.ModelForm):
    class Meta:
        model = ChuyenGia
        fields = ['so_hieu_cg', 'ten', 'don_vi_cong_tac', 'bang_cap', 'mo_ta', 'phong', 'nguoi_dung', 'nghe_nghiep']
    
    # Thiết lập trường select cho nghe_nghiep với danh sách nghề nghiệp
    nghe_nghiep = forms.ModelChoiceField(
        queryset=NgheNghiep.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'profession'
        }),
        required=False,
        label='Nghề nghiệp'
    )

    # Các trường khác như họ và tên, số hiệu CG,...
    so_hieu_cg = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'expertCode',
            'placeholder': 'CG_01'
        }),
        required=True,
        label='Số hiệu CG'
    )

    ten = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'fullName',
            'placeholder': 'Nguyễn Văn Bảy'
        }),
        required=True,
        label='Họ và tên'
    )

    don_vi_cong_tac = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'workplace',
            'placeholder': 'Công ty DX Tech'
        }),
        required=True,
        label='Đơn vị công tác'
    )

    bang_cap = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'qualifications',
            'rows': 3
        }),
        required=False,
        label='Bằng cấp'
    )

    mo_ta = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'description',
            'rows': 3
        }),
        required=False,
        label='Mô tả'
    )

class SuaChuyenGiaForm(forms.ModelForm):
    class Meta:
        model = ChuyenGia
        fields = ['so_hieu_cg', 'ten', 'don_vi_cong_tac', 'bang_cap', 'mo_ta', 'phong', 'nguoi_dung', 'nghe_nghiep']

    nghe_nghiep = forms.ModelChoiceField(
        queryset=NgheNghiep.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'nghe_nghiep'
        }),
        required=False,
        label='Nghề nghiệp'
    )

    so_hieu_cg = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'so_hieu_cg',  # id matches for JS
            'placeholder': 'CG_01'
        }),
        required=True,
        label='Số hiệu CG'
    )

    ten = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'ten',  # id matches for JS
            'placeholder': 'Nguyễn Văn Bảy'
        }),
        required=True,
        label='Họ và tên'
    )

    don_vi_cong_tac = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'don_vi_cong_tac',  # id matches for JS
            'placeholder': 'Công ty DX Tech'
        }),
        required=True,
        label='Đơn vị công tác'
    )

    bang_cap = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'bang_cap',  # id matches for JS
            'rows': 3
        }),
        required=False,
        label='Bằng cấp'
    )

    mo_ta = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'mo_ta',  # id matches for JS
            'rows': 3
        }),
        required=False,
        label='Mô tả'
    )

    phong = forms.ModelChoiceField(
        queryset=Phong.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'phong'  # id matches for JS
        }),
        required=False,
        label='Phòng'
    )

    nguoi_dung = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'nguoi_dung'  # id matches for JS
        }),
        required=False,
        label='Người dùng'
    )

    def __init__(self, *args, **kwargs):
        super(SuaChuyenGiaForm, self).__init__(*args, **kwargs)
        
        if 'instance' in kwargs:
            instance = kwargs['instance']
            self.fields['nghe_nghiep'].initial = instance.nghe_nghiep
            self.fields['phong'].initial = instance.phong
            self.fields['nguoi_dung'].initial = instance.nguoi_dung
            
            class SuaNhomNhanForm(forms.ModelForm):
                class Meta:
                    model = NhomNhanBaoCao
                    fields = ['ten', 'mo_ta']

                ten = forms.CharField(
                    required=True,
                    widget=forms.TextInput(
                        attrs={
                            "class": "form-control",
                            "id": "nhomNhanName",
                            "placeholder": "Tên nhóm nhận"
                        }
                    )
                )

                mo_ta = forms.CharField(
                    required=False,
                    widget=forms.Textarea(
                        attrs={
                            "class": "form-control",
                            "id": "nhomNhanDescription",
                            "rows": 3,
                            "placeholder": "Mô tả nhóm nhận"
                        }
                    )
                )

class ThemMayTinhNhanBaoCaoForm(forms.ModelForm):
    class Meta:
        model = MayTinhNhomNhan
        fields = ['may_tinh', 'nhom_nhan']

        widgets = {
            'may_tinh': forms.Select(attrs={
                'class': 'form-select',
                'id': 'mayTinhSelect',
                'placeholder': 'Chọn máy tính'
            }),
            'nhom_nhan': forms.Select(attrs={
                'class': 'form-select',
                'id': 'nhomNhanSelect',
                'placeholder': 'Chọn nhóm nhận'
            })
        }

class SuaMayTinhNhanBaoCaoForm(forms.ModelForm):
    class Meta:
        model = MayTinhNhomNhan
        fields = ['may_tinh', 'nhom_nhan']

    may_tinh = forms.ModelChoiceField(
        queryset=MayTinhKetNoi.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "mayTinhSelect",
                "placeholder": "Chọn máy tính"
            }
        )
    )

    nhom_nhan = forms.ModelChoiceField(
        queryset=NhomNhanBaoCao.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "nhomNhanSelect",
                "placeholder": "Chọn nhóm nhận"
            }
        )
    )

class ThemMayTinhChiaSeBaoCaoForm(forms.ModelForm):
    class Meta:
        model = MayTinhNhomChiaSe
        fields = ['may_tinh', 'nhom_chia_se']

        widgets = {
            'may_tinh': forms.Select(attrs={
                'class': 'form-select',
                'id': 'mayTinhSelect',
                'placeholder': 'Chọn máy tính'
            }),
            'nhom_chia_se': forms.Select(attrs={
                'class': 'form-select',
                'id': 'nhomChiaSeSelect',
                'placeholder': 'Chọn nhóm chia sẻ'
            })
        }

class SuaMayTinhChiaSeBaoCaoForm(forms.ModelForm):
    class Meta:
        model = MayTinhNhomChiaSe
        fields = ['may_tinh', 'nhom_chia_se']

    may_tinh = forms.ModelChoiceField(
        queryset=MayTinhKetNoi.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "mayTinhSelect",
                "placeholder": "Chọn máy tính"
            }
        )
    )

    nhom_chia_se = forms.ModelChoiceField(
        queryset=NhomChiaSe.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "nhomChiaSeSelect",
                "placeholder": "Chọn nhóm chia sẻ"
            }
        )
    )

class SuaNhomNhanForm(forms.ModelForm):
    class Meta:
        model = NhomNhanBaoCao
        fields = ['ten', 'mo_ta']

    ten = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "nhomNhanName",
                "placeholder": "Tên nhóm nhận"
            }
        )
    )

    mo_ta = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "nhomNhanDescription",
                "rows": 3,
                "placeholder": "Mô tả nhóm nhận"
            }
        )
    )

class SuaNhomChiaSeForm(forms.ModelForm):
    class Meta:
        model = NhomChiaSe
        fields = ['ten', 'mo_ta']

    ten = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "nhomChiaSeName",
                "placeholder": "Tên nhóm chia sẻ"
            }
        )
    )

    mo_ta = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "nhomChiaSeDescription",
                "rows": 3,
                "placeholder": "Mô tả nhóm chia sẻ"
            }
        )
    )

class ThemMayTinhKetNoiForm(forms.ModelForm):
    phong = forms.ModelChoiceField(
        queryset=Phong.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "phongSelect",
                "placeholder": "Chọn phòng"
            }
        )
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = MayTinhKetNoi
        fields = ['ten', 'ip', 'mac', 'mo_ta', 'khoa', 'ngay_het_han_khoa', 'phong', 'chu_so_huu']
        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'mayTinhTen',
                'placeholder': 'Tên máy tính'
            }),
            'ip': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'mayTinhIP',
                'placeholder': 'Địa chỉ IP'
            }),
            'mac': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'mayTinhMAC',
                'placeholder': 'Địa chỉ MAC'
            }),
            'mo_ta': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'mayTinhMoTa',
                'rows': 3,
                'placeholder': 'Mô tả máy tính'
            }),
            'khoa': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'mayTinhKhoa',
                'placeholder': 'Khóa'
            }),
            'ngay_het_han_khoa': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'id': 'mayTinhNgayHetHanKhoa',
                'type': 'datetime-local',
                'placeholder': 'Ngày hết hạn khóa'
            }),
            'chu_so_huu': forms.Select(attrs={
                'class': 'form-select',
                'id': 'mayTinhChuSoHuu',
                'placeholder': 'Chọn người quản lý'
            })
        }
        
class SuaMayTinhKetNoiForm(forms.ModelForm):
    phong = forms.ModelChoiceField(
        queryset=Phong.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "id": "phongSelect",
                "placeholder": "Chọn phòng"
            }
        )
    )
    
    def __init__(self, *args, **kwargs):
        super(SuaMayTinhKetNoiForm, self).__init__(*args, **kwargs)

    class Meta:
        model = MayTinhKetNoi
        fields = ['ten', 'ip', 'mac', 'mo_ta', 'khoa', 'ngay_het_han_khoa', 'phong', 'chu_so_huu']
        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'mayTinhTen',
                'placeholder': 'Tên máy tính'
            }),
            'ip': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'mayTinhIP',
                'placeholder': 'Địa chỉ IP'
            }),
            'mac': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'mayTinhMAC',
                'placeholder': 'Địa chỉ MAC'
            }),
            'mo_ta': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'mayTinhMoTa',
                'rows': 3,
                'placeholder': 'Mô tả máy tính'
            }),
            'khoa': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'mayTinhKhoa',
                'placeholder': 'Khóa'
            }),
            'ngay_het_han_khoa': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'id': 'mayTinhNgayHetHanKhoa',
                'type': 'datetime-local',
                'placeholder': 'Ngày hết hạn khóa'
            }),
            'chu_so_huu': forms.Select(attrs={
                'class': 'form-select',
                'id': 'mayTinhChuSoHuu',
                'placeholder': 'Chọn người quản lý'
            })
        }
   
            
class ThemChucVuForm(forms.ModelForm):
    class Meta:
        model = ChucVu
        fields = ['ten', 'mo_ta']
        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'chucVuTen',
                'placeholder': 'Tên chức vụ'
            }),
            'mo_ta': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'chucVuMoTa',
                'rows': 3,
                'placeholder': 'Mô tả chức vụ'
            })
        }
class SuaChucVuForm(forms.ModelForm):
    class Meta:
        model = ChucVu
        fields = ['ten', 'mo_ta']
        widgets = {
            'ten': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'chucVuTen',
                'placeholder': 'Tên chức vụ'
            }),
            'mo_ta': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'chucVuMoTa',
                'rows': 3,
                'placeholder': 'Mô tả chức vụ'
            })
        }

class ThemQuyTrinhForm(forms.Form):
    class Meta:
        models = QuyTrinh
        fields = ['ten_quy_trinh', 'mo_ta', 'loai_quy_trinh', 'nguoi_duyet', 'phong']

    ten_quy_trinh = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'procedureName',
                'placeholder': 'quy trình 1'
            }
        )
    )

    mo_ta = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'procedureDescription',
                'rows': 3,
                'placeholder': 'quy trình 1 là ...'
            }
        )   
    )

    loai_quy_trinh = forms.ModelChoiceField(
        queryset=LoaiQuyTrinh.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'procedureCategory',
            }
        )
    )

    nguoi_duyet = forms.ModelChoiceField(
        queryset=NhanVien.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'procedureManCheck'
            }
        )
    )

    phong = forms.ModelChoiceField(
        queryset=Phong.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'procedureRoom'
            }
        )
    )

class ThemBuocForm(forms.Form):
    class Meta:
        models = Buoc
        fields = ['ten_buoc', 'thu_tu', 'tai_lieu_mo_ta', 'yeu_cau', 'id_DoiTuong']
    
    ten_buoc = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'stepName',
                'placeholder': 'buoc danh gia'
            }
        )
    )

    thu_tu = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'stepNumber',
                'placeholder': 'buoc 1'
            }
        )
    )

    tai_lieu_mo_ta = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'tailieumota'
            }
        )
    )

    yeu_cau = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'yeucau',
                'placeholder': 'Bước này cần...'
            }
        )
    )

    id_DoiTuong = forms.ModelChoiceField(
        queryset=DoiTuongDanhGia.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'doituong'
            }
        )
    )

class ThemQuyTrinhBuocForm(forms.Form):
    class Meta:
        models = QuyTrinhBuoc
        fields = ['id_QuyTrinh', 'id_Buoc']
    
    id_QuyTrinh = forms.ModelChoiceField(
        queryset=QuyTrinh.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'procedureStep'
            }
        )
    )

    id_Buoc = forms.ModelChoiceField(
        queryset=Buoc.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'stepProcedure'
            }
        )
    )

class ThemKichBanForm(forms.Form):
    class Meta: 
        models = KichBan
        fields = ['ten', 'mo_ta', 'tai_lieu', 'id_QuyTrinhPhienBan']
    
    ten = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'tenkichban',
            }
        )
    )

    mo_ta = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'mota',
            }
        )
    )

    tai_lieu = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'tailieu',
                'placeholder': 'local path'
            }
        )
    )

    id_MauKichBan = forms.ModelChoiceField(
        queryset=MauKichBan.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'maukichban'
            }
        )
    )

    id_QuyTrinhPhienBan = forms.ModelChoiceField(
        queryset=QuyTrinhPhienBan.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'quytrinh'
            }
        )
    )

class ThemRuiRoForm(forms.Form):
    class Meta:
        models = RuiRo
        fields = ['ten', 'mo_ta', 'nguoi_lap', 'loai_rui_ro', 'du_an']
    
    ten = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'tenruiro',
            }
        )
    )

    mo_ta = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'mota',
            }
        )
    )

    nguoi_lap = forms.ModelChoiceField(
        queryset=NhanVien.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'nguoilap'
            }
        )
    )

    loai_rui_ro = forms.ModelChoiceField(
        queryset=LoaiRuiRo.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'loairuiro'
            }
        )
    )

    du_an = forms.ModelChoiceField(
        queryset=DuAn.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'duan'
            }
        )
    )