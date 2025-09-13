from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.

@permission_required('bookshelf.can_create',raise_exception = True)
@permission_required('bookshelf.can_edit',raise_exception = True)
@permission_required('bookshelf.can_delete')
@permission_required('bookshelf.can_view',raise_exception = True)
def permission_granter(request)