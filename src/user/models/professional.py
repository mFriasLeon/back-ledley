from django.db import models


class Professional(models.Model):
    user = models.ForeignKey(
        "user.User",
        primary_key=True,
        on_delete=models.CASCADE,
        related_name="professionals",
        db_comment="FK to User",
        help_text="FK to User",
    )
    role = models.CharField(max_length=50, db_comment="Role of the professional", help_text="Role of the professional")

    def __str__(self):
        return f"Professional ID{self.id}: User: {self.user.username}, Role: {self.role}"
