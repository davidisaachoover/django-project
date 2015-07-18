from django.contrib import admin
from .models import Brewery, site_header_set, User_added_deal, Displayed_prices

# Register your models here.

class DealInline(admin.TabularInline):
    model = Displayed_prices


class BreweryAdmin(admin.ModelAdmin):
	inlines = [DealInline]
	search_fields = ['brewery_name']
	list_filter = ['state']


admin.site.register(Brewery, BreweryAdmin)
admin.site.register(site_header_set)

