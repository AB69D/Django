from django.db import models

class student(models.Model):
    
        student_id = models.IntegerField() # for primary key models.IntegerField( primary_key = Trure )
        student_name =  models.CharField(max_length=30)
        student_email = models.EmailField(max_length=70)
        student_pass = models.CharField(max_length=30)
        comment = models.CharField(max_length=40, default="Not Avilable")
        
    
        # def __str__(self):
        #  return(self.student_id)
