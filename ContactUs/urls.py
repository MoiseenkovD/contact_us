from django.contrib import admin
from django.urls import path
from Contacts.api import contacts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/us', contacts.ContactsApi.as_view())
]
