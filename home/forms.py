# from django import forms
# from .models import FeeReceipt

# class FeeReceiptForm(forms.ModelForm):
#     class Meta:
#         model = FeeReceipt
#         fields = ['student_name', 'message', 'receipt_image']
from django import forms
from .models import FeeReceipt

class FeeReceiptForm(forms.ModelForm):
    class Meta:
        model = FeeReceipt
        fields = ['student_name', 'message', 'receipt_image']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'receipt_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
