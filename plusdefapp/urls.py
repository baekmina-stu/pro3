from django.urls import path


from plusdefapp.views import hello_world, chatgptcb, index, DeleteHistory

app_name = "plusdefapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('chatgptcb/', chatgptcb, name="chatgptcb"),
    path("chatqptbot/", index, name='main'),
    path("delete/", DeleteHistory, name='deleteChat'),
]