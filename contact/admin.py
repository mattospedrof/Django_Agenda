from django.contrib import admin
from contact.models import Contact
from contact.models import Category
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone',
    ordering = 'id',
    #ordering = '-id', descrescente
    #listed_filter = 'created_date',
    search_fields = 'id', 'fisrt_name', 'last_name', 'phone',
    list_per_page = 20
    list_max_show_all = 100
    list_editable = 'first_name', 'last_name', 'phone',
    list_display_links = 'id',
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
    