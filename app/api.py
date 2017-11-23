import json

import requests as rest

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import permission_classes

from app.models import RFID, SSHub, Log
from sshub_middleware.settings import SSHUB_API, SSHUB_FETCH_URL, SSHUB_LOGIN_URL


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


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
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

    def create(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))

        # set to log if rfid not found in system
        if not RFID.objects.filter(token_id__exact=data['tokenID']).exists():
            Log.objects.create(rfid=data['tokenID'])
            return JsonResponse({
                "error": "true",
                "errorMessage": "Card has not been paired with user"
            })

        # login proses
        rfid_data = SSHub.objects.filter(rfid__token_id__exact=data['tokenID']).first()

        # trigger start work
        url = SSHUB_LOGIN_URL(rfid_data.id)
        headers = {'token': SSHUB_API}
        sshub_data = rest.get(url, headers=headers)

        return JsonResponse({
            "error": "false",
            "tokenID": data['tokenID'],
            "uid": rfid_data.id,
            "name": rfid_data.name,
            "status": 'LOGGED_IN',
            # "payload": sshub_data.json()
        })


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = RFIDSerializer


@permission_classes(('AllowAny',))
def sync(request):
    url = SSHUB_FETCH_URL
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
router.register(r'log', LogViewSet)
