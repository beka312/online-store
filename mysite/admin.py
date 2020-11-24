from django import forms

from django.forms import ModelChoiceField
from django.contrib import admin

from .models import *



# class NoteBookAdmin(admin.ModelAdmin):
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'category':
#             return ModelChoiceField(Category.objects.filter(slug='notebook'))
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
#
#
# class SmartPhoneAdmin(admin.ModelAdmin):
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'category':
#             return ModelChoiceField(Category.objects.filter(slug='smartphone'))
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(Category)
admin.site.register(Product)
# admin.site.register(Notebook, NoteBookAdmin)
# admin.site.register(SmartPhone, SmartPhoneAdmin)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)
