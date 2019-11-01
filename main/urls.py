from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

from .views import index, other_page, profile, user_activate, by_rubric, detail
from .views import BbLoginView, BbLogoutView, ChangeUserInfoView, BBPasswordChangeView
from .views import RegisterUserView, RegisterDoneView, DeleteUserView
from .views import profile_bb_detail, profile_bb_add, profile_bb_delete, profile_bb_change

app_name = 'main'
urlpatterns = [
	path('', index, name='index'),
	path('detail/<int:pk>/', detail, name='detail'),
	path('<int:pk>/', by_rubric, name='by_rubric'),
	path('<str:page>/', other_page, name='other'),
	path('accounts/login/', BbLoginView.as_view(), name='login'),
	path('accounts/profile/delete/<int:pk>/', profile_bb_delete, name='profile_bb_delete'),
	path('accounts/profile/add/', profile_bb_add, name='profile_bb_add'),
	path('accounts/profile/', profile, name='profile'),
	path('accounts/profile/<int:pk>/', profile_bb_detail, name='profile_bb_detail'),
	path('accounts/profile/change/<int:pk>/', profile_bb_change, name='profile_bb_change'),
	path('accounts/logout/', BbLogoutView.as_view(), name='logout'),
	path('accounts/profile/change/', ChangeUserInfoView.as_view(),
		 name='profile_change'),
	path('accounts/password/change/', BBPasswordChangeView.as_view(),
		 name='password_change'),
	path('accounts/register/done/', RegisterDoneView.as_view(),
									name='register_done'),
	path('accounts/register/', RegisterUserView.as_view(),
							   name='register'),
	path('accounts/register/activate/<str:sign>/', user_activate,
		 name='register_active'),
	path('accounts/profile/delete/', DeleteUserView.as_view(),
									 name='profile_delete'),
	path('accounts/password_reset/', PasswordResetView.as_view(
		template_name='registration/reset_password.html',
		subject_template_name='registration/reset_subject.txt',
		email_template_name='registration/reset_email.html',
		success_url=reverse_lazy('main:password_reset_done')),
		name='password_reset'),
	path('accounts/password_reset/done/',
		PasswordResetDoneView.as_view(
		template_name='registration/email_sent.html'),
		name='password_reset_done'),
	path('accounts/reset/<uidb64>/<token>/',
		PasswordResetConfirmView.as_view(
		template_name='registration/confirm_password.html',
		success_url=reverse_lazy('main:password_reset_complete')),
		name='password_reset_confirm'),
	path('accounts/reset/done/',
		PasswordResetCompleteView.as_view(
		template_name='registration/password_confirmed.html'),
		name='password_reset_complete'),
	
]