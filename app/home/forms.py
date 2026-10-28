from django import forms
from .models import ContactMessage
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    captcha = CaptchaField(label='کد امنیتی', error_messages={
        'required': 'لطفا کد امنیتی را وارد کنید',
        'invalid': 'کد امنیتی وارد شده صحیح نیست'
    })
    
    class Meta:
        model = ContactMessage
        fields = ('full_name', 'phone', 'message')
        
    def clean_full_name(self):
        full_name = self.cleaned_data['full_name'].strip()
        
        if len(full_name) < 3:
            raise forms.ValidationError('نام و نام خانوادگی باید حداقل 3 کاراکتر داشته باشد')
        
        return full_name
    
    def clean_phone(self):
        phone = self.cleaned_data['phone'].strip()
        
        if len(phone) <= 10:
            raise forms.ValidationError('شماره تماس معتبر نمی باشد')
        
        return phone
    
    def clean_message(self):
        message = self.cleaned_data['message'].strip()
        
        if not message:
            raise forms.ValidationError('متن پیام نمی تواند خالی باشد')
        
        return message