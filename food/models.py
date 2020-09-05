from django.db import models
import datetime
from django.contrib.auth.models import User


class Table(models.Model):  # add, get all, delete
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# [
#   {
#     "id": 3,
#     "name": "Table #1"
#   },
#   {
#     "id": 5,
#     "name": "Table #3"
#   },
#   {
#     "id": 6,
#     "name": "Table #4"
#   },
#   {
#     "id": 7,
#     "name": "Table #5"
#   }
# ]

class Role(models.Model):  # add, get all, delete
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# [
#   {
#     "id": 3,
#     "name": "Waiter"
#   },
#   {
#     "id": 5,
#     "name": "Admin"
#   },
#   {
#     "id": 6,
#     "name": "Chef"
#   }
# ]


class Department(models.Model):  # add, get all, delete
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# [
#   {
#     "id": 3,
#     "name": "kitchen"
#   },
#   {
#     "id": 5,
#     "name": "bar"
#   }
# ]


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


# [
#   {
#     "id": 3,
#     "name": "Aika",
#     "surname": "Ivanova",
#     "login": "ivanova_aika",
#     "password": "",
#     "email": "sample@example.com",
#     "roleid": 2,
#     "dateofadd": "15.07.2017",
#     "phone": "0777777777"
#   },
#   {
#     "id": 7,
#     "name": "Bakyt",
#     "surname": "Sadyrbaev",
#     "login": "sadyrbaev_bakyt",
#     "password": "",
#     "email": "sample@example.com",
#     "roleid": 3,
#     "dateofadd": "25.08.2017",
#     "phone": "0777777777"
#   }
# ]


class GetUserToken(models.Model):
    roleid = models.ForeignKey(Role, on_delete=models.CASCADE)
    token = models.CharField(max_length=50)


# {
#   "roleid": 3,
#   "token": "sadfghjkhgfdgh"
# }

class MealCategory(models.Model):
    name = models.CharField(max_length=50)
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# [
#   {
#     "id": 3,
#     "name": "Pervoe",
#     "departmentid": 1
#   },
#   {
#     "id": 5,
#     "name": "Vtoroe",
#     "departmentid": 2
#   },
#   {
#     "id": 6,
#     "name": "Desrts",
#     "departmentid": 3
#   }
# ]


class MealCategoriesByDepartment(models.Model):
    name = models.CharField(max_length=50)
    departmentid = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# [
#   {
#     "id": 3,
#     "name": "Pervoe",
#     "departmentid": 1
#   },
#   {
#     "id": 5,
#     "name": "Vtoroe",
#     "departmentid": 1
#   },
#   {
#     "id": 6,
#     "name": "Desrts",
#     "departmentid": 1
#   }
# ]

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# [
#   {
#     "id": 1,
#     "name": "to do"
#   },
#   {
#     "id": 3,
#     "name": "in progress"
#   },
#   {
#     "id": 21,
#     "name": "done"
#   }
# ]

class ServicePercentage(models.Model):
    percentage = models.IntegerField()

    def __str__(self):
        return str(self.percentage)


# {
#   "percentage": 34
# }

class Meal(models.Model):
    name = models.CharField(max_length=50)
    categoryid = models.ForeignKey(MealCategory, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(help_text="option field", null=True, max_length=500)

    def __str__(self):
        return self.name


# [
#     {
#         "id": 4,
#         "name": "plov",
#         "categoryid": 3,
#         "price": 250,
#         "description": "dfghjkdfghjn" //optional
#     },
#     {
#         "id": 5,
#         "name": "lagman",
#         "categoryid": 2,
#         "price": 220,
#         "description": "dfghjkdfghjn" //optional
#     },
#     {
#         "id": 7,
#         "name": "manty",
#         "categoryid": 1,
#         "price": 180,
#         "description": "dfghjkdfghjn" //optional
#     }
# ]

#
# class MealMealsByCategory(models.Model):
#     name = models.CharField(max_length=50)
#     categoryid = models.ForeignKey(MealCategory, on_delete=models.CASCADE)
#     price = models.IntegerField()
#     description = models.CharField(help_text="option field", null=True)
#
#     def __str__(self):
#         return self.name


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
    count_meal = models.PositiveIntegerField()

    @property
    def total(self):
        return self.count_meal * self.name_meal.price

"""Create Check"""


class Check(models.Model):
    order = models.ForeignKey(Order, related_name='counts', on_delete=models.CASCADE)

    orderid = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    servicefee = models.ForeignKey(ServicePercentage, on_delete=models.CASCADE)
    totalsum = models.IntegerField()  # thinking about this

    def __str__(self):
        return self.orderid







#
# class Amount(models.Model):
#     list_of_check = models.ForeignKey(Check, related_name='meals', on_delete=models.CASCADE)
#     name = models.ForeignKey(Meal, on_delete=models.CASCADE, blank=True, null=True)
#     amount = models.PositiveIntegerField()
#
#     @property
#     def total(self):
#         return self.amount * self.name.price

# class MealsToOrder(models.Model):  # uniqueid ?
#     orderid = models.ForeignKey(Order, on_delete=models.CASCADE)
#     meals = models.ForeignKey(Meal, on_delete=models.CASCADE)
