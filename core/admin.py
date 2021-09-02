from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin

from .models import *


class FlowerinpotAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and not instance.sd:
            self.fields['pot_size'].widget.attrs.update({
                'readonly': True, 'style': 'background: lightgray;'
            })

    def clean(self):
        if not self.cleaned_data['greeting_card']:
            self.cleaned_data['pot_size'] = None
        return self.cleaned_data


class FlowerAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='flowers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class FlowerinpotAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='flowerinpots'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Flower, FlowerAdmin)
admin.site.register(Flowerinpot, FlowerinpotAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
