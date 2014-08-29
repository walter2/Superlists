#!/usr/bin/env python

from .base import FunctionalTest
                               

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        #Jimmy goes to the home page and accidentally tries to
        #submit an empty list item.
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        #the home page refreshes, and there is an error message saying
        #that the list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You cannot have an empty list item.")

        #He tries again with some text and it works.
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        #He tries to add another blank list
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        #He receives a similar error page like on the list page
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You cannot have an empty list item.")

        #He can correct it by filling some text in
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
