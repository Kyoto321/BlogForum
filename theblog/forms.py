from django import forms
from .models import Post, Category

#choices = [('coding', 'coding'), ('sports', 'sports'), ('entertaiment', 'entertainment')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
	choice_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'header_image', 'body', 'category', 'snippet', 'author')

		widgets= {
			'title' : forms.TextInput(attrs={'class' : 'form-control'}),
			'title_tag' : forms.TextInput(attrs={'class' : 'form-control'}),
			'body' : forms.Textarea(attrs={'class' : 'form-control'}),
			'category' : forms.Select(choices=choice_list, attrs={'class' : 'form-control'}),
			#'author' : forms.Select(attrs={'class' : 'form-control'}),
			'author' : forms.TextInput(attrs={'class' : 'form-control',  'value':'', 'id':'main', 'type':'hidden'}),
			'snippet' : forms.Textarea(attrs={'class' : 'form-control'}),

		}


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'body', 'snippet')

		widgets= {
			'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Title Placeholder'}),
			'title_tag' : forms.TextInput(attrs={'class' : 'form-control'}),
			'body' : forms.Textarea(attrs={'class' : 'form-control'}),
			#'author' : forms.Select(attrs={'class' : 'form-control'}),
			'snippet' : forms.Textarea(attrs={'class' : 'form-control'}),


		}