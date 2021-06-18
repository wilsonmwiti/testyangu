from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("created_date", "category","title","author")
    list_filter = ("created_date","category","author",)
    ordering = ("-id",)
    search_fields = ("title","author" )

admin.site.register(Post,PostAdmin)
