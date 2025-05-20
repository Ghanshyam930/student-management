from django.contrib import admin
from .models import (
    StudentProfile,
    TeacherProfile,
    AdminProfile,
    Subject,
    SubjectAssignment,
    AttendanceRecord,
    ClassSchedule,
    Notification,
    Performance,
    StudentDoubt
)

# StudentProfile Admin
@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'enrollment_number', 'department', 'year', 'section')
    search_fields = ('user__username', 'enrollment_number', 'department', 'section')
    list_filter = ('department', 'year', 'section')


# TeacherProfile Admin
@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department')
    search_fields = ('user__username', 'department')
    list_filter = ('department',)


# AdminProfile Admin
@admin.register(AdminProfile)
class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)


# Subject Admin
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


# SubjectAssignment Admin
@admin.register(SubjectAssignment)
class SubjectAssignmentAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'subject')
    search_fields = ('teacher__user__username', 'subject__name')
    list_filter = ('teacher', 'subject')


# AttendanceRecord Admin
@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject_assignment', 'date', 'status')
    list_filter = ('date', 'status', 'subject_assignment')
    search_fields = ('student__user__username', 'subject_assignment__subject__name')


# ClassSchedule Admin
@admin.register(ClassSchedule)
class ClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('subject_assignment', 'day', 'start_time', 'end_time')
    list_filter = ('day',)
    search_fields = ('subject_assignment__subject__name', 'subject_assignment__teacher__user__username')


# Notification Admin
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('user__username', 'message')


# Performance Admin
@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject_assignment', 'quiz_marks', 'assignment_marks')
    list_filter = ('subject_assignment',)
    search_fields = ('student__user__username', 'subject_assignment__subject__name')


# StudentDoubt Admin
@admin.register(StudentDoubt)
class StudentDoubtAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject_assignment', 'doubt_text', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('student__user__username', 'subject_assignment__subject__name', 'doubt_text')
