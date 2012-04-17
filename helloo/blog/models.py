from django.db import models
from taggit.managers import TaggableManager
from django import forms
from django.contrib import admin

class Post(models.Model):

    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField()
    tags = TaggableManager()
    order = models.CharField(max_length=2)
    picture_name = models.CharField(max_length=60, blank=True)
    ALIGNMENT_CHOICES = (
	('1', 'left'),
	('2', 'right'),
	('3', 'center'),
    )
    SIZE_CHOICES = (
	('1', 'small'),
	('2', 'medium'),
	('3', 'large'),
    )
    PIC_CHOICES = (
	('1', 'Include a picture'),
	('2', 'Don\'t include a picture'),
    )
    FILE_TYPE_CHOICES = (
	('gif', '.gif'),
	('jpg', '.jpf'),
	('bmp', '.bmp'),
    )
    include_picture = models.CharField(max_length=1, blank=True, choices=PIC_CHOICES)
    alignment = models.CharField(max_length=1, blank=True, choices=ALIGNMENT_CHOICES)
    size = models.CharField(max_length=1, blank=True, choices=SIZE_CHOICES)
    file_type = models.CharField(max_length=3, blank=True, choices=FILE_TYPE_CHOICES)
	
	
 #   def post_header(self, _title_size=3):
#	if include_picture == 1:
#	    if self.alignment == 1:
#		if self.size == 1:
#		    name = '/static/img/' + picture_name + '.' + file_type
#		    img_class = 'leftsmall'
#		    return _post_html(self, _title_size, name, img_class)
#		elif self.size == 2:
#		    name = '/static/img/' + picture_name + '.' + file_type
#		    img_class = 'leftmedium'
#		    return _post_html(self, _title_size, name, img_class)
#		elif self.size == 3:
#		    name = '/static/img/' + picture_name + '.' + file_type
#		    img_class = 'leftlarge'
#		    return _post_html(self, _title_size, name, img_class)
#	        else:
#	            return _post_html(self, _title_size, None, None)
#	    elif self.alignment ==2:
#		if self.size == 1:
#		    name = '/static/img/' + picture_name + '.' + file_type
#		    img_class = 'rightsmall'
#		    return _post_html(self, _title_size, name, img_class)
#		elif self.size == 2:
#		    name = '/static/img/' + picture_name + '.' + file_type
#		    img_class = 'rightmedium'
#		    return _post_html(self, _title_size, name, img_class)
#		elif self.size == 3:
#		    name = '/static/img/' + picture_name + '.' + file_type
#		    img_class = 'rightlarge'
#		    return _post_html(self, _title_size, name, img_class)
#	        else:
#	            return _post_html(self, _title_size, None, None)
#	    elif self.alignment == 3:
#		if self.size == 1:
#		    name = '/static/img/' + picture_name + '.' + file_type
#		    img_class = 'centersmall'
#		    return _post_html(self, _title_size, name, img_class)
#		elif self.size == 2:
#		    name = '/static/img/' + picture_name + '.' + file_type
#		    img_class = 'centermedium'
#		    return _post_html(self, _title_size, name, img_class)
#		elif self.size == 3:
#		    name = '/static/img/' + picture_name + '.' + file_type
#		    img_class = 'centerlarge'
#		    return _post_html(self, _title_size, name, img_class)
#	        else:
#	            return _post_html(self, _title_size, None, None)
#           else:
#                return _post_html(self, _title_size, None, None)
#	else:
#	    return _post_html(self, _title_size, None, None)
#			
#    def _post_html(self, _title_size, _name, _img_class):
#    	_image = _image_html(_name, _img_class)
#	_title = _title_html(self, _title_size)
#	_date_author = _date_author_html(self)
#	return _clean_post(_image, _title, _date_author)
#	
#   def _date_author_html(self):
#    	for tag in self.tags:
#	    if tag == 'news':
#	        _start = '<p class="meta"><span class="date"> '
#   		_date = self.created
#  		_middle = ' </span><span class="posted">Posted by '
#    		_end = '<a href="/blog/about/">Shane Gooden</a></span></p>'
#    		_date_and_author = ''.join(_start, _date, _middle, _end)
#	        return _date_and_author
#        return ''
#    
#    def _title_html(self, _title_size):
#        if not self.title == 'no_title':
#            _open = ''.join('<h', str(_title_size))
#	    _class = 'class="title"> '
#	    _close = ''.join(' </h', str(_title_size), '>')
#	    _title = ''.join(_open, _class, self.title, _close)
#	else:
#	    _title = ''
#	return _title
#	
#    def _image_html(_name, _img_class):
#    	if not (_name == None or _img_class=None):
#    	    _src = '<img src="'
#	    _class = '" class='
#	    _alt = ' alt="/static/img/img10.gif"'
#	    _close = ' />'
#	    _image = ''.join(_src, _name, _class, _img_class, _alt, _close)
#	else:
#	    _image = ''
#	return _image
#	
#    def _clean_post(_image, _title, _date_author):
#        _div_post = '<div class="post">'
#        _div_entry = '<div class="entry">'
#        _html1 = '\n'.join(_div_post, _div_title).rstrip()
#        _html2 = '\n'.join(_date_author, _div_entry, _image).rstrip().lstrip()
#        return '\n'.join(_html1, _html2)
#    
#
#    def post_footer(_disqus=False):
#    	_end_div= '</div>'
#    	_disqus = _disqus_script(_disqus)
#    	return '\n'.join(_end_div, _disqus, _end_div)
#    	
#    def _disqus_script(_disqus):
#    	if _disqus == True:
#    	    _script = d_script
#	else:
#	    _script = ''
#	return _script   
#    
    def __unicode__(self):
	return self.title

d_script = """<div id="disqus_thread"></div>
<script type="text/javascript">
    var disqus_shortname = 'fabnfool';
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
<a href="http://disqus.com" class="dsq-brlink">blog comments powered by <span class="logo-disqus">Disqus</span></a>"""

class Picture(models.Model):
    name = models.CharField(max_length=60)
    
    def __unicode__(self):
    	return self.name

class Image(models.Model):
    picture = models.ForeignKey(Picture)
    image = models.ImageField(upload_to='./')
    
    	
class InlineImage(admin.TabularInline):
    model = Image


class PictureAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

admin.site.register(Picture, PictureAdmin)


