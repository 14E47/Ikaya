from django.shortcuts import render, get_object_or_404
from journal.models import Journal

def journal_list(request, template = 'journal/journal.html'):
    journals = Journal.objects.all()
    return render(request, template, {'journals': journals,})

def journal_detail(request, slug, template='journal/journal_detail.html'):
    journal = Journal.objects.all()
    journal = get_object_or_404(journal, slug=slug)
    return render(request, template, {'journal': journal,})
