from django import forms
from .models import *

class ThemNguonLoHongForm(forms.Form):
    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project')
        super(ThemNguonLoHongForm, self).__init__(*args, **kwargs)
    
    ten_nguon = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "sourceName",
                "placeholder": "Common Vulnerabilities and Exposures"
            }
        )
    )

    ky_hieu = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "sourceCode",
                "placeholder": "CVE"
            }
        )
    )

    mo_ta = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "sourceDescription",
                "rows": 3
            }
        )
    )
    
    duong_dan = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "sourceUrl",
                "placeholder": "https://",
                "type": "url"
            }
        )
    )

    def clean_ten_nguon(self):
        data = self.cleaned_data['ten_nguon']
        if NguonLoHong.objects.filter(ten_nguon=data).count() > 0:
            raise forms.ValidationError(f"{data} đã tồn tại")
        return data

class ThemLoaiLoHongForm(forms.Form):
    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project')
        super(ThemLoaiLoHongForm, self).__init__(*args, **kwargs)
    
    ten_loai = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "categoryName",
                "placeholder": "Category of Vulnerable"
            }
        )
    )

    mo_ta = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "categoryDescription",
                "rows": 3
            }
        )
    )

    def clean_ten_loai(self):
        data = self.cleaned_data['ten_loai']
        if LoaiLoHong.objects.filter(ten_loai=data).count() > 0:
            raise forms.ValidationError(f"{data} đã tồn tại")
        return data

class ThemLoHongForm(forms.Form):
    class Meta:
        model = LoHong
        fields = ['ten_lo_hong', 'mo_ta', 'muc_do', 'id_LoaiLoHong', 'id_NguonLoHong', 'id_BienPhap']

    ten_lo_hong = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "vulnerabilityName",
                "placeholder": "Tên lỗ hổng"
            }
        )
    )

    mo_ta = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "description",
                "placeholder": "Mô tả",
                "rows": 5
            }
        )
    )

    MUC_DO_CHOICES = [
        ('critical', 'Critical'),
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
        ('info', 'Info')
    ]
    muc_do = forms.CharField(
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select",
                "id": "severityLevel",
                "placeholder": "Mức độ lỗ hổng"
            },
            choices=MUC_DO_CHOICES
        )
    )

    id_LoaiLoHong = forms.ModelChoiceField(
        queryset=LoaiLoHong.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select",
                "id": "vulnerabilityType",
                "placeholder": "Loại lỗ hổng"
            },
        )
    )

    id_NguonLoHong = forms.ModelChoiceField(
        queryset=NguonLoHong.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select",
                "id": "vulnerabilitySource",
                "placeholder": "Nguồn lỗ hổng"
            },
        )
    )

    id_BienPhap = forms.ModelChoiceField(
        queryset=BienPhap.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={
                "class": "form-select",
                "id": "remediationOne",
                "placeholder": "Cách khắc phục"
            },
        )
    )

    def clean_ten_lo_hong(self):
        data = self.cleaned_data['ten_lo_hong']
        if LoHong.objects.filter(ten_lo_hong=data).exists():
            raise forms.ValidationError(f"Tên lỗ hổng {data} đã tồn tại")
        return data

class ThemBienPhapForm(forms.ModelForm):
    class Meta:
        model = BienPhap
        fields = ['ten_bien_phap', 'mo_ta']
    
    ten_bien_phap = forms.CharField(
        label='Tên cách khắc phục',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "ten_bienphap",
                "placeholder": "Biện pháp 1"
            }
        )
    )

    mo_ta = forms.CharField(
        label='Mô tả',
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "mo_ta_bienphap",
                "rows": 3,
                "placeholder": "Mô tả biện pháp"
            }
        ),
        required=False
    )

class SuaNguonLoHongForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SuaNguonLoHongForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = NguonLoHong
        fields = ['ten_nguon', 'ky_hieu', 'mo_ta', 'duong_dan']

    ten_nguon = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "sourceName",
                "placeholder": "Common Vulnerabilities and Exposures"
            }
        )
    )

    ky_hieu = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "sourceCode",
                "placeholder": "CVE"
            }
        )
    )

    mo_ta = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "id": "sourceDescription",
                "rows": 3
            }
        )
    )
    
    duong_dan = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "sourceUrl",
                "placeholder": "https://",
                "type": "url"
            }
        )
    )

    def set_value(self, nguonlohong_value, ky_hieu_value, mo_ta_value, duong_dan_value):
        self.initial['ten_nguon'] = nguonlohong_value
        self.initial['ky_hieu'] = ky_hieu_value
        self.initial['mo_ta'] = mo_ta_value
        self.initial['duong_dan'] = duong_dan_value
        
# Form for Nen Tang Phat Trien
class NenTangPhatTrienForm(forms.ModelForm):
    class Meta:
        model = NenTangPhatTrien
        fields = ['ten', 'mo_ta']
    
    ten = forms.CharField(
        label='Nền tảng phát triển',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'ten_nentang',  # id matches for JS
            'placeholder': 'Nền tảng phát triển'
        })
    )
    
    mo_ta = forms.CharField(
        label='Mô tả',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'mo_ta_nentang',  # id matches for JS
            'rows': 3,
            'placeholder': 'Mô tả nền tảng'
        }),
        required=False
    )

# Form for Giai Doan Phat Trien
class GiaiDoanPhatTrienForm(forms.ModelForm):
    class Meta:
        model = GiaiDoanPhatTrien
        fields = ['ten', 'mo_ta']
    
    ten = forms.CharField(
        label='Giai đoạn phát triển',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'ten_giaidoan',  # id matches for JS
            'placeholder': 'Giai đoạn phát triển'
        })
    )
    
    mo_ta = forms.CharField(
        label='Mô tả',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'mo_ta_giaidoan',  # id matches for JS
            'rows': 3,
            'placeholder': 'Mô tả giai đoạn'
        }),
        required=False
    )

class HoSoPhanMemForm(forms.ModelForm):
    class Meta:
        model = HoSoPhanMem
        fields = ['nguoi_them', 'phien_ban', 'giai_doan', 'nen_tang', 'mo_ta', 'tai_lieu']
        widgets = {
            'nguoi_them': forms.TextInput(attrs={
                'class': 'form-control',
                'value': 'Nguyễn Văn ABC',
                'readonly': True,
                'id': 'nguoi_them',
                
            }),
            'phien_ban': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 70px;',
                'value': '1',
                'id': 'phien_ban'
            }),
            'giai_doan': forms.Select(attrs={
                'class': 'form-select',
                'aria-label': 'Chọn giai đoạn phát triển',
                'id': 'giai_doan'}),
            'nen_tang': forms.Select(attrs={
                'class': 'form-select',
                'aria-label': 'Chọn nền táng phát triển',
                'id': 'nen_tang'}),
            'mo_ta': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'CVE - Common Vulnerabilities and Exposures',
                'id': 'mo_ta'
            }),
            'tai_lieu': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'tai_lieu',
                'multiple': '',
                'accept': '.pdf,.zip'  # Limit file types to pdf and zip
            })
        }