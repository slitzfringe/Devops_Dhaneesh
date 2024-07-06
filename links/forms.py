from django import forms

from .models import Link
# class LinkForm(forms.Form):
#     name = forms.CharField(max_length=20)
#     url = forms.URLField(max_length=200)
#     slug = forms.SlugField(required=False)


# django has some better method to store form data 
# directly to the backend!

# using modelForm
class LinkForm(forms.ModelForm):
    
    class Meta:
        model = Link
        fields = ['name', 'url', 'slug']
# the form will be automatically rendered and displays
# this helps us the store the form data directly to 
# the database!