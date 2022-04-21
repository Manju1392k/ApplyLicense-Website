from django.shortcuts import redirect, render
from .forms import ApplyLicenseform
from django.contrib import messages

# Create your views here.
def Home(request):
    form = ApplyLicenseform
    if request.method == 'POST':
        form = ApplyLicenseform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Form has been successfully submitted')
            return redirect('home')
    return render(request, 'index.html', {'form':form})