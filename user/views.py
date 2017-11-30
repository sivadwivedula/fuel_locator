from django.views.generic.list import ListView
import messages
from user.models import Notice, UserProfile, Noticeforowner
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
import json
from user.forms import UserProfileForm, InfoForm, otpForm
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.views.generic.list import ListView
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render_to_response, render, redirect
from django.views.generic.edit import FormView, BaseFormView
from django.db import transaction
from django.contrib.messages.context_processors import messages
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory, modelformset_factory
from django.core.exceptions import PermissionDenied
from random import randint
#from user import way2sms
count=0
otp=3366
mobile=9826150156
form=None
class gov_notice(ListView):
    template_name = 'gov_notice.html'
    context_object_name = 'nl'
    def get_queryset(self):
        return Notice.objects.order_by('cr_date')[:5]
class gov_notice_details(generic.DetailView):
    model = Notice
    template_name = 'gov_notice_details.html'
    context_object_name = 'nl'
@method_decorator(login_required, name='dispatch')
class fuel_list(generic.ListView):
    model = UserProfile
    template_name = 'fuel_list.html'
    context_object_name = 'nl'
    def get_queryset(self):
        return Noticeforowner.objects.order_by('cr_date')[:5]
@login_required
def update_user_details(request, pk):
    user = User.objects.get(pk=pk)
    user_form = UserProfileForm(instance=user)
    ProfileInlineFormset = inlineformset_factory(User, UserProfile, form=InfoForm,extra=0,can_delete=False)
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/')
        return render(request, "account_update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied


# #TOCHANGE
class PostExample(TemplateView):
    template_name='test.html'    
    def post(self, request):
#         return redirect("user/account/update/"+ str(request.user.id));
        print(request.POST)
        return HttpResponse(json.dumps({'key': 'value'}), content_type="application/json")
    
    
    
def get_otp(request):
    # if this is a POST request we need to process the form data
   
    if request.method == 'POST' :
        global form
        form = otpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            otp1 = request.POST['otp']
            print(otp1,"otp1")
            print(otp,"otp")
            if otp == otp1:
                return HttpResponse('Hola')
            
    # if a GET (or any other method) we'll create a blank form
    else:
       
        form = otpForm()
        return render(request, 'otp.html', {'form': form})       
    
#def otp_gen(request):
#      
#         global otp,mobile
#         otp = randint(1000, 9999)  
#         print(otp,mobile,"otp_gen")
#         if form != "":
#                 q = way2sms.sms('7000728428','kuchbhi')  
#                     
#                 q.send(str(mobile), 'otp for verification fuel locator registration is ' + str(otp))          
#                 q.msgSentToday()
#                 q.logout()
#                 return redirect('settings:otp')
#         else:
#             return HttpResponse("lol")    