from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ("Usuario", "Orden",)

admin.site.register(Member, MemberAdmin)

# Register your models here.
