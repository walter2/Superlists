#!/usr/bin/env python

from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_an_retrieve_it_later(self):
        #Jimmy checks out the web page at:
        self.browser.get(self.server_url)

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
        jimmys_list_url = self.browser.current_url
        self.assertRegex(jimmys_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Cut the grass in the garden')

        #The text box is inviting him to write more
        #He enters: 'Put the cut grass into the wheelie bin.'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Put the cut grass into the wheelie bin.')
        inputbox.send_keys(Keys.ENTER)

        #The page updates and shows now both entries.
        self.check_for_row_in_list_table('1: Cut the grass in the garden')
        self.check_for_row_in_list_table('2: Put the cut grass into the wheelie bin.')

        #Now a new user, Peter, comes along and visits the site

        ## We use a new browser session to make sure that no information
        ## of Jimmy is coming through from cookies etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        #Peter is visiting the websiete
        # and there is no sign of Jimmy's list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Cut the grass in the garden', page_text)
        self.assertNotIn('Put the cut grass into the wheelie bin.', page_text)

        #Peter starts his own list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        #Peter gets his own unique URL
        peters_list_url = self.browser.current_url
        self.assertRegex(peters_list_url, '/lists/.+')
        self.assertNotEqual(peters_list_url, jimmys_list_url)

        #There is no trace of Jimmy's list on Peter's site
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Cut the grass in the garden', page_text)
        self.assertNotIn('Put the cut grass into the wheelie bin.', page_text)

        #Jimmy and Peter moves on to different things.
