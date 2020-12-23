from django import forms
from django.core import validators

#Custom validator function needs to be defined outside the class
def check_for_z(value):
    "Checking the first letter of the name should start with z"
    if value[0].lower() != 'z':
        raise forms.ValidationError("Needs to start with Z!")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    botCatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                validators = [validators.MaxLengthValidator(0)]) #Makes the field hidden/invisble from the user

    def clean(self):
        all_clean_data = super().clean() #This gets all the data in the form.
        email = all_clean_data["email"]
        vmail = all_clean_data["verify_email"]

        if email != vmail:
            raise forms.ValidationError("Please match your emails!")


    #Custom made Code to catch a bot trying to access the WebPage
    #botCatcher = forms.CharField(required=False, widget=forms.HiddenInput) #Makes the field hidden/invisble from the user.

    # def clean_botCatcher(self):
    #     botCatcher = self.cleaned_data['botCatcher']
    #     if len(botCatcher) > 0:
    #         raise forms.ValidationError('GOTCHA BOT!')
    #     return botCatcher
