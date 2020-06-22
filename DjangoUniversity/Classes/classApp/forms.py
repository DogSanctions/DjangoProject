from django.forms import ModelForm
from .models import djangoClasses


class djangoClassesForm(ModelForm):
    class Meta:
        model = djangoClasses
        fields = '__all__'
