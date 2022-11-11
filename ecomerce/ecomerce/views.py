
from django.shortcuts import render
from .formss import ContactForm
def home_page(request):
    return render(request,"home/home_page.html",{})

def about_page(request):
    context = {
        "teste":"teste var"
    }
    return render(request,"about/about_page.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"teste formulário",
        "content": "Bem-vindo a página sobre contato",
        "form": contact_form
    }
    if request.method == "POST":
        print(request.POST)
    return render(request,"contact/contact_page.html",context)