from django.shortcuts import render, get_object_or_404, HttpResponse

from .models import N

from django.contrib.auth.decorators import login_required as lr

@lr
def h(r):

    u = r.user
    p = r.user.p

    n = N.objects.filter(u = u)

    c = {}

    c['u'] = u
    c['p'] = p
    c['pi'] = p.n[0].upper()
    c['n'] = n
    c['an'] = p.an

    return render(r, 'a/h.html', c)


# htmx

def a(r):

    r.user.p.an = N.objects.get(uid = r.POST.get('u'))
    r.user.p.save()

    return HttpResponse('K')

def cn(r):

    u = r.user

    n = N.objects.create(u = u)

    u.p.an = n
    u.p.save()

    n = N.objects.filter(u = u)

    return render(r, 'a/nl.html', {'n': n, 'an': u.p.an})

def p(r):

    u = r.user

    u.p.an.p = not u.p.an.p
    
    u.p.an.save()

    n = N.objects.filter(u = u)

    c = {}

    c['n'] = n
    c['an'] = u.p.an

    return render(r, 'a/nl.html', c)

def d(r):

    u = r.user

    n = u.p.an

    u.p.an = None
    u.p.save()

    n.delete()

    n = N.objects.filter(u = u)

    u.p.an = n[0]
    u.p.save()
    an = u.p.an

    return render(r, 'a/nl.html', {'n': n, 'an': an})


# ajax


def t(r):

    u = r.POST.get('u')
    t = r.POST.get('t')

    n = get_object_or_404(N, uid = u)

    n.t = t
    n.save()

    return HttpResponse('K')

def c(r):

    u = r.POST.get('u')
    c = r.POST.get('c')

    n = get_object_or_404(N, uid = u)

    n.c = c
    n.save()

    return HttpResponse('K')