from django.shortcuts import redirect,render, HttpResponse, get_object_or_404
from .models import Link
from django.urls import reverse

from .forms import LinkForm

# Create your views here.
def index(request):
    links = Link.objects.all()

    context = {
        'links': links
    }
    return render(request, "links/index.html", context)

def new(request):

    if request.method == "POST":
        #post means we are receving new data to be stored!
        # ie., form has data
        form = LinkForm(request.POST)

        if form.is_valid():
            # save the data
            form.save()

            # redirecting to home page
            return redirect(reverse('home'))

    else:
        # get requeest
        form = LinkForm()

    context = {
        "form" : form 
    }
    

    return render(request, "links/create.html", context)

def root_link(request, link_slug):
    # localhost/google should redirect to google.com
    link = get_object_or_404(Link, slug=link_slug)
    link.click() # click() is defined in models.py
                    # helps us increment click varible
    return redirect(link.url)

