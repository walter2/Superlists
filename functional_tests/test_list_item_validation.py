#!/usr/bin/env python

from .base import FunctionalTest
                               

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        #Jimmy goes to the home page and accidentally tries to
        #submit an empty list item.
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        #the home page refreshes, and there is an error message saying
        #that the list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You cannot have an empty list item")

        #He tries again with some text and it works.
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        #He tries to add another blank list
        self.get_item_input_box().send_keys('\n')

        #He receives a similar error page like on the list page
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You cannot have an empty list item")

        #He can correct it by filling some text in
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        #Jimmy goes to the home page and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        #he accidentally tries to enter a duplicate
        self.get_item_input_box().send_keys('Buy wellies\n')

        #he sees a helpful error message
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'You have already got this in your list.')

