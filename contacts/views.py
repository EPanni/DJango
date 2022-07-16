from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Contact
from django.core.paginator import Paginator
def index(request):
    contacts=Contact.objects.order_by('name').filter(display=True)
    paginator = Paginator(contacts,15) # This content was only choosen due to validation purposes

    page = request.GET.get('p')
    contacts = paginator.get_page(page)
    return render(request,
    'contacts/index.html',{
    'contacts':contacts})

def display_contact(request,contact_id):
    contact=get_object_or_404(Contact,id=contact_id)
    
    if not contact.display:
        raise Http404()
        
    return render (request,'contacts/display_contact.html',
    {'contact':contact})

