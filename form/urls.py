from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.registerpage,name="register"),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logoutuser,name="logout"),
    path('user/',views.userpage,name="user"),
    path('contact/',views.contact,name="contact"),
    path('vip/',views.vip,name="vip"),
    path('packages/',views.packages,name="packages"),
    path('freeodds/',views.freeodds,name="freeodds"),
    path('about/',views.about,name="about"),
    path('success/',views.success,name="success"),
    path('accounts_settings/',views.accountSettings,name="accounts_settings"),
    path('payment/',views.payment,name="payment"),
    path('payment1/',views.payment1,name="payment1"),
    path('payment2/',views.payment2,name="payment2"),
    path('payment3/',views.payment3,name="payment3"),
   

    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
    name="reset_password"),

    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
    name="password_reset_done"),

    path('reset/<uidb64>/<token>',
    auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
    name="password_reset_confirm"),

    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
    name="password_reset_complete"),
]


# 1 submit email form                        // passwordResetView.as_view
# 2 Email sent success message             // PasswordDoneView.as_view())
# 3 Link to password Rest form in email       //PasswordConfirmView.as_view()),
# 4 password successfully changed message    //PasswordCompleteView.as_view()),
