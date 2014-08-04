#!/usr/bin/env python
#01_functional_test.py

from django.test import LiveServerTestCase
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Jimmy checks out the web page at:
        self.browser.get(self.live_server_url)

        #He notes that the header is called.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #He is invited to enter some tasks into the text box.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #He types 'Cut the grass in the garden'.
        inputbox.send_keys('Cut the grass in the garden')

        #When he hits enter, the page updates and shows:
        #'1. Cut the grass in the garden' as an item in the ToDo list.
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Cut the grass in the garden')

        #The text box is inviting him to write more
        #He enters: 'Put the cut grass into the wheelie bin.'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Put the cut grass into the wheelie bin.')
        inputbox.send_keys(Keys.ENTER)

        #The page updates and shows now both entries.
        self.check_for_row_in_list_table('1: Cut the grass in the garden')
        self.check_for_row_in_list_table('2: Put the cut grass into the wheelie bin.')


        #Jimmy wonders if the site will remember the items - the site has generated an unique url for him
        #after a reload of the url the items are still there, the unique url is explained.
        self.fail('Finish the tests now here.')

        #Jimmy moves on to different things.

#log
#2014-07-31
#- first test for Test-Django book, p. 6
#- initial user stories added, p. 14
#- user is called Jimmy
#- test implemented as unit test, p. 16
#- moved to its own folder functional_tests; renamed
# !from now on changes are tracked in git