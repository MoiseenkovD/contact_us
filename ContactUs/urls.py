from Contacts.api import contacts

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/us', contacts.ContactsApi.as_view())
]
