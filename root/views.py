from django.http import HttpResponse
from django.views import View


BASE_URL = "https://github.com/quickhaze/shark/pulls"


# Create your views here.
def hii(request):
    return HttpResponse('this hii virew')


def hello_view(request):
    return HttpResponse("Hello")


class IndexView(View):
    def get(self, request, *args, **kwrags):
        return HttpResponse("This is  index")
