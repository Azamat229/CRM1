from django.db import models
import datetime
from django.contrib.auth.models import User


class Table(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Userr(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    roleid = models.ForeignKey(Role, on_delete=models.CASCADE)
    dateofadd = models.DateField(("Date"), default=datetime.date.today)
    phone = models.IntegerField(help_text="996559444345")

    def __str__(self):
        return self.name


class GetUserToken(models.Model):
    roleid = models.ForeignKey(Role, on_delete=models.CASCADE)
    token = models.CharField(max_length=50)


class MealCategory(models.Model):
    name = models.CharField(max_length=50)
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MealCategoriesByDepartment(models.Model):
    name = models.CharField(max_length=50)
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ServicePercentage(models.Model):
    percentage = models.IntegerField(default=33)

    def __str__(self):
        return str(self.percentage)


class Meal(models.Model):
    name = models.CharField(max_length=50)
    categoryid = models.ForeignKey(MealCategory, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(help_text="option field", null=True, max_length=500)

    def __str__(self):
        return self.name


class Order(models.Model):
    waiterid = models.ForeignKey(Userr, on_delete=models.CASCADE)
    tableid = models.ForeignKey(Table, on_delete=models.CASCADE)
    tablename = models.CharField(max_length=50)
    isitopen = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}, {}'.format(self.waiterid, self.tableid)


class CountOfMeal(models.Model):
    order = models.ForeignKey(Order, related_name='count', on_delete=models.CASCADE)
    name_meal = models.ForeignKey(Meal, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.PositiveIntegerField()

    @property
    def total(self):
        return self.amount * self.name_meal.price

    def __str__(self):
        return self.total


"""Create Check"""


class Check(models.Model):
    orderid = models.ForeignKey(Order, related_name='counts', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    servicefree = models.IntegerField(default=20)
    totalsum = models.IntegerField(blank=True, null=True)  # thinking about this
    mealsid = models.ForeignKey(CountOfMeal, on_delete=models.CASCADE)

    def __str__(self):
        return self.orderid
