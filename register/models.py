from django.db import models


class Create(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="create/images/")
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    education = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "Create"

    def __str__(self):
        return str(self.id)
