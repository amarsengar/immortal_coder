from django.contrib import admin
from .models import PostView,Author,Comment,Category,Post

# Register your models here.


admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Category)