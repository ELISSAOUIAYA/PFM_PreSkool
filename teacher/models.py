from django.db import models
from django.conf import settings

class Teacher(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='teacher_profile'
    )
    employee_id = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)
    
    department = models.ForeignKey(
        'departments.Department', 
        on_delete=models.CASCADE, 
        related_name='teachers'
    )

    def __str__(self):
        # La ligne s'arrête bien ICI :
        return f"{self.user.first_name} {self.user.last_name}"