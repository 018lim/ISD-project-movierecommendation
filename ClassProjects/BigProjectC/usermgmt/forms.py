from django import forms
from usermgmt.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        #field = ['salutation', 'first_name', 'last_name', 'email']
