from django.contrib import admin
from .models import Book
from modeltranslation.admin import TranslationAdmin

# Register your models here.
@admin.register(Book)
class BookTranslationAdmin(TranslationAdmin):
    pass
