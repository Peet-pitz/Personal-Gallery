from django.contrib import admin
from .models import Image,Photographer,Location,Category

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Image)
admin.site.register(Photographer)
admin.site.register(Location)
admin.site.register(Category)