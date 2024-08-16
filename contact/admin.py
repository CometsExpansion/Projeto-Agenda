from django.contrib import admin
from contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ...

# admin.site.register(Contact)
# Register your models here.
