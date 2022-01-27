from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import Jobserializer, MyTokenObtainPairSerializer
from rest_framework.viewsets import ModelViewSet

from .models import Job, Image
from rest_framework.permissions import IsAuthenticated
from .serializers import ImageSerializer
from rest_flex_fields.views import FlexFieldsModelViewSet
#want to add view to apply jobs
class ApplyJobView(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = Jobserializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    def perform_create(self, serializer):
        job = Job.objects.get(pk=self.kwargs['pk'])
        user = self.request.user
        job.users_applied.add(user)
        job.save()
        return super().perform_create(serializer)

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
