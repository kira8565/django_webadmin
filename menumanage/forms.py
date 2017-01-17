from django.forms import ModelForm

from menumanage.models import SysMenu


class MenuForm(ModelForm):
    class Meta:
        model = SysMenu
        fields = '__all__'
