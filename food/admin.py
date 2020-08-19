from django.contrib import admin
from .models import Table, Role, Department, User, GetUserToken, MealCategory, MealCategoriesByDepartment, Status, \
    ServicePercentage, Meal

# Register your models here.
admin.site.register(Table)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(User)
admin.site.register(GetUserToken)
admin.site.register(MealCategory)
admin.site.register(MealCategoriesByDepartment)
admin.site.register(Status)
admin.site.register(ServicePercentage)
admin.site.register(Meal)
