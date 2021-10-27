from django.db import models
from rest_framework import serializers


class ContactUs(models.Model):
    class Meta:
        db_table = "contacts_us"

    email_from = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"