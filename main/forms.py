from django import forms


class getInTouchForm(forms.Form):
    fullname = forms.CharField(max_length=100, label = "Full Name")
    email = forms.EmailField()
    phone = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
