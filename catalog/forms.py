from django import forms

from catalog.models import Product
from version.models import Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        name = self.cleaned_data.get('name').lower()

        for word in forbidden_words:
            if word in name:
                raise forms.ValidationError(f"Запрещенное слово '{word}' в имени продукта.")

        return name

    def clean_description(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        description = self.cleaned_data.get('description').lower()

        for word in forbidden_words:
            if word in description:
                raise forms.ValidationError(f"Запрещенное слово '{word}' в описании продукта.")

        return description


# class VersionForm(forms.ModelForm):
#     class Meta:
#         model = Version
#         fields = ['version_number', 'version_name', 'version_status']
