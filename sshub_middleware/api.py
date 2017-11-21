from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from app.models import SSHub, RFID


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class SSHubSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSHub
        fields = '__all__'


class RFIDSerializer(serializers.ModelSerializer):
        class Meta:
            model = RFID
            fields = '__all__'


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SSHubViewSet(viewsets.ModelViewSet):
    queryset = SSHub.objects.all()
    serializer_class = SSHubSerializer


class RFIDViewSet(viewsets.ModelViewSet):
    queryset = RFID.objects.all()
    serializer_class = RFIDSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sshub', SSHubViewSet)
router.register(r'rfid', RFIDViewSet)
