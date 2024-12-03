from .models import Data
from django.forms import ModelForm, Textarea

class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = ['oldData']
        widgets = {
            "oldData": Textarea(attrs={
                'class': 'form-control',
                'placeholder' : 'Введите сюда ваши числа через пробел'
            })
        }
