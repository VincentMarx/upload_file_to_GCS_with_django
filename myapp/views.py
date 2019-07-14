from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from myapp.models import Document
from myapp.forms import DocumentForm
from django.contrib.auth.decorators import login_required


@login_required
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        files = request.FILES.getlist('docfile')
        user = request.user.username
        if form.is_valid():
            for f in files:
                filename = f.name
                try:
                    doc = Document.objects.get(filename=filename)
                    doc.filename = filename
                    doc.uploadedby = user
                    doc.lastuploadtime = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
                except Document.DoesNotExist:
                    doc = Document(docfile=f, filename=filename, uploadedby=user, lastuploadtime=timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
                doc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()


    # Render list page with the documents and the form
    return render(request, 'list.html', {'documents': documents, 'form': form})