# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Type'
        db.create_table(u'magazine_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64)),
        ))
        db.send_create_signal(u'magazine', ['Type'])

        # Adding model 'Journal'
        db.create_table(u'magazine_journal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='journal', to=orm['magazine.Type'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=64)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True)),
            ('cnt_view', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'magazine', ['Journal'])

        # Adding model 'Number'
        db.create_table(u'magazine_number', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('journal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magazine.Journal'])),
            ('year', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=4)),
            ('number', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2)),
        ))
        db.send_create_signal(u'magazine', ['Number'])

        # Adding model 'NumberCover'
        db.create_table(u'magazine_numbercover', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magazine.Number'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True)),
            ('type', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cnt_view', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'magazine', ['NumberCover'])

        # Adding model 'Rubric'
        db.create_table(u'magazine_rubric', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('journal', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rubric', to=orm['magazine.Journal'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'magazine', ['Rubric'])

        # Adding model 'Article'
        db.create_table(u'magazine_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('journal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magazine.Journal'])),
            ('number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magazine.Number'])),
            ('rubric', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magazine.Rubric'])),
            ('page', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('cnt_view', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'magazine', ['Article'])

        # Adding model 'Text'
        db.create_table(u'magazine_text', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(related_name='text_set', to=orm['magazine.Article'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'magazine', ['Text'])

        # Adding model 'ArticleImage'
        db.create_table(u'magazine_articleimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['magazine.Article'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('note', self.gf('django.db.models.fields.TextField')()),
            ('cnt_view', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'magazine', ['ArticleImage'])

    def backwards(self, orm):
        # Deleting model 'Type'
        db.delete_table(u'magazine_type')

        # Deleting model 'Journal'
        db.delete_table(u'magazine_journal')

        # Deleting model 'Number'
        db.delete_table(u'magazine_number')

        # Deleting model 'NumberCover'
        db.delete_table(u'magazine_numbercover')

        # Deleting model 'Rubric'
        db.delete_table(u'magazine_rubric')

        # Deleting model 'Article'
        db.delete_table(u'magazine_article')

        # Deleting model 'Text'
        db.delete_table(u'magazine_text')

        # Deleting model 'ArticleImage'
        db.delete_table(u'magazine_articleimage')

    models = {
        u'magazine.article': {
            'Meta': {'ordering': "['page']", 'object_name': 'Article'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'cnt_view': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magazine.Journal']"}),
            'number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magazine.Number']"}),
            'page': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'rubric': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magazine.Rubric']"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'magazine.articleimage': {
            'Meta': {'object_name': 'ArticleImage'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magazine.Article']"}),
            'cnt_view': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'note': ('django.db.models.fields.TextField', [], {})
        },
        u'magazine.journal': {
            'Meta': {'object_name': 'Journal'},
            'cnt_view': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'journal'", 'to': u"orm['magazine.Type']"})
        },
        u'magazine.number': {
            'Meta': {'object_name': 'Number'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magazine.Journal']"}),
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2'}),
            'year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '4'})
        },
        u'magazine.numbercover': {
            'Meta': {'ordering': "['type']", 'object_name': 'NumberCover'},
            'cnt_view': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magazine.Number']"}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'magazine.rubric': {
            'Meta': {'object_name': 'Rubric'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rubric'", 'to': u"orm['magazine.Journal']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'magazine.text': {
            'Meta': {'ordering': "['id']", 'object_name': 'Text'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'text_set'", 'to': u"orm['magazine.Article']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'magazine.type': {
            'Meta': {'object_name': 'Type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '64'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['magazine']