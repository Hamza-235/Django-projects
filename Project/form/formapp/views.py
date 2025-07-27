from django.shortcuts import render,redirect
from .forms import f_form

def formview(request):
    form =f_form()
    if request.method == 'POST':
        form= f_form(request.POST)
        if form.is_valid():
            print("form valid")
            form.save()
            return redirect ("/forms")
    
        else:
            print("unsuccessful")
            print(form.errors)
    return render (request, 'forms.html', {'form':form})
            

# Create your views here.
