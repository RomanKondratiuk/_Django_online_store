from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('name', 'description', 'image', 'category', 'purchase_price', 'date_of_creation', 'last_modified_date')

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
