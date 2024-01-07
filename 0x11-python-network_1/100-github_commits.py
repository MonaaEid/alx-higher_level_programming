# Import requests and sys packages
import requests
import sys


repo = sys.argv[1]
owner = sys.argv[2]

url = f"https://api.github.com/repos/{owner}/{repo}"

response = requests.get(url)


if response.status_code == 200:
    data = response.json()

    # Print the repository information
    print("{}: {}",data["author"], data["name"] )
