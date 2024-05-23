from django.contrib import admin

from .models import IndirectHours, TimeCode


@admin.register(IndirectHours)
class IndirectHoursAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date', 'status', 'is_archive')
    readonly_fields = ('is_archive',)

    # def get_mechanics(self, obj):
    #     return "\n".join([str(p) for p in obj.mechanic.all()])
@admin.register(TimeCode)
class TimeCodeAdmin(admin.ModelAdmin):
    pass
