from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Contacts.models import ContactUs, ContactUsSerializer
from rest_framework.views import APIView


class ContactsApi(APIView):
    def get(self, request):
        contact = ContactUs.objects.all()

        return JsonResponse(list(contact.values()), safe=False)

    @csrf_exempt
    def post(self, request):
        email_from = request.data.get("email_from")
        subject = request.data.get("subject")
        message = request.data.get("message")

        contact = ContactUs(email_from=email_from, subject=subject, message=message)
        contact.save()
        return JsonResponse(ContactUsSerializer(contact).data, status=201)