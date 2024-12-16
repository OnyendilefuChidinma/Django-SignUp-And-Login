# import pdb
# from re import S
import profile
from turtle import st
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from .models import Student, CohortGroup, Student_profile, Program, student_types, status_choices
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin


class HomepageView(LoginRequiredMixin,View):
    login_url = 'login'
    def get(self, request):
        all_students = Student.objects.all()
        # print(all_students)
        # pdb.set_trace()
        studentpaginator = Paginator(all_students, 4)
        page_numbers = request.GET.get('page')

        try:
            page_info = studentpaginator.get_page(page_numbers)
        except EmptyPage:
            pass

        print(page_info.has_next())

        context = {
            'students' : all_students,
            'students' : page_info,
            'student_rank': student_types
        }

        return render(request, 'cohorts/index.html', context = context)

def view_profile(request, slug):
    student = get_object_or_404(Student, slug=slug)
    cohort_group = student.cohortgroup_set.all().first()
    if cohort_group:
        cohort_members = Student.objects.filter(
            cohortgroup = cohort_group

        ).exclude(slug=slug)
    else:
        cohort_members = Student.objects.none()
        
    context= {
        'student': student,
        'cohort_members': cohort_members,
        'cohort_group': cohort_group
    }    
    return render(request, 'cohorts/profile.html', context)


def delete_student(request, slug):
    user = get_object_or_404(Student, slug=slug)
    user.delete()
    messages.success(request, f"{user.first_name} {user.last_name} has been deleted successfully.")
    return redirect('dashboardView')


from datetime import datetime
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
from django.views import View
# from .models import Student, Student_profile, Program, CohortGroup

class Add_Students(View):
    def post(self, request):
        # Safely get POST data
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        bio = request.POST.get('bio')
        cohort = request.POST.get('cohort')
        program = request.POST.get('program')
        student_role = request.POST.get('student_role')
        dateJoined = request.POST.get('dateJoined')
        rating = request.POST.get('rating')
        profile_image = request.FILES.get('profile_image')  # Handle file uploads
        date_of_birth = request.POST.get('date_of_birth')

        # Validate required fields
        if not username:
            return HttpResponse("Enter username")
        if not student_role:
            return HttpResponse("Enter student role")
        if not date_of_birth:
            return HttpResponse("Enter date of birth")

        # Parse date fields
        try:
            dateJoined = datetime.strptime(dateJoined, '%Y-%m-%d')
            date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
        except ValueError:
            return HttpResponse("Invalid date format. Use YYYY-MM-DD.")

        # Check for duplicate roles
        if student_role.lower() != "member" and Student.objects.filter(student_type__iexact=student_role).exists():
            return HttpResponse(f"The role {student_role} already exists")

        # Create student
        student = Student.objects.create(
            username=username,
            first_name=firstname,
            last_name=lastname,
            student_type=student_role,
            date_join=dateJoined
        )

        # Create student profile
        Student_profile.objects.create(
            student=student,
            bio=bio,
            date_of_birth=date_of_birth,
            rating=rating,
            profile_image=profile_image
        )

        # Create or get cohort
        cohort_group, created = CohortGroup.objects.get_or_create(name=cohort)
        cohort_group.students.add(student)

        # Create or get program
        Program.objects.create(
            courses=program,
            grade=0,  # Default value if grade is not provided
            student=student
        )

        return HttpResponse("All created successfully")
