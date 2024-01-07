# Import requests and sys packages
import requests
import sys

# Get the repository name and the owner name from the command line arguments
repo = sys.argv[1]
owner = sys.argv[2]

# Set the URL for the GitHub API
url = f"https://api.github.com/repos/{owner}/{repo}"

# Make a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()

    # Print the repository information
    print("Repository name:", data["name"])
    print("Repository description:", data["description"])
    print("Repository language:", data["language"])
    print("Repository stars:", data["stargazers_count"])
    print("Repository forks:", data["forks_count"])
else:
    # Print the error message
    print("Something went wrong:", response.reason)

