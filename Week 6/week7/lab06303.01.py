from github import Github
import requests
from github.Commit import Commit
from github.ContentFile import ContentFile
# remove the minus sign from the key
g = Github("de5a5b9cefe7be45eeec0d60e32474e1f003b345-")


#for repo in g.get_user("oreillyh").get_repos("dataRepresentation"):
    #print(repo.name)

#g = Github("g = Github("de5a5b9cefe7be45eeec0d60e32474e1f003b345-")
repo = g.get_repo("oreillyh/dataRepresentation")
print(repo.clone_url)
repo.create_file("test.txt", "test", "test")
{'content': ContentFile(path="oreillyh/dataRepresentation/test.txt"), 'commit': Commit(sha="de5a5b9cefe7be45eeec0d60e32474e1f003b345-")}

# ContentFile(path="oreillyh/dataRepresentation/test.txt") 
# Commit(sha="de5a5b9cefe7be45eeec0d60e32474e1f003b345-")

# print(repo.clone_url)")
# repo = g.get_repo("datarepresentationstudent/aPrivateOne")
# print(repo.clone_url)
# print (urlOfFile)
# pip install PyGithub
# g = Github("de5a5b9cefe7be45eeec0d60e32474e1f003b345-")
