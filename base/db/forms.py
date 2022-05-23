from django import forms
from .models import Db


class DbForm(forms.ModelForm):
    class Meta:
        model = Db
        fields = ('surname', 'name', 'patronymic', 'pin', 'address', 'pin_bank', 'erp', 'image', 'image1', 'image2',)
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
                       "placeholder": "Номер ЕРП",
                        "rows": 5,
                       }),

            "image": forms.FileInput(
                attrs={"class": "form-control",

                       "placeholder": "",


                       }),
            "image1": forms.FileInput(
                attrs={"class": "form-control",
                       "placeholder": "",
                       "id": "imgInp",
                       "type": "file",
                       }),
            "image2": forms.FileInput(
                attrs={"class": "form-control",
                       "placeholder": ""
                       }),

        }