from rest_flex_fields import FlexFieldsModelSerializer
from .models import Job, Image
from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )

    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']

#create serializer for Job
class Jobserializer(serializers.ModelSerializer):
   
    class Meta:
        model = Job
        fields = '__all__'
    def create(self,validated_data):
      
        print(validated_data)
        job = Job.objects.create(image=validated_data['image'],title=validated_data['title'],description=validated_data['description'],
                                    location=validated_data['location'],company=validated_data['company'],
                                    link=validated_data['link'],date=validated_data['date'],salary=validated_data['salary'])
        job.users_applied.set(validated_data['users_applied'])                                                   
        # print(job)                            
                                   
        return job
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.location = validated_data.get('location', instance.location)
        instance.company = validated_data.get('company', instance.company)
        instance.link = validated_data.get('link', instance.link)
        instance.date = validated_data.get('date', instance.date)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.users_applied = validated_data.get('users_applied', instance.users_applied)

        instance.save()
        return instance


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
