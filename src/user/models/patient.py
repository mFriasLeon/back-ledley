from django.db import models


class Patient(models.Model):
    user = models.ForeignKey(
        "user.User",
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="patients",
        db_comment="FK to User",
        help_text="FK to User",
    )
    medical_record_number = models.CharField(
        max_length=50,
        unique=True,
        db_comment="Unique medical record number for the patient",
        help_text="Unique medical record number for the patient",
    )
    allergies = models.TextField(
        blank=True, db_comment="Allergies of the patient", help_text="Allergies of the patient"
    )

    def __str__(self):
        return f"Patient ID{self.id}: User: {self.user.username}, MRN: {self.medical_record_number}"
