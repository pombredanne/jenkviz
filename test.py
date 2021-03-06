#!/usr/bin/env python
# -*- coding: utf_8 -*
__author__ = "Benoit Delbosc"
__copyright__ = "Copyright (C) 2012 Nuxeo SA <http://nuxeo.com>"
"""
   jenkviz.test
   ~~~~~~~~~~~~~~~~

   Test cases
"""
import os
from tempfile import mkdtemp
from unittest import TestCase
from jenkviz.util import duration_to_second
from jenkviz.util import split_jenkins_url
from jenkviz.main import main


class JenkVizTestCase(TestCase):
    def test_duration(self):
        self.assertEquals(duration_to_second('8 sec'), 8)
        self.assertEquals(duration_to_second('8.8 sec'), 8)
        self.assertEquals(duration_to_second('1 min'), 60)
        self.assertEquals(duration_to_second('1 min 1 sec'), 61)
        self.assertEquals(duration_to_second('10 min 10 sec'), 610)
        self.assertEquals(duration_to_second('1 sec'), 1)
        self.assertEquals(duration_to_second('55 sec'), 55)
        self.assertEquals(duration_to_second('1 hr 1 sec'), 3601)
        self.assertEquals(duration_to_second('1 hr 1 min 1 sec'), 3661)

    def test_graphviz(self):
        tmp_dir = mkdtemp('_jenkviz')
        svg_file = os.path.join(tmp_dir, 'test.svg')
        ret = main(['jenkviz', 'crawl', 'http://foo/jenkins/job/nuxeo-features-master/72/', '--from-file=test-data', '-o', svg_file])
        self.assertEquals(ret, 0)

    def test_graphviz_direct(self):
        tmp_dir = mkdtemp('_jenkviz')
        svg_file = os.path.join(tmp_dir, 'test-direct.svg')
        ret = main(['jenkviz', 'crawl', 'http://foo/jenkins/job/nuxeo-features-master/72/', '--from-file=test-data', '-o', svg_file, '--direct'])
        self.assertEquals(ret, 0)

    def test_split_jenkins_url(self):
        server, path, base_path, name, build = split_jenkins_url('http://qa.nuxeo.org/jenkins/job/nuxeo-features-master/103/')
        self.assertEquals(server, 'http://qa.nuxeo.org')
        self.assertEquals(path, '/jenkins/job/nuxeo-features-master/103/')
        self.assertEquals(base_path, '/jenkins/job')
        self.assertEquals(name, 'nuxeo-features-master')
        self.assertEquals(build, '103')
