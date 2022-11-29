from django.contrib import admin

# Register your models here.
from .models import About, Profile, blog_post, Category, Image, Contact

#admin.site.register(About)
#admin.site.register(Profile)

class ProfileInline(admin.TabularInline):
    model= Profile
    extra=1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines=[
        ProfileInline,
    ]



#blogspot
@admin.register(blog_post)
class blog_postAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'post_time')
    prepopulated_fields= {'slug': ['title'],}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_name', 'category_slug')
    prepopulated_fields= {'category_slug': ['category_name'],}

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_Display=('image_name','image_category','image_slug','image_size')
    prepopulated_fields= {'image_slug': ['image_name'],}

admin.site.register(Contact)
