#!/usr/bin/env python

from flask import Flask
from unittest import TestCase
import requests
import dv

class TestDV(TestCase):
    def setUp(self):
        dv.app.testing=True
        self.app = dv.app.test_client()
    def test_index(self):
        r=self.app.get('/')
        self.assertEqual(200,r.status_code)
    def test_storage_query(self):
        dset='ThisIsNotARealPID'
        r = self.app.get('api/datasets/:persistentId/', query_string={'persistentId':'doi:10.5072/FK2/%s'%dset})
        self.assertEqual(200,r.status_code)
        j = r.get_json()
        fs = j['data']['latestVersion']['files']
        self.assertEqual(1, len(fs))
        pkg = fs[0]
        sid = pkg['dataFile']['storageIdentifier']
        self.assertEqual('16389c3b4de-8052ecdd77c1',sid) # aka - this is what we've got in testdata

