from django.contrib import admin
from webapp.models import *

"""
class CatagoryAdmin(admin.ModelAdmin):
    list_display=('name','image','description')
admin.site.register(Catagory,CatagoryAdmin)
admin.site.register(Product) """


admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)