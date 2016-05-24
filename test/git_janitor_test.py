from src.git_janitor import GitJanitor
import unittest

class GitJanitorTest(unittest.TestCase):

    def test_want_to_delete_remote(self):
        gj = GitJanitor("--remote")
        self.assertTrue(gj.want_to_delete_remote(), True)

    def test_want_to_clean(self):
        gj = GitJanitor("--clean")
        self.assertTrue(gj.want_to_clean(), True)

if __name__ == '__main__':
    unittest.main()
