from django.db import models

class Plan(models.Model):
    id = models.AutoField(primary_key=True, db_comment="PK of a Plan", help_text="PK of a Plan")
    name = models.CharField(max_length=255, unique=True, db_comment="Name of the plan", help_text="Name of the plan")
    description = models.TextField(blank=True, db_comment="Description of the plan", help_text="Description of the plan")
    created_date = models.DateTimeField(auto_now_add=True, db_comment="Creation date of the plan", help_text="Creation date of the plan")
    patient = models.ForeignKey(
        "user.Patient",
        on_delete=models.CASCADE,
        related_name="plans",
        db_comment="FK to Patient",
        help_text="FK to Patient",
    )
    professional = models.ForeignKey(
        "user.Professional",
        on_delete=models.CASCADE,
        related_name="plans",
        db_comment="FK to Professional",
        help_text="FK to Professional",
    )

    def __str__(self):
        return (f"Plan ID{self.id}: Name: {self.name}, Created on: {self.created_date}"
                f", Patient: {self.patient.user.username}, Professional: {self.professional.user.username}")