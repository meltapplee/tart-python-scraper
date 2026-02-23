from django.db import models

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField("칼럼 아이디", max_length=255, unique=True)
    author = models.CharField("작성자", max_length=100)
    title = models.CharField("칼럼 제목", max_length=255)
    summary = models.TextField("본문 요약")
    image = models.URLField("이미지 URL")
    posted_at = models.DateField("발행 날짜")
    url = models.URLField("원문 링크")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "article"
