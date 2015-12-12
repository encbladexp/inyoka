# -*- coding: utf-8 -*-
"""
    tests.apps.wiki.test_utils
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Test the wiki utilities like join_pagename and normalize_pagename.

    :copyright: Copyright 2007 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from inyoka.utils.test import TestCase
from inyoka.utils.text import join_pagename, normalize_pagename
from inyoka.wiki.models import Page
from inyoka.wiki.utils import CircularRedirectException, get_safe_redirect_target


class TestWikiUtils(TestCase):

    def test_join_pagename(self):
        j = join_pagename
        self.assertEqual(j("Foo", "Bar"), "Foo/Bar")
        self.assertEqual(j("Foo", "Bar/Baz"), "Bar/Baz")
        self.assertEqual(j("Foo", "./Bar/Baz"), "Foo/Bar/Baz")
        self.assertEqual(j("Foo", "./Bar"), "Foo/Bar")
        self.assertEqual(j("Foo/Bar", "../Blah"), "Foo/Blah")
        self.assertEqual(j("Foo/Bar", "./Blah"), "Foo/Bar/Blah")
        self.assertEqual(j("Foo", "../../../Blub"), "Blub")

    def test_normalize_pagename(self):
        n = normalize_pagename
        self.assertEqual(n("Foo Bar"), "Foo_Bar")
        self.assertEqual(n("/Foo_Bar/"), "Foo_Bar")
        self.assertEqual(n("Foo%Bar?#"), "FooBar")

    def test_multiple_redirect(self):
        Page.objects.create(name='redirect_a', text='# X-Redirect: redirect_b')
        Page.objects.create(name='redirect_b', text='Test')
        self.assertEqual(get_safe_redirect_target('redirect_a'), 'redirect_b')

    def test_circular_redirect(self):
        Page.objects.create(name='circular_a', text='# X-Redirect: circular_b')
        Page.objects.create(name='circular_b', text='# X-Redirect: circular_a')
        self.assertRaises(CircularRedirectException,
                          get_safe_redirect_target,
                          'circular_a')
