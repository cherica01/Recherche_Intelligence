import google.generativeai as genai
from django.shortcuts import render
from .models import Produit
from .forms import RechercheForm

# Configuration de l'API Google Generative AI
GEMINI_API_KEY ="AIzaSyDHjOrj5AeGEOBJpI5sBbc0t8dqJ0fA_Sk"  
genai.configure(api_key=GEMINI_API_KEY)

def produits_view(request):
    produits = Produit.objects.all()
    form = RechercheForm()
    resultats = []

    if request.method == "POST":
        form = RechercheForm(request.POST)
        if form.is_valid():
            mot_cle = form.cleaned_data["mot_cle"]

            
            produits_context = "\n".join(
                f"{produit.nom}: {produit.description}, prix {produit.prix} EURO"
                for produit in produits
            )

            
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                prompt = (
                    f"Voici une liste de produits :\n{produits_context}\n\n"
                    f"Question : Quels produits correspondent au mot-clé '{mot_cle}' et pourquoi , repondez juste en une phrase?"
                )
                response = model.generate_content(prompt)

                
                resultats_text = response.text.split("\n")
                resultats = [ligne for ligne in resultats_text if ligne.strip()]  

            except Exception as e:
                print(f"Erreur lors de l'appel à Gemini : {e}")

    return render(request, "produits/produits.html", {
        "produits": produits,
        "form": form,
        "resultats": resultats,
    })
