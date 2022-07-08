from.models import GlowhiteMeta

def metalinks(request):
    if GlowhiteMeta.objects.filter(id = 1).exists() :
        ml = GlowhiteMeta.objects.get(id = 1)
        d1 = {'ml':ml}
    else:
        d1={'ml':'Glowhite'}
    return d1
    