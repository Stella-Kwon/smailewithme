from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("create/", views.create),
    # # path("create_page", views.create_page),
    # # <int:어쩌꼬> 계속 바뀔값의 데이터필드와 변수이름을 명시해주는것
    # #이 투두아이디는 detail_read에 명시해준 매개변수의 이름과 같아야한다.
    # path("<int:todo_id>/", views.read),
    # path("delete/<int:todo_id>/", views.delete),
    # path("update/<int:todo_id>/", views.update),
]