from django.shortcuts import render
from .models import Estate

def index_view(request):
    return render(
        request=request,
        template_name='main/index.html',

    )
def estate_detail_view(request):
    estates = Estate.objects.all()[:3]  # список из 3 объектов
    return render(
        request,
        template_name='main/estate_detail.html',
        context={'estates': estates}
    )