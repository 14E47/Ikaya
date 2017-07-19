from django.shortcuts import render, get_object_or_404
from journal.models import Journal

def journal_list(request, template = 'journal/journal.html'):
    n = 5
    journals = Journal.objects.all()
    journals_f = [journals[i:i + n] for i in range(0, len(journals), n)]
    return render(request, template, {'journals': journals_f,})

def journal_detail(request, slug, template='journal/journal_detail.html'):
    journal = Journal.objects.all()
    journal = get_object_or_404(journal, slug=slug)
    return render(request, template, {'journal': journal,})
