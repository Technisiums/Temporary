from django.http import JsonResponse
from .models import Book
from .serializers import BookSerializer
# Create your views here.

def all_books(request):
    obj = Book.objects.all()
    serializer = BookSerializer(obj, many=True)
    return JsonResponse(serializer.data, safe=False)