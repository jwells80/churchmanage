from django.shortcuts import render, get_object_or_404
from .forms import memberForm
from .models import member


def memberlist(request):
    allmembers = member.objects.all()
    return render(request, 'members/memberlist.html', {'title': 'Members', 'allmembers': allmembers})

def detail(request, member_id):
    memberdetail = get_object_or_404(member, pk=member_id)
    form = memberForm(instance=memberdetail)
    return render(request, 'members/detail.html', {'title': 'Edit Member', 'member': memberdetail, 'form': form})

def addmember(request):
    form = memberForm()
    return render(request, 'members/add.html', {'title': 'Add New Member', 'form': form})
