from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    title = "Trang chủ"
    context = {
        'title': title
    }
    return render(request, './index.html', context)