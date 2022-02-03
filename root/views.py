from django.http import HttpResponse

# Create your views here.
def hii(request):
    return HttpResponse('this hii virew')


def hello_view(request):
    return HttpResponse("Hello")
