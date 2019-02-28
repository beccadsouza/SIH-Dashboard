from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
	return render(request, 'dashboard.html')

def signout(request):
	return render(request, 'registration/logout.html')
