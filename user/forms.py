from django import forms
from django.contrib.auth.models import User
from user.models import UserProfile

# from user.models import Profile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)        
        self.fields['email'].widget.attrs['readonly']="true"

class InfoForm(forms.ModelForm):
     
    class Meta:
        model=UserProfile
        widgets={
                'last_updated': forms.DateInput(attrs={'class':'datepicker'}),
            }
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super(InfoForm, self).__init__(*args, **kwargs)
        self.fields['latitude'].widget.attrs['readonly']="true"
        self.fields['longitude'].widget.attrs['readonly']="true"

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'               
            })
            if(field=='last_updated'):
                self.fields[field].widget.attrs.update({
                'class': 'datepicker form-control'               
                })
            if(field=='opening_time'):
                self.fields[field].widget.attrs.update({
                'class': 'timepicker form-control'               
                })
            self.fields[field].widget.attrs['cols'] = 10
            self.fields[field].widget.attrs['rows'] = 4
class otpForm(forms.Form):
    otp = forms.CharField(label='OTP', max_length=4)
       
