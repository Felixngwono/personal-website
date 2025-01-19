from django.forms import ModelForm
from .models import BlogPost, PortfolioItem, User, contact
from django.contrib.auth.forms import UserCreationForm

class  MyUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = '__all__'

class BlogPostForm(ModelForm):
    class Meta:
        model=BlogPost
        fields='__all__'
        
        
class PortfolioForm(ModelForm):
    class Meta:
        model=PortfolioItem
        fields='__all__'
        
class  ContactusForm(ModelForm):
    
    class Meta:
        model = contact
        fields = '__all__'


