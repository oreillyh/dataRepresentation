from github import Github
import requests
from github.Commit import Commit
from github.ContentFile import ContentFile
# remove the minus sign from the key
g = Github("")


#for repo in g.get_user("oreillyh").get_repos("dataRepresentation"):
 #   print(repo.name)

#g = Github("g = Github("")
repo = g.get_repo("oreillyh/dataRepresentation")

# print(repo.clone_url)
# print (urlOfFile)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url

#print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
#print(contentOfFile)

newContents = contentOfFile + "more stuff \n"

#print(newContents)

GitHubResponse = repo.update_file(fileInfo.path, "updated by prog", newContents,fileInfo.sha)

print(GitHubResponse)
