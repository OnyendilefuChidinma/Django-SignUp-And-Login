from django.urls import path
from .home import HomepageView, view_profile, delete_student, Add_Students
# from . import home
from . import views
# from . import auth_user
# from blogfolder.student.auth import Signup
from .auths import Signup, Login, Logout
# from .auths import signup
# from . import auths


urlpatterns = [
    
    path('student_dashboard/', HomepageView.as_view(), name='dashboardView'),
    
    # My user_auth path
    path('signup/', Signup.as_view(), name='signup'),
    # path('signup/', signup, name='signup'),
    # path('signup/', auths.signup, name='signup'),
    # path('signup/', views.signup, name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),

    # path('profile/<int:student_id>/', view_profile, name='student_profile'),
    path('send_message/', views.send_message, name='send_message'),
    path('add', Add_Students.as_view(), name='add_student'),

    path('<slug:slug>/', view_profile, name='student_profile'),
    path('delete/<slug:slug>/', delete_student, name='delete_student'),

]
