from django.contrib import admin
from .models import member, child


class childInline(admin.StackedInline):
    model = child
    extra = 3



class memberAdmin(admin.ModelAdmin):
    list_display = [ 'last_name', 'first_name', 'spouse', 'address', 'city', 'state', 'zip']
    #fieldsets = [('Child', {'fields': ['name']})]
    inlines = [childInline]

admin.site.register(member, memberAdmin)
