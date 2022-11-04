from django.shortcuts import render

def l(r):

    c = {}
    
    if r.user.is_authenticated:
        
        c['u'] = True

    return render(r, 'l.html', c)