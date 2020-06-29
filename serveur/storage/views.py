from django.http import HttpResponse
from .serializers import PhotoSerializer
from .models import Photo
from rest_framework import viewsets


from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)


class PhotoViewSet(viewsets.ModelViewSet):
    queryset=Photo.objects.all()
    serializer_class = PhotoSerializer

    def post(self, request):
        name=request.data['name']
        photo=request.data['photo']
        Photo.objects.create(name=name, photo=photo)
        return HttpResponse({'message': 'image enregistrée'})


