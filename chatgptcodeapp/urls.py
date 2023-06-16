from django.urls import path


from chatgptcodeapp.views import cgcode, DeleteHistory

app_name = "chatgptcodeapp"

urlpatterns = [
    path("chatqptcode/", cgcode, name='main'),
    path("delete/", DeleteHistory, name='deleteChat'),
]