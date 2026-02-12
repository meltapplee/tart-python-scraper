from django.db import models

class Column(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField("칼럼 아이디", max_length=255, unique=True)
    title = models.CharField("칼럼 제목", max_length=255)
    summary = models.TextField("칼럼 미리보기? 요약? 카드 밑에 나타나는 내용")
    image = models.URLField("칼럼 이미지 URL")
    date = models.DateField("발행 날짜")

    class Meta:
        db_table = "column"
