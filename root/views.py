from django.http import HttpResponse
from django.views import View


BASE_URL = "127.0.0.1:8000/root/"


# Create your views here.
<<<<<<< HEAD
=======


def administration(request):
    return render(request, "homepage.html")


>>>>>>> c892de625e93deb6a84eeca78f5f235f03dd2741
def hii(request):
    return HttpResponse("this hii virew")


def hello_view(request):
    return HttpResponse("Hello")


class IndexView(View):
    def get(self, request, *args, **kwrags):
        return HttpResponse("This is  index")
    



class HomeView(View):
    def get(request):
        return HttpResponse("<h1>Hello All</h1>")