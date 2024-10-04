from modeltranslation.translator import register, TranslationOptions
from .models import Book

@register(Book)
class BookTranslation(TranslationOptions):
    fields = ['name', 'description']