from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm

# Create your views here.

def register(request):

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save() # Actually put the new user into the model/db
            username = form.cleaned_data.get("username")
            messages.success(request, f"User {username} successfully created.")
            return redirect("sharks-home")
    else:
        form = UserRegistrationForm()
    
    return render(request, "registration.html", { "form" : form })