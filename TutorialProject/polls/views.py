from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from polls.models import Poll, Choice

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = Context({
        'latest_poll_list' : latest_poll_list
        })
    return render(request, "polls/index.html", context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, "polls/detail.html", {'poll' : poll})

def result(request, poll_id):
    return HttpResponse("Result page %s" % poll_id)

def vote(request, poll_id):
    return HttpResponse("Vote page %s" % poll_id)
