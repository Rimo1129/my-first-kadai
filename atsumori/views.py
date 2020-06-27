from django.shortcuts import render
from django.utils import timezone
from .models import MoriUser

def user_list(request):
    moriusers = MoriUser.objects.filter(fixed_date__lte=timezone.now()).order_by('fixed_date')
    return render(request, 'atsumori/user_list.html', {'moriusers': moriusers})
