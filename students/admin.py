from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.html import format_html
from .models import Student, Course, Enrollment, Instructor, Semester

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'credits')  # Fields to display in the list view
    search_fields = ('title', 'code')  # Fields to search
    list_filter = ('credits',)  # Add filters

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')  # Fields to display
    search_fields = ('first_name', 'last_name', 'email')  # Search fields

# Register your models with custom admin classes
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment)
admin.site.register(Instructor)
admin.site.register(Semester)

class CustomAdminSite(admin.AdminSite):
    site_header = "Student Enrollment System"
    site_title = "Enrollment Admin"
    index_title = "Welcome to the Enrollment Admin"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            # Add custom URLs if needed
        ]
        return custom_urls + urls

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_css'] = staticfiles_storage.url('students/css/custom_admin.css')
        return context

admin_site = CustomAdminSite(name='custom_admin')
