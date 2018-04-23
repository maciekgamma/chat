from django.shortcuts import render
from accounts.forms import RegistrationForm
from django.shortcuts import render, HttpResponse, redirect
from chat.models import Conversations, Participants, Messages
# Create your views here.
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            queryConv = Conversations(name="Witaj w Gamnet", creator = user)
            queryConv.save()
            queryAdd = Participants(conversation=queryConv, user=user)
            queryAdd.save()
            startMessage = Messages(conversation=queryConv, user = user, message = '@server Witaj w Gamnet. Wyszukaj znajomych i zacznij rozmowę!')
            startMessage.save()
            return redirect('/accounts/login')
        else:
            args={'form':form}
            return render(request, 'accounts/reg_form.html', args)
    else:
        form=RegistrationForm()
        args={'form':form}
        return render(request, 'accounts/reg_form.html', args)
