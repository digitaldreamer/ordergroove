from django.db import models
from django.template.defaultfilters import slugify

from django.contrib.sites.models import Site


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True)
    parent = models.ForeignKey('Category', blank=True, null=True)
    site = models.ForeignKey(Site, blank=True, null=True)
    active = models.BooleanField(blank=True, default=True)
    order = models.IntegerField(default=0)

    @classmethod
    def root_categories(cls, active=True):
        site = Site.objects.get_current()
        categories = Category.objects.filter(site=site)

        if active:
            categories = categories.filter(active=True)

        return categories.filter(parent__isnull=True).order_by('order')

    def __unicode__(self):
        ret = self.name

        if self.parent:
            ret = '%s | %s' % (self.parent.name, self.name)

        return ret

    def save(self, *args, **kwargs):
        # force the site
        if not self.site:
            self.site = Site.objects.get_current()

        # force the slug field if not populated
        if not self.slug:
            self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return_vars = {
            'category_slug': self.slug,
        }
        return('shop_products_category', (), return_vars)

    @property
    def children(self, active=True):
        site = Site.objects.get_current()
        categories = Category.objects.filter(site=site)

        if active:
            categories = categories.filter(active=True)

        return categories.filter(parent=self).order_by('order')

    class Meta:
        verbose_name_plural = 'Categories'
