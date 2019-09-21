from django.forms import ModelForm
from .models import Member


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = {'name', 'last_name', 'department', 'post', 'leader'}

