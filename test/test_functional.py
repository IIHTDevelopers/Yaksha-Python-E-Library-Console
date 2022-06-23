import unittest
from book_inventory import BookInventory
from book import Book
from issue import Issue
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.b=Book("22","Python","X Publicatiton","IT")
        BookInventory.add_book(cls.b)
    def test_add_book(self):
        b=Book("33","Java","Y Publicatiton","IT")
        BookInventory.add_book(b)
        test_obj = TestUtils()
        if len(BookInventory.Book_List)!=0:
            test_obj.yakshaAssert("TestAddBook", True, "functional")
            print("TestAddBook = Passed")
        else:
            test_obj.yakshaAssert("TestAddBook", False, "functional")
            print("TestAddBook = Failed")

    def test_issue_book(self):
        i=Issue("22","Venu","16-11-2021")
        BookInventory.issue_book(i)
        test_obj = TestUtils()
        if self.b.issue==True:
            test_obj.yakshaAssert("TestIssueBook", True, "functional")
            print("TestIssueBook = Passed")
        else:
            test_obj.yakshaAssert("TestIssueBook", False, "functional")
            print("TestIssueBook = Failed")

    def test_return_type(self):
        obj=BookInventory.show_inventory()
        test_obj = TestUtils()
        if type(obj)==type([]):
            test_obj.yakshaAssert("TestReturnType", True, "functional")
            print("TestReturnType = Passed")
        else:
            test_obj.yakshaAssert("TestReturnType", False, "functional")
            print("TestReturnType = Failed")
