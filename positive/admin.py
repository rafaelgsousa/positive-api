from django.contrib import admin

from positive.models import *

admin.site.register(CustomUser)
admin.site.register(AlbumMeeting)
admin.site.register(CommentCourse)
admin.site.register(Course)
admin.site.register(EBook)
admin.site.register(ImageAlbumMeeting)
admin.site.register(Meeting)
admin.site.register(News)
admin.site.register(Planner)
admin.site.register(WheelUserAnalysis)
admin.site.register(VideoCourse)
admin.site.register(VideoMeeting)
admin.site.register(Welcome)


class UserAdmin(admin.ModelAdmin):
    ...
