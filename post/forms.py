from django import forms
from .models import Post,Image,File

# form은 모델과 연동을 통해 
# 여러 파일,사진등을 자동적으로 
# 데이터의 생성, 수정, 유효성 검사, 에러 메시지 표시 등에 관련 기능이 
# 풍부하기 떄문에 사용

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'content')
        
class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput())
    #모델필드 커스트 마이징 ::  특별한 위젯 설정을 적용하기위해 
    #widget:
    #폼 필드를 HTML로 렌더링할 때 어떤 형태로 렌더링될 것인지를 결정하는 컴포넌트
    # 간단히 말해, 위젯은 데이터 입력을 위한 HTML 요소(예: <input>, <textarea>, <select> 등)를 생성
    # widget=forms.ClearableFileInput: ImageField의 기본 위젯을 ClearableFileInput으로 변경 => 업로드된 파일 삭제하는 지우기옵션 제공
    # attrs={'multiple': True} : 위젯의 속성을 설정하여, 사용자가 한 번에 여러 이미지 파일을 선택할 수 있게 해줌 => html <input type="file" name="image" multiple> mutilple 속성과 같음
    #하지만 애초에 그 속성이 가능한 위젯이 있기에 알아서 설정,  폼셋이든...
    class Meta:
        model = Image
        fields = ('image',)
        
class FileForm(forms.ModelForm):
    file = forms.ImageField(widget=forms.ClearableFileInput())
    class Meta:
        model = File
        fields = ('file',)