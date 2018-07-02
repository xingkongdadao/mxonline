import xadmin
from courses.models import *


class CourseAdmin(object):
    list_display = ['course_org', 'name', 'ditail', 'degree']
    search_fields = ['course_org', 'name', 'is_banner']
    list_filter = ['course_org', 'name', 'desc', 'ditail', 'is_banner', 'teacher', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums', 'category', 'tag', 'youneed_know', 'teacher_tell', 'add_time']


class LessonAdmin(object):

    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']


class BannerCourseAdmin(object):

    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
