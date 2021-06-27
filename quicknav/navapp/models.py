from django.db import models

# Create your models here.

class NavItem(models.Model):
    text = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    class_type = models.CharField(max_length=200)

    is_admin = models.BooleanField(default=True)

class NavTemplate(models.Model):
    items = models.ManyToManyField(NavItem)
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=100)

def get_actual_template(request):
    datas = NavTemplate.objects.filter(is_active=True)

    assert len(datas) == 1

    return datas[0]

def get_templates(request):
    return NavTemplate.objects.all()

def get_authorized_items(request):
    template = get_actual_template(request)

    if request.user.is_staff:
        return template.items.all()
    elif request.user.is_authenticated:
        return template.items.filter(is_admin=False)
    return []

def toggle_active(to_toggle=-1):
    nvtem = NavTemplate.objects.filter(id=to_toggle)

    assert len(nvtem) < 2
    
    actual = False
    if len(nvtem) == 1:
        nvtem = nvtem[0]
        actual = nvtem.is_active
    else:
        nvtem = None
    
    for templ in NavTemplate.objects.filter(is_active=True):
        templ.is_active = False
        templ.save()

    nvtem.is_active = not actual
    nvtem.save()

def verify_item_presence(form):
    try:
        assert "class" in form.keys()
        assert "text" in form.keys()
        assert "url" in form.keys()
    except AssertionError as e:
        return 0
    return None

def verify_item_form(form, id):
    try:
        assert len(NavItem.objects.filter(id=id)) == 1

        assert verify_item_presence(form) == None
    except AssertionError as e:
        return 0
    return None

def modify_item(form, id):
    assert verify_item_form(form, id) == None

    item = NavItem.objects.filter(id=id)[0]

    item.text = form["text"]
    item.url = form["url"]
    item.class_type = form["class"]
    item.is_admin = "is_admin" in form.keys()

    item.save()

def create_item(form):
    item = NavItem.objects.create()

    modify_item(form, item.id)

    return item

def remove_item(temp_id, it_id):
    try:
        assert len(NavTemplate.objects.filter(id=temp_id)) == 1
        assert len(NavItem.objects.filter(id=it_id)) == 1
    except AssertionError as e:
        return 0

    NavTemplate.objects.filter(id=temp_id)[0].items.remove(NavItem.objects.filter(id=it_id)[0])
    NavItem.objects.filter(id=it_id)[0].delete()

    return None
