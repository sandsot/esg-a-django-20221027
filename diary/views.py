from django.shortcuts import render, redirect
from diary.models import Memory
from django.views.generic import CreateView
from diary.forms import DiaryForm

def memory_list(request) :
    posts = Memory.objects.all().order_by('-pk')
    return render(
        request,
        'diary/memory_list.html',
        {
            'posts' : posts,
        }
    )

def memory_detail(request, pk):
    post = Memory.objects.get(pk=pk)
    
    return render(
        request,
        'diary/memory_detail.html',
        {
        'post':post,
        }
    )   



def memory_new(request):

    if request.method == "GET":
        form = DiaryForm()
    else :
        form = DiaryForm(request.POST)
        if form.is_valid() :
            post = form.save()
            return redirect(post)
        
    return render(request, "diary/memory_new.html", {
        "form" : form,
    })