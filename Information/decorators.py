from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import Info


def if_logged_in(wrapper):
    def func(request, *args, **kwargs):
        if request.user.is_authenticated:
            info = Info.objects.get(user=request.user)
            if info.type_of_user == 'Buyer':
                return HttpResponseRedirect(reverse('homeB'))
            elif info.type_of_user == 'Seller':
                return HttpResponseRedirect(reverse('homeS'))
        else:
            return wrapper(request, *args, **kwargs)
    return func