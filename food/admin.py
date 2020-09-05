from django.contrib import admin
from .models import Table, Role, Department, User, GetUserToken, MealCategory, MealCategoriesByDepartment, Status, \
    ServicePercentage, Meal, Userr, Order, CountOfMeal

# Register your models here.
admin.site.register(Table)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Userr)
admin.site.register(GetUserToken)
admin.site.register(MealCategory)
admin.site.register(MealCategoriesByDepartment)
admin.site.register(Status)
admin.site.register(ServicePercentage)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(CountOfMeal)
admin.site.unregister(User)

