from django.contrib import admin

# Register your models here.
from .models import product

class PostModelAdmin(admin.ModelAdmin):
	
	class Meta:
		model = product


admin.site.register(product, PostModelAdmin)