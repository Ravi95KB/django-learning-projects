from django import forms
from AppTwo.models import User

class NewUserForm(forms.ModelForm):
    #If we want custom validations then define it outside the Meta class.
    class Meta:
        model = User
        fields = '__all__'    #For getting all the fields from the model.
