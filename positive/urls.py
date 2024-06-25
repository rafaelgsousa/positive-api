from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import *

view_album_meeting = SimpleRouter()
view_album_meeting.register('', AlbumMeetingView, basename='album_meeting-router')

view_comment_course = SimpleRouter()
view_comment_course.register('', CommentCourseView, basename='comment_course-router')

view_course = SimpleRouter()
view_course.register('', CourseView, basename='course-router')

view_ebook = SimpleRouter()
view_ebook.register('', EBookView, basename='ebook-router')

view_planner = SimpleRouter()
view_planner.register('', PlannerView, basename='planner-router')

view_image_album_meeting = SimpleRouter()
view_image_album_meeting.register('', ImageAlbumMeetingView, basename='image_album_meeting-router')

view_meeting = SimpleRouter()
view_meeting.register('', MeetingView, basename='meeting-router')

view_news = SimpleRouter()
view_news.register('', NewsView, basename='news-router')

view_user_analysis = SimpleRouter()
view_user_analysis.register('', WheelUserAnalysisView, basename='user_analysis-router')

view_user = SimpleRouter()
view_user.register('', CustomUserView, basename='user-router')

view_video_course = SimpleRouter()
view_video_course.register('', VideoCourseView, basename='video_course-router')

view_video_meeting = SimpleRouter()
view_video_meeting.register('', VideoMeetingView, basename='video_meeting-router')

view_welcome = SimpleRouter()
view_welcome.register('', WelcomeView, basename='welcome-router')

urlpatterns = [
    path('user/', include(view_user.urls)),
    path('user_analysis/', include(view_user_analysis.urls)),
    path('welcome/', include(view_welcome.urls)),
    path('meeting/', include(view_meeting.urls)),
    path('video_meeting/', include(view_video_meeting.urls)),
    path('album_meeting/', include(view_album_meeting.urls)),
    path('image_album_meeting/', include(view_image_album_meeting.urls)),
    path('course/', include(view_course.urls)),
    path('video_course/', include(view_video_course.urls)),
    path('comment_course/', include(view_comment_course.urls)),
    path('news/', include(view_news.urls)),
    path('ebook/', include(view_ebook.urls)),
    path('planner/', include(view_planner.urls)),
]
