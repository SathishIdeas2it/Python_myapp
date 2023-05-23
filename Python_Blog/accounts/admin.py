from django.contrib import admin

# Register your models here.
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
   list_display =('title','description','created_on','image',)
       
    
admin.site.register(Post,PostAdmin)