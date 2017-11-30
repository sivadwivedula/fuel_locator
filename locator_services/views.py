from django.shortcuts import render
import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
@login_required()
def contact(request):
    return render(request, "contact.html", {'time' : datetime.datetime.now()})
