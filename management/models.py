from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('office_staff', 'Office Staff'),
        ('librarian', 'Librarian'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='admin')

    def __str__(self):
        return f"{self.username} ({self.role})"


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(25)])
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} (Grade {self.grade})"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['name']


class LibraryHistory(models.Model):
    STATUS_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='library_records')
    book_name = models.CharField(max_length=100)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.book_name} ({self.status})"

    class Meta:
        verbose_name = "Library History"
        verbose_name_plural = "Library Histories"
        ordering = ['-borrow_date']


class FeesHistory(models.Model):
    FEE_TYPE_CHOICES = [
        ('tuition', 'Tuition'),
        ('library', 'Library'),
        ('transport', 'Transport'),
        ('exam', 'Exam'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees_records')
    fee_type = models.CharField(max_length=100, choices=FEE_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.fee_type} - ${self.amount}"

    class Meta:
        verbose_name = "Fees History"
        verbose_name_plural = "Fees Histories"
        ordering = ['-payment_date']
