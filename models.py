from django.db import models
from django.contrib.auth.models import User

# Student Profile
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    year = models.IntegerField()
    section = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


# Teacher Profile
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


# Admin Profile
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# Subject Model
class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Assign Subject to Teacher
class SubjectAssignment(models.Model):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher.user.username} - {self.subject.name}"


# Attendance Record Model
class AttendanceRecord(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject_assignment = models.ForeignKey(SubjectAssignment, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student.user.username} - {self.subject_assignment.subject.name} - {self.date}"


# Class Schedule Model
class ClassSchedule(models.Model):
    subject_assignment = models.ForeignKey(SubjectAssignment, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.subject_assignment} - {self.day} {self.start_time}-{self.end_time}"


# Notification Model
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To: {self.user.username} - {self.timestamp}"


# Performance Model
class Performance(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject_assignment = models.ForeignKey(SubjectAssignment, on_delete=models.CASCADE)
    quiz_marks = models.FloatField()
    assignment_marks = models.FloatField()

    def __str__(self):
        return f"{self.student.user.username} - {self.subject_assignment.subject.name}"


# Doubt Submission Model
class StudentDoubt(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject_assignment = models.ForeignKey(SubjectAssignment, on_delete=models.CASCADE)
    doubt_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.subject_assignment.subject.name}"

# from django.db import models
# from django.contrib.auth.models import User

# # Student Profile Model
# class StudentProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     enrollment_number = models.CharField(max_length=20, unique=True)
#     department = models.CharField(max_length=50)
#     year = models.IntegerField()
#     section = models.CharField(max_length=10)

#     def __str__(self):
#         return self.user.username


# # Teacher Profile Model
# class TeacherProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     department = models.CharField(max_length=50)

#     def __str__(self):
#         return self.user.username


# # Admin Profile Model
# class AdminProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username


# # Subject Model
# class Subject(models.Model):
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name


# # Subject Assignment: Assign Subject to Teacher
# class SubjectAssignment(models.Model):
#     teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.teacher.user.username} - {self.subject.name}"


# # Attendance Record Model
# class AttendanceRecord(models.Model):
#     student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
#     subject_assignment = models.ForeignKey(SubjectAssignment, on_delete=models.CASCADE)
#     date = models.DateField()
#     status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

#     def __str__(self):
#         return f"{self.student.user.username} - {self.subject_assignment.subject.name} - {self.date}"


# # Class Schedule Model
# class ClassSchedule(models.Model):
#     subject_assignment = models.ForeignKey(SubjectAssignment, on_delete=models.CASCADE)
#     day = models.CharField(max_length=10)
#     start_time = models.TimeField()
#     end_time = models.TimeField()

#     def __str__(self):
#         return f"{self.subject_assignment} - {self.day} {self.start_time} - {self.end_time}"


# # Notification Model
# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"To: {self.user.username} - {self.timestamp}"


# # Performance Model
# class Performance(models.Model):
#     student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
#     subject_assignment = models.ForeignKey(SubjectAssignment, on_delete=models.CASCADE)
#     quiz_marks = models.FloatField()
#     assignment_marks = models.FloatField()

#     def __str__(self):
#         return f"{self.student.user.username} - {self.subject_assignment.subject.name}"


# # Student Doubt Model
# class StudentDoubt(models.Model):
#     student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
#     subject_assignment = models.ForeignKey(SubjectAssignment, on_delete=models.CASCADE)
#     doubt_text = models.TextField()
#     submitted_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.student.user.username} - {self.subject_assignment.subject.name}"
