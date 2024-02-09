from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'id': 'name', 'class': 'form__input', 'placeholder': " "}
        )
    )