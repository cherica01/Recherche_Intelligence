from django import forms

class RechercheForm(forms.Form):
    mot_cle = forms.CharField(
        max_length=100,
        required=True,
        label="Recherche",
        widget=forms.TextInput(attrs={
            'class': 'w-full sm:w-3/4 md:w-2/3 px-10 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-400 focus:outline-none text-gray-700 shadow-sm',
            'placeholder': 'Rechercher...',
        })
    )
