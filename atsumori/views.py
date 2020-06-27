from django.shortcuts import render

def user_list(request):
    return render(request, 'atsumori/user_list.html', {})
