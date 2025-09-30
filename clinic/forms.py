from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ContactForm(forms.Form):
    email = forms.EmailField(
        label='Twój email',
        widget=forms.EmailInput(attrs={
            "class": "block w-full p-2 text-xl rounded-lg w-[60%] border-slate-800  focus:border-green-800 focus:ring-green-300 sm:text-sm"
        })
    )

    temat = forms.CharField(
        label='Temat',
        widget=forms.TextInput(attrs={
            "class": "block w-full p-3 text-xl rounded-lg border-slate-800  focus:border-pink-400 focus:ring-pink-400 sm:text-sm"
        })
    )
    
    
    message = forms.CharField(
        label='Wiadomość',
        widget=forms.Textarea(attrs={
            "class": "block w-full  text-lg rounded-lg p-2 border-slate-800  focus:border-green-500 focus:ring-green-500 sm:text-sm",
            "rows": 5
        })
    )
    
    
    AREA_CHOICES = [
        ("urologia", "Urologia"),
        ("kardiologia", "Kardiologia"),
        ("rehabilitacja", "Rehabilitacja"),
    ]

    topic = forms.ChoiceField(
        choices=AREA_CHOICES,
        widget=forms.RadioSelect(
            attrs={"class": "h-4 w-3 text-xl text-indigo-600 border-gray-300 focus:border-green-800 focus:ring-green-500"}
        ),
        label="Specjalizacja"
    )

   

    

