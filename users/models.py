from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class Meta :
        db_table = "user_list"
    
    follow = models.ManyToManyField(
        'self', #내 자신을 연결 User
        symmetrical=False, #서로 동일하지 않게 해주겠다 => 서로 팔로워가 되어있지않아도 ㄱㅊ아요.
        through = "Follow" #중간 모델 직접정의
        )
    
class Follow(models.Model):
    class Meta:
        db_table = "follow_list"
    #자기자신을 manytomany로 연결해서 두개의 fk가 유저에서 나오는것을 볼 수 있죵?
    follower = models.ForeignKey(User, related_name="following",on_delete=models.CASCADE)
    followee = models.ForeignKey(User,related_name="followers", on_delete=models.CASCADE)
    
    #  역 관계 :oreignKey나 OneToOneField, ManyToManyField와 같은 관계 필드를 정의할 때 자동으로 생성되는 관계
    #  이러한 역관계의 생성시 기본 :  소문자클라스이름_ser(follow_set) 
    #  related_name 을 활용하여 이름을 바꿔서 
    #  쉽게 명칭을 정해 모델의 각 데이터를 불러 올 수 있다.
    #  예) user1_following = user1.following.all()
    followed_at =models.DateTimeField("팔로워한날",auto_now_add=True)


class Profile(models.Model):
    class Meta:
        db_table = "profile"
        
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    # ForeignKey 또는 OneToOneField, manytomany와 같은 관계 필드를 사용할 때 관련된 모델 간에 반대 방향으로 참조를 자동으로 제공, 즉 유저모델에서 profile모델에 들어가 데이터를 불러올수 있음
    intro = models.TextField("소개글", max_length= 500)
    birth_date = models.DateField("생년월일")
    portrait = models.ImageField("프로필사진",upload_to="profile/",blank=True, null=True)
