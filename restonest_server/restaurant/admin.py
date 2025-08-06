from django.contrib import admin
from .models import MenuItem, Reservation

# Register your models here.
admin.site.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_editable = ('name', 'price')
    
admin.site.register(Reservation)    
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'number_of_people', 'menu_item', 'date')
    list_filter = ('user', 'menu_item', 'date')
    search_fields = ('user', 'menu_item')