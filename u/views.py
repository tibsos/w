from django.shortcuts import render, redirect, reverse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm as UCF

from a.models import N

def l(r):

    if r.user.is_authenticated:

        return redirect('a:h')

    else:
        
        if r.method == 'POST':


            u = r.POST.get('u')
            p = r.POST.get('p')

            u = authenticate(username = u, password = p)

            if u:

                login(r, u)

                return redirect('a:h')
            
            else:

                return render(r, 'u/l.html',{'e': True})
    
    return render(r, 'u/l.html')


def r(r):

    if r.method == 'POST':

        n = r.POST.get('n')

        u = r.POST.get('username')
        p = r.POST.get('password1')

        _mutable = r.POST._mutable
        r.POST._mutable = True
        r.POST['password2'] = p
        r.POST.pop('n', None)
        r.POST._mutable = _mutable

        f = UCF(r.POST)

        if f.is_valid():

            u = f.save()

            u.p.n = n

            n = N.objects.create(u = u)

            u.p.an = n
            u.p.save()

            u = authenticate(username = u, password = p)

            login(r, u)

            return redirect('a:h')


    return render(r, 'u/r.html')
