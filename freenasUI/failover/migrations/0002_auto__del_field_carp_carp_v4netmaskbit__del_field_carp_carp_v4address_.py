# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models


class Migration(DataMigration):

    def forwards(self, orm):

        # Adding field 'CARP.carp_interface'
        db.add_column('network_carp', 'carp_interface',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['network.Interfaces']),
                      keep_default=False)

        for o in orm['failover.CARP'].objects.all():
            iface = orm['network.Interfaces'].objects.create(
                int_interface='carp%d' % o.carp_vhid,
                int_ipv4address=o.carp_v4address,
                int_v4netmaskbit=o.carp_v4netmaskbit,
            )
            o.carp_interface = iface
            o.save()

        db.create_unique('network_carp', ['carp_interface_id'])


    def backwards(self, orm):

        # Deleting field 'CARP.carp_interface'
        db.delete_column('network_carp', 'carp_interface_id')


    models = {
        'failover.carp': {
            'Meta': {'object_name': 'CARP', 'db_table': "'network_carp'"},
            'carp_interface': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['network.Interfaces']", 'unique': 'True'}),
            'carp_pass': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'carp_skew': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'carp_vhid': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'carp_v4address': ('freenasUI.contrib.IPAddressField.IP4AddressField', [], {'default': "''", 'blank': 'True'}),
            'carp_v4netmaskbit': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '3', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'failover.failover': {
            'Meta': {'unique_together': "(('volume', 'carp'),)", 'object_name': 'Failover', 'db_table': "'system_failover'"},
            'carp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['failover.CARP']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipaddress': ('freenasUI.contrib.IPAddressField.IPAddressField', [], {}),
            'volume': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['storage.Volume']"})
        },
        'network.interfaces': {
            'Meta': {'ordering': "['int_interface']", 'object_name': 'Interfaces'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'int_dhcp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'int_interface': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'int_ipv4address': ('freenasUI.contrib.IPAddressField.IPAddressField', [], {'default': "''", 'blank': 'True'}),
            'int_ipv6address': ('freenasUI.contrib.IPAddressField.IPAddressField', [], {'default': "''", 'blank': 'True'}),
            'int_ipv6auto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'int_name': ('django.db.models.fields.CharField', [], {'max_length': "'120'"}),
            'int_options': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'int_v4netmaskbit': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '3', 'blank': 'True'}),
            'int_v6netmaskbit': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '4', 'blank': 'True'})
        },
        'storage.volume': {
            'Meta': {'object_name': 'Volume'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vol_encrypt': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'vol_encryptkey': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'vol_fstype': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'vol_guid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'vol_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '120'})
        }
    }

    complete_apps = ['failover']
