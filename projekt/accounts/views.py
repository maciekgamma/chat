from django.shortcuts import render
from accounts.forms import RegistrationForm
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form=RegistrationForm()
        args={'form':form}
        return render(request, 'accounts/reg_form.html', args)
