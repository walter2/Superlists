#!/usr/bin/env python

from .base import FunctionalTest
                               

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        #Jimmy goes to the home page and accidentally tries to
        #submit an empty list item.

        #the home page refreshes, and there is an error message saying
        #that the list items cannot be blank

        #He tries again with some text and it works.

        #He tries to add another blank list

        #He receives a similar error page like on the list page

        #He can correct it by filling in some text
        self.fail('write me!')
