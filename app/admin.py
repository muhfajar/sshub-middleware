from django.contrib import admin

from app.models import SSHub, RFID, Log

admin.site.register(SSHub)
admin.site.register(RFID)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('rfid',)}),
    )
    list_display = ('rfid', 'last_access')
    search_fields = ('rfid',)
    ordering = ('rfid', 'last_access')
