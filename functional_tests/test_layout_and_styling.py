#!/usr/bin/env python

from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        #Jimmy goes to the home page and
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        #He notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width']/2,
                               512, delta=10)

        #When a new list is started the input box is centered
        # there as well
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width']/2,
                               512, delta=10)
