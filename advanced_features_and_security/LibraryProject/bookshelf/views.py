from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
# Create your views here.
<ExampleForm () = 'post'>{% csrf_token %} 
def form_example(request):
    return HttpResponse(request ,'form_example.html')


def book_views(request):
    return HttpResponse(request,'book_list.html')

    
@permission_required('bookshelf.can_create',raise_exception = True)
@permission_required('bookshelf.can_edit',raise_exception = True)
@permission_required('bookshelf.can_delete')
@permission_required('bookshelf.can_view',raise_exception = True)
def permission_granter(request,book_list):
    pass