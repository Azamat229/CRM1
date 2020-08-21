from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),

    path('meals/', views.MealListView.as_view()),
    path('meals/<int:pk>/', views.MealDetailView.as_view()),

    path('table/', views.TableList.as_view()),
    path('table/<int:pk>/', views.TableDetail.as_view()),

    path('role/', views.RoleList.as_view()),
    path('role/<int:pk>/', views.RoleDetail.as_view()),

    path('Departments/', views.DepartmentList.as_view()),
    path('depart_ment/<int:pk>/', views.DepartmentDetail.as_view()),

    path('MealCategory/', views.MealCategoryList.as_view()),
    path('MealCategory/<int:pk>/', views.MealCategoryDetail.as_view()),

    path('MealCategoriesByDepartment/', views.MealCategoriesByDepartmentList.as_view()),

    path('Status/', views.StatusList.as_view()),
    path('Status/<int:pk>/', views.StatusDetail.as_view()),

    path('ServicePercentage/', views.ServicePercentageList.as_view()),
    path('StServicePercentageatus/<int:pk>/', views.ServicePercentageDetail.as_view()),

    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    # path('hello/', views.HelloView.as_view(), name='hello'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
