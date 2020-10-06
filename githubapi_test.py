import unittest
import githubapi

class test_git_api(unittest.TestCase):

    def test_repo_name(self): 
        self.assertIn('FocusTheHedgehog', githubapi.getRepos('giannamiggins'))
    def test_repo_name2(self): 
        self.assertIn('magicdeck', githubapi.getRepos('giannamiggins'))
    def test_sample(self): 
        self.assertEqual(githubapi.getRepos('richkempinski'), {'csp': 2, 'threads-of-life': 1, 'helloworld': 6, 'try_nbdev2': 5, 'Mocks': 2, 'try_nbdev': 2, 'hellogitworld': 30, 'Project1': 2, 'richkempinski.github.io': 9})

if __name__ == '__main__':
    print('3 unit tests running')
    unittest.main()