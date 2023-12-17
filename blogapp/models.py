from django.db import models

class Write(models.Model):
    title = models.CharField(max_length=100)  # 제목
    contents = models.TextField()  # 내용
    updated_at = models.DateTimeField(auto_now=True)  # 글 작성 시간

    def __str__(self):
        return f"{self.title} - {self.updated_at}"

class Comment(models.Model):
    write = models.ForeignKey(Write, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content} - {self.created_at}"