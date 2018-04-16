from django.shortcuts import *
from django.views.generic import TemplateView
from chat.forms import FindUserForm
import json
from accounts.models import User
from chat.models import Conversations, Participants, Messages, Friends
from django.db.models import Q # filter or

class HomeView(TemplateView):
    template_name = 'chat/home.html'

    def get(self, request):
        find_user_form = FindUserForm()
        args = {'find_user_form':find_user_form, }
        return render(request, self.template_name, args)

    def post(self, request):
        print(request.POST.get('type'))
        if request.POST.get('type')=='find_user_form' :
            ans={}
            results=None;
            form = FindUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['user']
                #print(username)
                try:
                    results = User.objects.filter(username__contains=username)
                    oldFriendsOne = Friends.objects.values_list('user_two', flat=True).filter(user_one=request.user)
                    oldFriendsTwo = Friends.objects.values_list('user_one', flat=True).filter(user_two=request.user)
                    #print(oldFriends)
                    resulTab=[]

                    #print(results)

                    for i in results:
                        if i != request.user and i.id not in oldFriendsOne and i.id not in oldFriendsTwo :

                            print(i)
                            foudUser={'first_name': i.first_name,
                            'last_name' : i.last_name,
                            'username' : i.username}
                            resulTab.append(foudUser)
                    ans = {'users':resulTab}
                except User.DoesNotExist:
                    results=None;
            else:
                ans={'user': 'user'}
        elif request.POST.get('type')=='add_user':
            #print(User.objects.get(username=request.POST.get('user')))
            #print(request.user.get_full_name())
            friend = User.objects.get(username=request.POST.get('user'))
            user = request.user
            queryConv = Conversations(name=friend.get_full_name()+" - "+user.get_full_name(), creator = user)
            #print(query)
            queryConv.save()
            queryAdd = Participants(conversation=queryConv, user=friend)
            queryAdd.save()
            queryAdd = Participants(conversation=queryConv, user=user)
            queryAdd.save()
            setFriends= Friends(user_one= user, user_two=friend)
            setFriends.save()
            startMessage = Messages(conversation=queryConv, user = user, message = '@server Rozpoczęto Rozmowę')
            startMessage.save()
            ans={'flag': 'Done'}
        elif request.POST.get('type')=='load_conversations':
            conversations = Participants.objects.filter(user = request.user)
            resulTab=[]
            for i in conversations:
                name = i.conversation.name
                id = i.conversation.id
                lastMsg = Messages.objects.filter(conversation=i.conversation).order_by('-id')[:1]
                lastMsg = lastMsg[0].message
                foundConversation={
                'id':id, 'name':name, 'lastMsg':lastMsg
                }
                #print(name)
                resulTab.append(foundConversation)
                ans={'flag':'Found', 'conversations':resulTab}

        elif request.POST.get('type')=='load_chat':
            conv = request.POST.get('conv')
            name = Conversations.objects.filter(id = conv)[0].name
            messages = Messages.objects.filter(conversation = conv).order_by('id')
            resultTab=[]
            for msg in messages:
                user= msg.user.get_full_name()
                message = msg.message
                sent_time = msg.sent_time.__str__()[:-16]
                foundMessage={'user':user,'message':message, 'sent_time':sent_time}
                resultTab.append(foundMessage)

            ans={'flag': 'Found', 'messages':resultTab, 'name':name, 'user':request.user.get_full_name()}

        elif request.POST.get('type')=='send_message':
            if (request.POST.get('conversation')!=None)and (request.POST.get('message')!=None):
                user = request.user
                msg = request.POST.get('message')

                conv = request.POST.get('conversation')
                print(conv)
                message = Messages(conversation_id=conv, user=user, message=msg)
                message.save()
                ans={'flag': 'Done'}
            else:
                ans={'flag': 'Error'}
        #ans=['aaa','as']
        print(json.dumps(ans))
        return  HttpResponse(json.dumps(ans))
