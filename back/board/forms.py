from django import forms
from .models import FinancialProduct, Review, Comment

class FinancialProductForm(forms.ModelForm):
    class Meta:
        model = FinancialProduct
        fields = ['name', 'description', 'provider']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rating']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)])
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4})
        }