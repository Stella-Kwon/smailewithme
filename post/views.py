from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from post.models import Post, Image, File
from django.conf import settings #media url
from .forms import PostForm, ImageForm, FileForm

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    if request.method == "GET":

        return render(request, 'post/index.html',{'posts' : posts, 'MEDIA_URL': settings.MEDIA_URL})
    elif request.method == "POST":
        pass
    else:
        return HttpResponse("Invalid request method" , status=405)
    


# @csrf_exempt   
# @login_required(login_url="/users/login/")
# def create(request):
#     # if request.user.is_authenticated:
#         if request.method == "POST":
#             title = request.POST['title']
#             author =request.user
#             content =request.POST['content']
#             image =request.FILES.get('image')
#             file = request.FILES.get('file')

#             # file = request.FILES.getlist('files')
#             # image = request.FILES.getlist('images')
#           1번쨰 방식
            # for img_file in request.FILES.getlist('images'):
            #     Image.objects.create(post=post, image=img_file)

            # for file in request.FILES.getlist('files'):
            #     File.objects.create(post=post, file=file)
            
            # 2번쨰 방식
#             # for f in file:
#             #     file_instance = File(file=f) # 클라스 인스턴스 생성
#             #     file_instance.save()
#             
#             # for img in image:
#             #     img_instance = Image(image=img)
#             #     img_instance.save()

#             Post.objects.create(
#                 title = title,
#                 author =author,
#                 content=content,
#                 image = image,
#                 file = file,
#                 )
#             return redirect('/todo/')
#         elif request.method =="GET":
#             return render(request,'post/create.html')
#         else:
#             return HttpResponse("Invalid request method" , status=405)
#     # else:  # if not request.user.is_authenticated:
#     #     # 로그인전 새로만들기 눌렀을때 로그인페이지로 next값 저장해주고 넘어가게해주기위해 만든것
#     #     login_url = f"/user/login/?next={request.path}"
#     #     return redirect(login_url)
@csrf_exempt   
@login_required(login_url="/users/login/")
def create(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save()
            print(post_form)
            print(f'포스트:{post}')
            #폼셋으로도 처리해줄 수 있다.
            for img_file in request.FILES.getlist('image'):
                image_form = ImageForm({'post': post.id}, {'image': img_file})
                if image_form.is_valid():
                    image_form.save()
                    
            for file in request.FILES.getlist('file'):
                file_form = ImageForm({'post': post.id}, {'image': file})
                if file_form.is_valid():
                    file_form.save()  
            return redirect('/post/')
        else:
            post_form = PostForm()
            image_form = ImageForm()
            file_form = FileForm()
            # 처음 방문할 때 폼 객체가 존재하지 않기 때문에 템플릿에서 {{ form.as_p }} 등의 폼 렌더링 메서드를 사용할 경우 오류가 발생할 수 있기때문에
        # context =  {'post_form': post_form, 'image_form' : image_form , 'file_form':file_form}
    elif request.method == "GET":
        posts = Post.objects.all() # fk로 참조되어있어서 image나 file access가능
        return render(request, 'post/create.html', {'posts': posts})
    else:
        return HttpResponse("Invalid request method" , status=405)
    