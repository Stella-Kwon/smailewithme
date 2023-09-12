from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta:
        db_table = "post_list"
        
    author = models.ForeignKey(
                'users.User',
                verbose_name="글쓴이",
                null=True, #on_delete해주기위해
                related_name="author",
                on_delete=models.SET_NULL)
    title = models.CharField("제목",max_length=50)
    content = models.TextField('내용',max_length=8000)
    comment = models.ManyToManyField('users.User',related_name="comment",through='Comments')
    liked_post = models.ManyToManyField('users.User', through='PostLike', related_name='liked_posts')
    # image = models.ImageField(upload_to = 'posts/images/',null=True,blank=True)
    # file = models.FileField(upload_to = 'posts/files/',null=True,blank=True)
    #여러 파일을 넣으려면 파일 이미지 모델 따로 분리해서 폼 생성.
    created_at = models.DateTimeField("생성일",auto_now_add=True)
    updated_at = models.DateTimeField("수정일",auto_now=True)
    
    #여기서 User모델이 참조되는 인스턴스들이 많아서 => post_set으로 다 지정되다보니 혼동이 온다
    #그래서 related_name꼭 넣어주기
    def __str__(self):  # admin 페이지에 content를 대표로 보여주는것 , 그리고 실제 페이지애서 반영은 좀더 크기가 키워져 나온다.
        return self.content
class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to = 'posts/images/',null=True,blank=True)
class File(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to = 'posts/files/',null=True,blank=True)
class PostLike(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name="좋아요한 포스트")
    user = models.ForeignKey('users.User',on_delete=models.CASCADE,verbose_name="포스트 좋아요한 유저")
    # likes_count = models.IntegerField("좋아요 수",default=0)
#  좋아요 수는 해당 포스트 또는 댓글과 연결된 PostLike 또는 CommentLike 객체의 수로 계산가능
class Comments(models.Model):
    author = models.ForeignKey('users.User',related_name="comment_author",verbose_name="댓글 쓴 유저",on_delete =models.CASCADE)
    post = models.ForeignKey('Post',related_name="comment_post",verbose_name="댓글달린 포스트",on_delete =models.CASCADE)
    comment = models.TextField("댓글",max_length=1500,null=True,blank=True)
    #textfield는 말그대로 문자열만 나타내주기때문에 다른 모델과의 관계를 정의하지 않는다, 고로 on_delete옵션이 없음
    #그리고 이미 author나 post가 지워지면 코멘트도 사라지게되어있다. on_delete지워주기
    #모든 참조한 데이터들 on_delete로 사라지는 기능
    liked_comments = models.ManyToManyField('users.User',verbose_name="댓글좋아요",related_name="liked_comments",through="CommentLike")
    
class CommentLike(models.Model):
    comment = models.ForeignKey(Comments,on_delete=models.CASCADE,verbose_name="좋아요한 댓글")
    user = models.ForeignKey('users.User',on_delete=models.CASCADE,verbose_name="댓글 좋아요한 유저")
    # likes_count = models.IntegerField("좋아요 수",default=0)


