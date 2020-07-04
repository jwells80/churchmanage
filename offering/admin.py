from django.contrib import admin
from .models import offering, paymenttype, fund


admin.site.register(paymenttype)
admin.site.register(fund)

class offeringAdmin(admin.ModelAdmin):
    list_display = [ 'member_id', 'amount', 'date', 'mode_id', 'fund_id']

admin.site.register(offering, offeringAdmin)