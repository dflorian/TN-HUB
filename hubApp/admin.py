from django.contrib import admin
from .models import Paper, Backend, Category

admin.site.register(Paper)
admin.site.register(Backend)
admin.site.register(Category)