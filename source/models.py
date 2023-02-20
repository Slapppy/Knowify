from django.db import models
from django.contrib.auth.models import User



class CourseCatalog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.ImageField(upload_to='images/')


class CourseCategory(models.Model):
    name = models.CharField(max_length=100)


class UserProfile(models.Model):
    name = models.CharField(max_length=128, null=True)
    surname = models.CharField(max_length=128, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)


class CourseEnrollment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseCatalog, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)


class PaymentHistory(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(CourseCatalog, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)


class CourseSection(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(CourseCatalog, on_delete=models.CASCADE)


class CourseContent(models.Model):
    title = models.CharField(max_length=100)
    content_type = models.CharField(max_length=50)
    content = models.TextField()
    section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)


class Review(models.Model):
    course = models.ForeignKey(CourseCatalog, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
