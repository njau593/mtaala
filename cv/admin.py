from django.contrib import admin
from .models import About, Contact, Files, Images, Portfolio

# Register your models here.

admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Portfolio)
admin.site.register(Images)
admin.site.register(Files)
