from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django import forms

from blog.forms import ArticleForm

from .models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def show(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/show.html', {'article': article})

def contact(request):
    if request.method == 'POST': # S'il s'agit d'une requête POST
        form = ArticleForm(request.POST) # Nous reprenons les données

        if form.is_valid(): # Nous vérifions que les données envoyées sont valides

            # Ici nous pouvons traiter les données du formulaire
            titre = form.cleaned_data['titre']
            auteur = form.cleaned_data['auteur']
            contenu = form.cleaned_data['contenu']

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
            envoi = True
            form.save()

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = ArticleForm() # Nous créons un formulaire vide

    return render(request, 'blog/contact.html', locals())
