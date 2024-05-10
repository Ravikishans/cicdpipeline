from github import Github, Auth
import os
import subprocess
import shutil


# G_TOKEN = os.getenv('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')
G_TOKEN = "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"
Token=os.getenv(G_TOKEN)
print(Token)
# print("G_TOKEN:", G_TOKEN)
# print("Type of G_TOKEN:", type(G_TOKEN))
# auth = Auth.Token(G_TOKEN)

# if isinstance(G_TOKEN, str):
#     auth = Auth.Token(G_TOKEN)
# else:
#     print("Error: G_TOKEN is not a valid string.")

if G_TOKEN is not None:
   auth = Auth.Token(G_TOKEN)
else:
   print("Error: G_TOKEN is None. Please set a valid GitHub token.")


g = Github(auth=auth)
repo_name = "ravikishans/CICDPipeline-html"
repo = g.get_repo(repo_name)
print(repo)
latest_commit = repo.get_commits()[0]

latest_commit_sha = latest_commit.sha
print(latest_commit_sha)

repo_url = repo.clone_url
destination_dir = "repo"

if os.path.exists("commit_hash.txt"):
    with open("commit_hash.txt", "r") as commit_hash_file:
        previous_commit_sha = commit_hash_file.read()

    if previous_commit_sha == latest_commit_sha:
        print("No new commits")
        exit(0)
else:
    print("Running for the first time")

with open("commit_hash.txt", "w") as file:
    file.write(latest_commit_sha)

if os.path.exists(destination_dir):
    shutil.rmtree(destination_dir)

subprocess.run(["git", "clone", repo_url, destination_dir])
print("Cloned repo")

subprocess.run(["bash", "deploy.sh"])

commit_hash_file = open("commit_hash.txt", "w")
commit_hash_file.write(latest_commit_sha)
commit_hash_file.close()

g.close()
