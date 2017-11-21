from django.db import models


class SSHub(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SSHub'


class RFID(models.Model):
    token_id = models.CharField(max_length=16)
    sshub = models.OneToOneField(SSHub)

    def __str__(self):
        return self.sshub.name

    class Meta:
        verbose_name = 'RFID'
