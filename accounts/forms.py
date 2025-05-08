from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'date_of_birth',
            'delivery_method',
            'address',
            'phone_number',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'delivery_method': forms.RadioSelect(),
            'address': forms.Textarea(attrs={'rows': 2}),
        }
        labels = {
            'date_of_birth': 'Data nașterii',
            'delivery_method': 'Metodă de livrare',
            'address': 'Adresă',
            'phone_number': 'Telefon',
        }
