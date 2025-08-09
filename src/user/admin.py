from django.contrib import admin

# Register your models here.

from user.models.user import User
from user.models.professional import Professional
from user.models.patient import Patient


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "name", "email", "gender", "birth_date", "active", "created_date")
    list_filter = ("gender", "active")
    search_fields = ("username", "name", "email")
    ordering = ("id",)


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    search_fields = ("user__username", "role")
    list_filter = ("role",)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("user", "medical_record_number", "allergies")
    list_filter = ("allergies",)
    search_fields = ("user__username", "medical_record_number")
