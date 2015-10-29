from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

from django.http import HttpResponse


@login_required
def main(request):
    return render_to_response('angular/index.html')

def new_user(request):
    return HttpResponse('<h1>hi</h1>')