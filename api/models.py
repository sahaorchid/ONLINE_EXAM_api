from django.db import models


class qusform(models.Model):
    qno=models.IntegerField()
    qus=models.TextField()
    op1=models.CharField(max_length=1000)
    op2 = models.CharField(max_length=1000)
    op3 = models.CharField(max_length=1000)
    op4 = models.CharField(max_length=1000)

class allans(models.Model):
    qusno=models.IntegerField()
    qus=models.CharField(max_length=1000)
    ans=models.CharField(max_length=1000)
