import Laba01Main
import unittest
from Laba01Main import  *


class Test01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    def setUp(self):
        print("setUp")
    def test_ifemptyall(self):
        Laba01Main.line.insert(0, "")
        Laba01Main.count()
        self.assertEqual(Laba01Main.restext.cget("text"), errordata)
        print("---TEST 1")
    def test_ifemptyline(self):
        Laba01Main.char.insert(0, "a")
        Laba01Main.count()
        self.assertEqual(Laba01Main.restext.cget("text"), errordata)
        print("---TEST 2")
    def test_ifemptychar(self):
        Laba01Main.line.insert(0, "fksdfhj")
        Laba01Main.count()
        self.assertEqual(Laba01Main.restext.cget("text"), errordata)
        print("---TEST 3")
    def test_char(self):
        Laba01Main.char.insert(0, "kekcheburek")
        Laba01Main.count()
        self.assertEqual(Laba01Main.restext.cget("text"), errordata)
        print("---TEST 4")
    def tearDown(self):
        print("tearDown")
        line.entry.delete(0,'end')
        char.entry.delete(0, 'end')
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")







