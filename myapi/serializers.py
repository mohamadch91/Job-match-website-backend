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
    Image=ImageSerializer()
    class Meta:
        model = Job
        fields = '__all__'
    def create(validated_data):
        image1=validated_data['image']
        image2=Image.objects.create(name=image1['name'],image=image1['image'],image_ppoi=image1['image_ppoi'])
        job = Job.objects.create(image=image2,title=validated_data['title'],description=validated_data['description'],
                                    location=validated_data['location'],company=validated_data['company'],
                                    link=validated_data['link'],date=validated_data['date'],ppoi=validated_data['ppoi'])
        return job
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.location = validated_data.get('location', instance.location)
        instance.company = validated_data.get('company', instance.company)
        instance.link = validated_data.get('link', instance.link)
        instance.date = validated_data.get('date', instance.date)
        instance.ppoi = validated_data.get('ppoi', instance.ppoi)
        instance.save()
        return instance


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
