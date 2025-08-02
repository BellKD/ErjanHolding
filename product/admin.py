from django.contrib import admin
from .models import Estate, Category, Image, City, District

class EstateAdmin(admin.ModelAdmin):
    list_display = ('title','category','city','created_at','is_active')
    list_filter = ('category','city','district')
    search_fields = ('title','description')



admin.site.register(Estate,EstateAdmin)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(City)
admin.site.register(District)
