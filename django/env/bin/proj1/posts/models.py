from django.db import models

# Create your models here.
class Meta:
	db_table ='posts'

class Post (models.Model):
	id = models.AutoField(primary_key =True)
	post_likes = models.IntegerField(default=0,verbose_name="Лайки")
	title = models.CharField(max_length = 120,verbose_name="Заголовок")
	genre = (('r1','Роман'),('p','Поэма'),('r2','Рассказ'))
	genre = models.CharField(max_length=30,verbose_name="Жанр",choices= genre,default='r1')
	content = models.TextField(verbose_name="Текст",default= "Дефолтный текст")
	timestamp = models.DateTimeField(verbose_name="Время создания")
	updated = models.DateTimeField(verbose_name="Время обновления")
	post_author = models.ForeignKey('Author',null=True,blank=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

class Author(models.Model):
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=120,verbose_name= "Имя")
	last_name = models.CharField(max_length=120, verbose_name= "Фамилия")
	email =models.EmailField(verbose_name= "Email")

	def __unicode__(self):
		return self.first_name + " " + self.last_name

	def __str__(self):
		return self.first_name + " " + self.last_name

class Comment(models.Model):
	id = models.AutoField(primary_key= True)
	comment_text = models.TextField(verbose_name="Комментарий",default='')
	comment_article = models.ForeignKey(Post)

	def __unicode__(self):
		return self.comment_text

	def __str__(self):
		return self.comment_text