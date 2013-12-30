# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductImage'
        db.create_table(u'products_productimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['products.Product'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'products', ['ProductImage'])

        # Adding model 'Product'
        db.create_table(u'products_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('short_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('short_description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=100, decimal_places=2)),
            ('sku', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('inventory', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('weight', self.gf('django.db.models.fields.FloatField')(default=1)),
            ('weight_units', self.gf('django.db.models.fields.CharField')(default='LB', max_length=10, blank=True)),
            ('total_sold', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], null=True, blank=True)),
        ))
        db.send_create_signal(u'products', ['Product'])

        # Adding M2M table for field categories on 'Product'
        m2m_table_name = db.shorten_name(u'products_product_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False)),
            ('category', models.ForeignKey(orm[u'products.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'ProductImage'
        db.delete_table(u'products_productimage')

        # Deleting model 'Product'
        db.delete_table(u'products_product')

        # Removing M2M table for field categories on 'Product'
        db.delete_table(db.shorten_name(u'products_product_categories'))


    models = {
        u'products.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Category']", 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'})
        },
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inventory': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '100', 'decimal_places': '2'}),
            'short_description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'sku': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'total_sold': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'weight': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'weight_units': ('django.db.models.fields.CharField', [], {'default': "'LB'", 'max_length': '10', 'blank': 'True'})
        },
        u'products.productimage': {
            'Meta': {'object_name': 'ProductImage'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['products.Product']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['products']