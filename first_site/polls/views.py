from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Om Here. This is The First Site I've Ever Created. Crazy to think anybody could run this code use this url and read this from anywhere at anytime in any life as long as the web exists... Life is incredible at times, most times.")