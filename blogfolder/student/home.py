import pdb
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Student, CohortGroup, Student_profile, Program


class HomepageView(View):
    def get(self, request):
        all_students = Student.objects.all()
        # print(all_students)
        # pdb.set_trace()

        context = {
            'students' : all_students
        }



        return render(request, 'cohorts/index.html', context = context)

# def HomepageView(request):
#         return render(request, 'cohorts/index.html')


# def view_profile(request):
#     return render(request, 'cohorts/profile.html')


# def view_profile(request, student_id):
    
#     student = Student.objects.get(id=student_id)
#     return render(request, 'cohorts/profile.html', {'student': student})


# def view_profile(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     related_students = Student.objects.filter(cohort=student.cohort).exclude(id=student_id)
    
#     return render(request, 'profile.html', {
#         'student': student,
#         'related_students': related_students
#     })


# from django.shortcuts import get_object_or_404

def view_profile(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    cohort_group = student.cohortgroup_set.all().first()
    if cohort_group:
        cohort_members = Student.objects.filter(
            cohortgroup = cohort_group

        ).exclude(id=student_id)
    else:
        cohort_members = Student.objects.none()
        
    context= {
        'student': student,
        'cohort_members': cohort_members,
        'cohort_group': cohort_group
    }    
    return render(request, 'cohorts/profile.html', context)
