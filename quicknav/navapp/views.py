from django.shortcuts import render, redirect
from django.conf import settings
import navapp.models as models

##############################
# TEMPLATE VIEWS             #
##############################

## List all templates
def list_nvtem(request, *args, **kwargs):
    if not request.user.is_staff:
        return redirect(settings.QUICK_NAV__REDIRECTION)

    return render(request, settings.QUICK_NAV__NAVTEMPLATE_LIST, {"nvtems":models.get_templates(request)})

## Edit template
def edit_nvtem(request, *args, **kwargs):
    if not request.user.is_staff:
        return redirect(settings.QUICK_NAV__REDIRECTION)

    return render(request, settings.QUICK_NAV__NAVTEMPLATE_VIEWER, {
        "nvtem":models.NavTemplate.objects.filter(id=kwargs['id'])[0],
        "items":models.NavTemplate.objects.filter(id=kwargs['id'])[0].items.all()
    })

##############################
# POST VIEWS                 #
##############################

def create_nvtem(request, *args, **kwargs):
    if not request.user.is_staff or not request.method == "POST":
        return redirect(settings.QUICK_NAV__REDIRECTION)
    
    assert "name" in request.POST.keys()

    temp = models.NavTemplate.objects.create(name=request.POST['name'])

    return redirect('/quicknav/admin/'+str(temp.id)+'/edit')

def toggle_nvtem(request, *args, **kwargs):
    if not request.user.is_staff or not request.method == "POST":
        return redirect(settings.QUICK_NAV__REDIRECTION)

    models.toggle_active(to_toggle=kwargs['id'])

    return redirect('/quicknav/admin/'+str(kwargs['id'])+'/edit')

def edit_nvitem(request, *args, **kwargs):
    if not request.user.is_staff or not request.method == "POST":
        return redirect(settings.QUICK_NAV__REDIRECTION)
    
    data = models.verify_item_form(request.POST, kwargs['it_id'])
    if data != None:
        return redirect('/quicknav/admin/'+str(kwargs['id'])+'/edit')

    models.modify_item(request.POST, kwargs['it_id'])

    return redirect('/quicknav/admin/'+str(kwargs['id'])+'/edit')

def create_nvitem(request, *args, **kwargs):
    if not request.user.is_staff or not request.method == "POST":
        return redirect(settings.QUICK_NAV__REDIRECTION)
    
    if len(models.NavTemplate.objects.filter(id=kwargs['id'])) != 1:
        return redirect(settings.QUICK_NAV__REDIRECTION)

    data = models.verify_item_presence(request.POST)
    if data != None:
        return redirect('/quicknav/admin/'+str(kwargs['id'])+'/edit')

    item = models.create_item(request.POST)

    models.NavTemplate.objects.filter(id=kwargs['id'])[0].items.add(item)

    return redirect('/quicknav/admin/'+str(kwargs['id'])+'/edit')

def remove_nvitem(request, *args, **kwargs):
    if not request.user.is_staff or not request.method == "POST":
        return redirect(settings.QUICK_NAV__REDIRECTION)

    models.remove_item(kwargs['id'], kwargs['it_id'])
        
    return redirect('/quicknav/admin/'+str(kwargs['id'])+'/edit')

