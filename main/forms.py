from django import forms
from .models import Service, ServiceImage


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            "name",
            "category",
            "price",
            "description",
            "city",
            "address",
            "phone_number",
            "main_image",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "category": forms.Select(attrs={"class": "form-control"}),
            "price": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control-desc",
                    "rows": 6,
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                }
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "main_image": forms.FileInput(
                attrs={"class": "form-control-file", "accept": "image/*"}
            ),
        }
        labels = {
            "name": "Название услуги *",
            "category": "Категория *",
            "price": "Цена (руб.) *",
            "description": "Описание *",
            "city": "Город *",
            "address": "Адрес",
            "phone_number": "Контактный телефон *",
            "main_image": "Главное изображение *",
        }
        help_texts = {
            "phone_number": "Введите номер в международном формате",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["city"].required = True
        self.fields["address"].required = False

        self.fields["category"].empty_label = "Выберите категорию"


    def clean_name(self):

        name = self.cleaned_data.get("name")
        if name and len(name) > 40:
            raise forms.ValidationError("Название не может быть длиннее 40 символов")
        return name


    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")
        if not phone:
            raise forms.ValidationError("Это поле обязательно")
        
        cleaned = "".join(filter(str.isdigit, phone))
        
        if len(cleaned) < 10:
            raise forms.ValidationError("Введите корректный номер телефона (не менее 10 цифр)")
        if len(cleaned) > 15:
            raise forms.ValidationError("Номер телефона слишком длинный")
        
        if cleaned[0] not in ['7', '8'] and len(cleaned) == 11:
            raise forms.ValidationError("Номер должен начинаться с 7 или 8")
            
        return phone

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price and price <= 0:
            raise forms.ValidationError("Цена должна быть больше 0")
        return price

