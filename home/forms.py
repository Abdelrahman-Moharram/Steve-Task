from django import forms
from .models import Book
import datetime


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
    def clean_address(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        if not len(name.strip()):
            raise forms.ValidationError("Book Name shouldn't be null or empty")
        return name.strip()
    
    def clean_address(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        if not len(name.strip()):
            raise forms.ValidationError("Book Name shouldn't be null or empty")
        return name.strip()
    
    def clean_publish_at(self, *args, **kwargs):
        publish_at = self.cleaned_data.get('publish_at')
        if publish_at:
            # publish_at = datetime.strptime(publish_at, '%m/%d/%Y %H:%M:%S')
            if datetime.datetime.today().date() <= publish_at:
                raise forms.ValidationError("Book date should be in the past")
        return publish_at