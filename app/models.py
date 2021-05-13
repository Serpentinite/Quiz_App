from django.db import models
# from django.urls import reverse_lazy

class Quiz(models.Model):
    id = models.IntegerField(primary_key=True)
    quiz_content = models.TextField()
    answer = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    sub_category = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'quiz'

    # def get_absolute_url(self):
    #     return reverse_lazy('app:quiz_list')

