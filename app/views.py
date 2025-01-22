from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
def insert_topic(request):
    tn=input('enter topic name:')
    to=Topic.objects.get_or_create(topic_name=tn)
    if to[1]:
       lto=Topic.objects.all()
       d={'lto':lto}
       return render(request,'display_topics.html',d) 
    else:
        return HttpResponse('this topic is already present in db')
    

def insert_webpage(request):
    tn=input('enter topic name')
    n=input('enter name')
    url=input('enter url')
    email=input('enter mail')
    lto=Topic.objects.filter(topic_name=tn)
    if lto:
        wo=Webpage.objects.get_or_create(topic_name=lto[0],name=n,uri=url,email=email)
        if wo[1]:
            lwo=Webpage.objects.all()
            
            d={'lwo':lwo}
            return render(request,'display_webpages.html',d)
        else:
            return HttpResponse('this web is already available')
    else:
        return HttpResponse('given topic is not available')
    
def insert_ar(request):
    pk=int(input('enter pk for webpage'))
    author=input('enter author')
    date=input('enter date')
    wlo=Webpage.objects.filter(pk=pk)
    if wlo:
        ato=AccessRecord.objects.get_or_create(name=wlo[1],author=author,date=date)
        if ato[1]:
                lao=AccessRecord.objects.all()
                d={'lao':lao}
                return render(request,'display_accessrecords.html',d)


        else:
            return HttpResponse('given details Ar is present')
    else:
        return HttpResponse('given parent table data is  not present')
    

def display_topics(request):
    lto=Topic.objects.all()
    d={'lto':lto}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    lwo=Webpage.objects.all()
    lwo=Webpage.objects.order_by('name')
    lwo=Webpage.objects.order_by('-name')
    lwo=Webpage.objects.order_by(Length('name'))
    lwo=Webpage.objects.order_by(Length('name').desc())
    lwo=Webpage.objects.filter(topic_name='skipping')
    lwo=Webpage.objects.filter(topic_name='chess')
    lwo=Webpage.objects.exclude(topic_name='chess')

    lwo=Webpage.objects.filter(name__startswith='s')
    lwo=Webpage.objects.filter(name__endswith='i')
    lwo=Webpage.objects.filter(name__contains='n')
    lwo=Webpage.objects.filter(name__isnull=False)
    lwo=Webpage.objects.filter(id__range=(1,10))
    lwo=Webpage.objects.filter(name__startswith='s')
    lwo=Webpage.objects.filter(id__in=(5,10))
    lwo=Webpage.objects.filter(name__regex=('^s\w+'))
    lwo=Webpage.objects.filter(name__regex=('\w+n\w{1}'))
    lwo=Webpage.objects.filter(name__regex=('\w+u\w{2}'))

    
    d={'lwo':lwo}
    return render(request,'display_webpages.html',d)

def display_accessrecords(request):
    lao=AccessRecord.objects.all()
    lao=AccessRecord.objects.filter(date='2000-02-08')
    lao=AccessRecord.objects.filter(date__year='2000')
    lao=AccessRecord.objects.filter(date__month='2')
    lao=AccessRecord.objects.filter(date__day='20')
    lao=AccessRecord.objects.filter(date__gt='2000-02-08')
    lao=AccessRecord.objects.filter(date__gte='2000-02-08')
    lao=AccessRecord.objects.filter(date__lt='2025-01-02')
    
    lao=AccessRecord.objects.filter(date__lte='2025-01-02')
    lao=AccessRecord.objects.filter(date__year__lte='2025')
    lao=AccessRecord.objects.filter(date__year__lt='2025')
    lao=AccessRecord.objects.filter(date__year__gte='2000')
    lao=AccessRecord.objects.filter(date__year__gt='2000')
    lao=AccessRecord.objects.filter(date__month__gte='02')
    lao=AccessRecord.objects.filter(date__month__gt='2000')
    lao=AccessRecord.objects.filter(date__month__lt='2025')
    lao=AccessRecord.objects.filter(date__month__lte='2025')
    lao=AccessRecord.objects.filter(date__day__gte='08')
    lao=AccessRecord.objects.filter(date__day__gt='08')
    lao=AccessRecord.objects.filter(date__day__lt='29')
    lao=AccessRecord.objects.filter(date__day__lte='29')
    d={'lao':lao}
    return render(request,'display_accessrecords.html',d)

def update_webpage(request):
    lw=Webpage.objects.filter(name='suni').update(topic_name='hand ball')
    lw=Webpage.objects.filter(topic_name='skipping').update(name='reddy')
    lwo=Webpage.objects.all()
    lw=Webpage.objects.filter(name='lahari').update(name='lahari reddy')
    lw=Webpage.objects.filter(topic_name='badminton').update(name='sindhu')
    lw=Webpage.objects.update_or_create(topic_name='carrom',defaults={'name':'anand'})
    lw=Webpage.objects.update_or_create(name='suni',defaults={'uri':'http://swathi.com'})
    #lw=Webpage.objects.update_or_create(name='lahari reddy',defaults={'topic_name':'chess'})whenever dealing with foriegn key column,you should provide object not value

    co=Topic.objects.get(topic_name='chess')
    lw=Webpage.objects.update_or_create(name='lahari reddy',defaults={'topic_name':co})

    cr=Topic.objects.get(topic_name='cricket')#if any condition not satisfies it will create new record
    lw=Webpage.objects.update_or_create(name='chintu',defaults={'uri':'http://chintu.in','topic_name':cr})
    
    lwo=Webpage.objects.all()
    d={'lwo':lwo}
    return render(request,'display_webpages.html',d)

def delete_webpage(request):
    Webpage.objects.filter(name='chintu').delete()
    lwo=Webpage.objects.all()
    d={'lwo':lwo}
    return render(request,'display_webpages.html',d)














