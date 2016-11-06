from django.shortcuts import render
from django.http import HttpResponse

from base.forms import UserProfileForm


def index(request):
    return render(request, 'base.html')

def game(request):
    return render(request, 'base/game.html')

def register(request):

    registered = False

    if request.method == 'POST':
        profile_form = UserProfileForm(data=request.POST)

        if profile_form.is_valid():

            profile = profile_form.save(commit=False)
            profile.save()

            registered = True

        else:
            print(profile_form.errors)

    else:
        profile_form = UserProfileForm()

    return render(request,
                  "base/dummy_register.html",
                  {'profile_form': profile_form,
                   'registered': registered})
