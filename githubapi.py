import urllib.request, json, requests
import unittest

#gianna miggins
#SSW 567 Homework 4a 

def getRepos():
    #input github username
    user = 'giannamiggins'
    #input("Enter a github username")
    print("searching", user,"'s repositories...")


    #build url with input
    url = "https://api.github.com/users/{}/repos".format(user)
    print(url)

    #save to json file
    solid = requests.get(url)
    data = solid.json()
    with open('data.json', 'w') as f:
        json.dump(data, f)

    #number of repos
    length = len(data)
    print(user, " has", length, "public repositories")

    #output Repo: 'name of repo' Number of commits: 'num'
    x=0
    output = {}
    for x in range(0,length):
        name = data[x]["name"]
        
        url2 = "https://api.github.com/repos/{}/{}/commits".format(user, name)
        get2 = requests.get(url2)
        comdata = get2.json()
        
        #number of commits
        commits = len(comdata)
        
        print("Repo: ", name, "     Number of Commits: ", commits)
        #save to a json file in order to test that the output if correct
        output[name] = commits
        x += 1

    print(output)
    return output

#when commits are over 30, it defaults to 30
class TestGitRepos(unittest.TestCase):
    def testGiannaRepo(self):
        self.assertEqual(getRepos(), {'FocusTheHedgehog': 30, 'GEDCOM_Project': 30, 'helloworld': 1, 'magicdeck': 30, 'twitterAPI': 2})

if __name__ == '__main__':

    unittest.main(exit=False)