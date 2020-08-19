from django.db import models
import datetime


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


class User(models.Model):
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


# class MealsMealsByCategory(models.Model):
#     name = models.CharField(max_length=50)
#     category = models.ForeignKey(MealCategory, on_delete=models.CASCADE)
#     price = models.IntegerField()
#     description = models.CharField(help_text="option field", null=True)
#
#     def __str__(self):
#         return self.name
#
#
# class ActiveOrders(models.Model):
#     waiterid = models.ForeignKey()  ## fvfgjgsfdg
#     tableid = models.ForeignKey(Table, on_delete=models.CASCADE())
#     tablename = models.CharField(max_length=50)  ##dfsghdfhgsdfh
#     isitopen = models.BooleanField(default=True)
#     date = models.DateTimeField(auto_now_add=True)
#     mealid = models.ForeignKey(Meal, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.tablename  # походу нужно еще какое нибудь поле
#
#
# class Order(models.Model):
#     waiterid = models.ForeignKey()  ## fvfgjgsfdg
#     tableid = models.ForeignKey(Table, on_delete=models.CASCADE())
#     tablename = models.CharField(max_length=50)  ##dfsghdfhgsdfh
#     isitopen = models.BooleanField(default=False)
#     date = models.DateTimeField(auto_now_add=True)
#     mealid = models.ForeignKey(Meal, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.tablename  # походу нужно еще какое нибудь поле
