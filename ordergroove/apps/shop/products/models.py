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
        """
        Get root categories filtered by site and active
        """
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

    def get_children(self, active=True):
        """
        Get children categories filtered by active
        """
        site = Site.objects.get_current()
        categories = Category.objects.filter(site=site)

        if active:
            categories = categories.filter(active=True)

        return categories.filter(parent=self).order_by('order')

    def get_products(self, featured=False, active=True):
        """
        Get all products that belong to the category
        """
        products = Product.objects.filter(categories=self)

        if active:
            products = products.filter(active=True)
        if featured:
            products = products.filter(featured=True)

        return products.order_by('order')

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

    class Meta:
        verbose_name_plural = 'Categories'


class ProductManager(models.Manager):
    def get_products(self, active=True):
        """
        Get all products filtered by site and and active
        """
        site = Site.objects.get_current()
        products = self.filter(site=site)

        if active:
            products = products.filter(active=True)

        return products.order_by('order')

    def featured(self, active=True):
        """
        Get all featured products
        """
        products = self.get_products(active=active)
        return products.filter(featured=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, blank=True, default='')
    slug = models.SlugField(blank=True, unique=True)
    active = models.BooleanField(blank=True, default=True)
    featured = models.BooleanField(blank=True, default=False)
    sku = models.CharField(max_length=255, blank=True, default='')
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    order = models.IntegerField(default=0)
    description = models.TextField(blank=True, default='')
    short_description = models.TextField(blank=True, default='')
    categories = models.ManyToManyField(Category, blank=True)
    inventory = models.IntegerField(default=0)
    weight = models.FloatField(default=1)
    weight_units = models.CharField(max_length=10, blank=True, default='LB')
    total_sold = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    site = models.ForeignKey(Site, blank=True, null=True)
    objects = ProductManager()

    def __unicode__(self):
        return self.name

    @property
    def main_image(self):
        """
        Get the first sorted product image
        """
        images = self.images

        if images.count() > 0:
            image = images[0]
        else:
            image = None

        return image

    @property
    def images(self):
        """
        Get all the product images
        """
        return self.productimage_set.order_by('order')

    @property
    def main_category(self):
        """
        Get the main category
        """
        category = None

        if self.categories.count() > 0:
            category = self.categories.order_by('order')[0]

        return category

    def save(self, *args, **kwargs):
        # force populate fields
        if not self.site:
            self.site = Site.objects.get_current()
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.sku:
            self.sku = self.slug
        if not self.short_name:
            self.short_name = self.name

        super(Product, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return_vars = {
            'product_slug': self.slug,
        }
        return('shop_products_product', (), return_vars)


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    order = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shop/products')
    description = models.TextField(blank=True, default='', help_text='Optional description')

    class Meta:
        verbose_name_plural = 'Product Images'
