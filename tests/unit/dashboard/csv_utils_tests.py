# -*- coding: utf-8 -*-
import datetime
from six.moves import cStringIO
from six import text_type

from django.test import TestCase

from oscar.apps.dashboard.reports.csv_utils import CsvUnicodeWriter


class TestCsvWriter(TestCase):

    def test_(self):
        s = u'ünįcodē'
        class unicodeobj(object):
            def __unicode__(self):
                return s
        rows = [
            [s, s.encode('utf-8'), unicodeobj(), 123, datetime.date.today()]
        ]
        f = cStringIO.StringIO()
        CsvUnicodeWriter(f).writerows(rows)
        f.seek(0)
        self.assertEqual(
            f.read().decode('utf-8-sig').strip(),
            u','.join((s, s, s, u'123', text_type(datetime.date.today())))
        )
        f = cStringIO.StringIO()
        self.assertRaises(TypeError, CsvUnicodeWriter(f).writerows, [object()])
