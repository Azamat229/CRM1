from .models import User, Meal, Table, Role, Department, MealCategory, MealCategoriesByDepartment, Status, \
    ServicePercentage, Order, CountOfMeal, Check
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


"""Create Order"""


class CountOfMealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountOfMeal
        fields = ['id', 'count_meal', 'name_meal']


class OrderCreateSerializer(serializers.ModelSerializer):
    count = CountOfMealsSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'waiterid', 'tableid', 'count', ]

    def create(self, validated_data):
        count = validated_data.pop('count')
        order = Order.objects.create(**validated_data)
        for coun in count:
            CountOfMeal.objects.create(**coun, order=order)
        return order


"""List Order"""


class OrderListSerializer(serializers.ModelSerializer):
    count = CountOfMealsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'waiterid', 'tableid', 'tablename', 'isitopen', 'date', 'count']


"""Delete Order"""


class OrderDetailSerializer(serializers.ModelSerializer):
    count = CountOfMealsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


"""Check create"""


#
# class AmountListSerializer(serializers.ModelSerializer):
#     price = serializers.IntegerField( source='name.price')
#
#     class Meta:
#         model = Amount
#         fields = ['id', 'name', 'amount', 'price', ]


class CheckCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = ['orderid']
        # fields = '__all__'
    #
    # def create(self, validated_data):
    #     meals = validated_data.pop('meals')
    #     list_of_check = Check.objects.create(**validated_data)
    #     for meal in meals:
    #         Amount.objects.create(**meal, list_of_check=list_of_check)
    #     return list_of_check


"""List Check"""


class CheckListSerializer(serializers.ModelSerializer):
    counts = CountOfMealsSerializer(many=True, read_only=True)


    class Meta:
        model = Check
        # fields = '__all__'
        fields = ['id', 'orderid', 'date', 'servicefee', 'counts']
