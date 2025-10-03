from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(
        label='Twój email',
        widget=forms.EmailInput(attrs={
            "class": "block w-full p-2 text-xl rounded-lg w-[60%] border-1 border-slate-800  focus:border-green-800 focus:ring-green-300 "
        })
    )

    temat = forms.CharField(
        label='Temat',
        widget=forms.TextInput(attrs={
            "class": "block  w-full p-3 text-xl rounded-lg border-1 border-slate-800  focus:border-pink-400 focus:ring-pink-400 "
        })
    )
    
    
    message = forms.CharField(
        label='Wiadomość',
        widget=forms.Textarea(attrs={
            "class": "block w-full text-xl  rounded-lg p-2 border-1 border-slate-800  focus:border-green-500 focus:ring-green-500 ",
            "rows": 10
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

   

    

