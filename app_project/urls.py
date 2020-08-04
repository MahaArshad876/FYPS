from django.urls import path

from app_project import views, viewsAdmin

urlpatterns = [
    path('', views.Home, name="home"),
    path('login/', views.loginUser, name="login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user),
    path('doLogin', views.doLogin, name="doLogin"),
    path('admin_home', viewsAdmin.admin_home, name='admin_home'),
    path('add_supervisor', viewsAdmin.add_supervisor, name="add_supervisor"),
    path('add_supervisor_save', viewsAdmin.add_supervisor_save, name="add_supervisor_save"),
    # path('signup/', views.signup, name="signup"),

]