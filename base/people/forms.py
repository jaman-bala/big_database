from django import forms
from .models import Passport


class PassportForm(forms.ModelForm):
    class Meta:
        model = Passport
        fields = ('surname', 'name', 'patronymic', 'pin', 'address', 'erp', 'image',)
        widgets = {

            "surname": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Фамилия"
                       }),
            "name": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Имя"
                       }),
            "patronymic": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Отчество"
                       }),
            "pin": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "ПИН"
                       }),
            "address": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Адрес"
                       }),
            "pin_bank": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Номер карточки банка"
                       }),

            "erp": forms.Textarea(
                attrs={"class": "form-control",
                       "placeholder": "Комментарии",
                        "rows": 5,
                       }),

            "image": forms.FileInput(
                attrs={"class": "form-control",

                       "placeholder": "",


                       }),


        }