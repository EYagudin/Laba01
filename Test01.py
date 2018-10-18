import Laba01Main
import unittest
from Laba01Main import  *

class Test01(unittest.TestCase):
    def test_ifemptyall(self): #если все поля пустые
        print("---TEST 1")
        Laba01Main.line.insert(0, "")
        Laba01Main.count()
        self.assertEqual(Laba01Main.restext.cget("text"), errordata)
    def test_ifemptyline(self): #если пустое поле строки
        print("---TEST 2")
        Laba01Main.char.insert(0, "a")
        Laba01Main.count()
        self.assertEqual(Laba01Main.restext.cget("text"), errordata)
    def test_ifemptychar(self): #если пустое поле символа
        print("---TEST 3")
        Laba01Main.line.insert(0, "fkksdkkkfhj")
        Laba01Main.count()
        self.assertEqual(Laba01Main.restext.cget("text"), errordata)
    def test_char(self):
        print("---TEST 4") #если несколько симолов в поле символа
        Laba01Main.line.insert(0, "fkksdfkkkhj")
        Laba01Main.char.insert(0, "kek")
        Laba01Main.count()
        self.assertEqual(Laba01Main.restext.cget("text"), errorone)
    def test_noice(self):
        print("---TEST 5")  # если всё правильно
        Laba01Main.line.insert(0, "fkksdkkkfhj")
        Laba01Main.char.insert(0, "k")
        Laba01Main.count()
    def tearDown(self):
        print("Results:")
        print(labelres.cget("text"))
        print(restext.cget("text"))
        Laba01Main.clear()







