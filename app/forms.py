from django import forms
from .models import Quiz

# クイズを作るフォームの作成
class QuizForm(forms.ModelForm):
    id = forms.IntegerField(
        label='問題番号',
        min_value=0
        )
    quiz_content = forms.CharField(
        widget=forms.Textarea(attrs={'cols': '100', 'rows': '1'}), 
        label='問題',
        required=True
        )
    answer = forms.CharField(
        label='答え',
        required=True
        )
    category = forms.ChoiceField(
        label='大分類',
        widget=forms.Select,
        choices=(
            ('語学・文学','語学・文学'),
            ('歴史・地理・社会','歴史・地理・社会'),
            ( '理系学問','理系学問'),
            ( '文化・芸術','文化・芸術'),
            ('ライフスタイル','ライフスタイル'),
            ('芸能', '芸能'),
            ('アニメ・ゲーム', 'アニメ・ゲーム'),
            ('スポーツ', 'スポーツ'),
            ('その他', 'その他'),
        ),
        required=True,
    )
    sub_category = forms.CharField(
        max_length=255,
        label='小分類',
        required=False
        )

    class Meta:
        model = Quiz
        fields = '__all__'


class QuizDeleteForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput)



