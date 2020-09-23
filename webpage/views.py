from django.shortcuts import render
from django.contrib import messages
from .forms import FeedbackForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    """View function for home page of site."""
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return render(request, 'index.html', {'form': f, 'sent': True})
    else:
        f = FeedbackForm()
    
    return render(request, 'index.html', {'form': f})
