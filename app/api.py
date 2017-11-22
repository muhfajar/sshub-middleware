import requests as rest

from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import permission_classes

from app.models import RFID, SSHub
from sshub_middleware.settings import SSHUB_API


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SSHubViewSet(viewsets.ModelViewSet):
    queryset = SSHub.objects.all()
    serializer_class = SSHubSerializer


class RFIDViewSet(viewsets.ModelViewSet):
    queryset = RFID.objects.all()
    serializer_class = RFIDSerializer


@permission_classes(('AllowAny',))
def sync(request):
    url = 'http://hubdev.softwareseni.co.id/api/v1/users'
    headers = {'token': SSHUB_API}
    sshub_data = rest.get(url, headers=headers)

    # start import data
    for user in sshub_data.json()['result']:
        SSHub.objects.update_or_create(id=int(user['user_id']), name=user['name'])
    return JsonResponse({
        "sync": "success"
    })


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'sshub', SSHubViewSet)
router.register(r'rfid', RFIDViewSet)
