from django.contrib import admin
from .models import djangoClasses


class djangoClassesAdmin(admin.ModelAdmin):
    fields = ['Title', 'Course', 'Instructor', 'Duration']


admin.site.register(djangoClasses, djangoClassesAdmin)
