from .models import User, Meal, Table, Role, Department, MealCategory, MealCategoriesByDepartment, Status, \
    ServicePercentage
from rest_framework import serializers

""" USER """


class UserListSerializer(serializers.ModelSerializer):
    roleid = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


"""MEAL"""


class MealListSerializer(serializers.ModelSerializer):
    categoryid = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Meal
        fields = '__all__'


class MealDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


"""Table"""


class TableListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class TableDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


"""Role"""


class RoleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class RoleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


"""Department"""


class DepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


"""MealCategory"""


class MealCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = '__all__'


class MealCategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategory
        fields = '__all__'


"""MealCategory"""


class MealCategoriesByDepartmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealCategoriesByDepartment
        fields = '__all__'


"""MealCategory"""


class StatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class StatusDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


"""MealCategory"""


class ServicePercentageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = '__all__'


class ServicePercentageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = '__all__'
