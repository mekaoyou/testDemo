from django.contrib import admin
from mysite.books.models import Publisher,Author,Book

class AuthorAdmin(admin.ModelAdmin):
	"""admin for author"""
	list_display = ('first_name','last_name','email')
	search_fields = ('first_name','last_name')
	
class BookAdmin(admin.ModelAdmin):
	"""admin for books"""
	list_display = ('title','publisher','publication_date')
	list_filter = ('publication_date','authors')
	date_hierarchy = 'publication_date'
	ordering = ('-publication_date',)
	fields = ('title', 'authors', 'publisher', 'publication_date')
	filter_horizontal = ('authors',)
	raw_id_fields = ('publisher',)
		

admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)

# Register your models here.
