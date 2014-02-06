# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Review.user_name'
        db.add_column(u'krsk24au_info_review', 'user_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Review.user_name'
        db.delete_column(u'krsk24au_info_review', 'user_name')


    models = {
        u'krsk24au_info.review': {
            'Meta': {'ordering': "['-date_time']", 'object_name': 'Review'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'good_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'uniq': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['krsk24au_info.User']"}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'krsk24au_info.user': {
            'Meta': {'object_name': 'User'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['krsk24au_info']