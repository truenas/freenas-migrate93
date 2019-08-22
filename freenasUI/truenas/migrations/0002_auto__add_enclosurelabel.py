# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EnclosureLabel'
        db.create_table('truenas_enclosurelabel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('truenas', ['EnclosureLabel'])


    def backwards(self, orm):
        # Deleting model 'EnclosureLabel'
        db.delete_table('truenas_enclosurelabel')


    models = {
        'truenas.enclosurelabel': {
            'Meta': {'object_name': 'EnclosureLabel'},
            'encid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['truenas']