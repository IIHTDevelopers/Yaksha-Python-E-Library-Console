import unittest
from exception import ISBNDoesNotExistsError,ISBNAlreadyExistsError,BookNotAvailableError
from book_inventory import BookInventory
from book import Book
from issue import Issue
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        b=Book("11","Python","X Publicatiton","IT")
        BookInventory.add_book(b)
    def test_error_at_add_book(self):
        test_obj = TestUtils()
        try:
            b=Book("11","Python","Y Publicatiton","IT")
            BookInventory.add_book(b)
            test_obj.yakshaAssert("TestErrorAtAddBook", False, "exception")
            print("TestErrorAtAddBook = Failed")
        except ISBNAlreadyExistsError:
            test_obj.yakshaAssert("TestErrorAtAddBook", True, "exception")
            print("TestErrorAtAddBook = Passed")

    def test_error_at_issue_book(self):
        test_obj = TestUtils()
        try:
            i=Issue("12345","Venu","16-11-2021")
            BookInventory.issue_book(i)
            test_obj.yakshaAssert("TestErrorAtIssueBook", False, "exception")
            print("TestErrorAtIssueBook = Failed")
        except ISBNDoesNotExistsError:
            test_obj.yakshaAssert("TestErrorAtIssueBook", True, "exception")
            print("TestErrorAtIssueBook = Passed")
    def test_error_at_issue_book_of_non_exist(self):
        test_obj = TestUtils()
        try:
            i=Issue("11","Karthik","16-11-2021")
            BookInventory.issue_book(i)
            i=Issue("11","Chary","17-11-2021")
            BookInventory.issue_book(i)
            test_obj.yakshaAssert("TestErrorAtIssueBookOfNonExist", False, "exception")
            print("TestErrorAtIssueBookOfNonExist = Failed")
        except BookNotAvailableError:
            test_obj.yakshaAssert("TestErrorAtIssueBookOfNonExist", True, "exception")
            print("TestErrorAtIssueBookOfNonExist = Passed")
