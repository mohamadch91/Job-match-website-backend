from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import Jobserializer, MyTokenObtainPairSerializer
from rest_framework.viewsets import ModelViewSet

from .models import Job, Image
from rest_framework.permissions import IsAuthenticated
from .serializers import ImageSerializer
from rest_flex_fields.views import FlexFieldsModelViewSet


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = Jobserializer
   
class ImageViewSet(FlexFieldsModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated]


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
