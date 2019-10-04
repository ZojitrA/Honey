from django.contrib import admin
from listings.models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links =('id', 'address')
    list_filter = ('realtor',)
    search_fields = ('address', 'description', 'city', 'state', 'zipcode')
    list_per_page = 40
    # list_editable =('is_published')

admin.site.register(Listing, ListingAdmin)
