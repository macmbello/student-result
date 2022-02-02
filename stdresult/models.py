from calendar import c
from multiprocessing.sharedctypes import Value
from random import choices
from django.db import models

class Result_Sheet(models.Model):
    sn = models.CharField(max_length=2)
    course_code = models.CharField(max_length=7)
    course_title = models.CharField(max_length=30)
    
    CATEGORY_CHOICES = (
        ('core', 'CORE'),
        ('elective', 'ELECTIVE'),
    )
    
    category = models.CharField(max_length=8, choices=CATEGORY_CHOICES)
    grade = models.CharField(max_length=1)
    
    
class Result(models.Model):
    SESSION_CHOICES = (
        ('2018/2019', '2018/2019'),
        ('2019/2020', '2019/2020'),
    )
    session = models.CharField(max_length=9, choices=SESSION_CHOICES)
    
    SEMESTER_CHOICES = (
        ('first', 'FIRST'),
        ('second', 'SECOND'),
    )
    
    semester = models.CharField(max_length=6)
    
    LEVEL_CHOICES = (
        ('100', 'Level 100'),
        ('200', 'Level 200'),
        ('300', 'Level 300'),
        ('400', 'Level 400'),
    )
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES)
    tcr = models.FloatField(max_length=4)
    tce = models.FloatField(max_length=4)
    gpa = models.FloatField(max_length=4)
    cgpa = models.FloatField(max_length=4)
    remark = models.CharField(max_length=200, null=True)
    details = models.CharField(max_length=7)
    
    