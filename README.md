# mbot github

## Overview
This is a Python script that interacts with the GitHub API to manage the users you are following. It helps you identify users who do not follow you back and allows you to unfollow them, while also providing the option to exclude certain users from being unfollowed.

## Features
- **Fetch Following Users**: Retrieves a list of users that the specified GitHub account is following.
- **Fetch Followers**: Retrieves a list of users that are following the specified GitHub account.
- **Unfollow Users**: Unfollows users who do not follow you back, excluding those specified in the exclusion list.

## Prerequisites
- Python 3.x
- `requests` library (can be installed via pip)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/mbot_github.git
## Navigate to the project directory:
```bash
cd mbot_github
```

## Install the required libraries:
```bash
pip install requests
```
## Configuration
Before running the script, you need to configure the following variables in the code:
- `GITHUB_TOKEN`: Your personal access token from GitHub.
- `USERNAME`: Your GitHub username.
- `EXCLUDED_USERS`: A set of usernames that you want to exclude from being unfollowed.

### Usage
To run the script, execute the following command in your terminal:
```bash
python mbot_github.py
```
### Example
```bash
# Example configuration
GITHUB_TOKEN = 'your_github_token'
USERNAME = 'your_github_username'
EXCLUDED_USERS = {'username1', 'username2'}
```
### Notes
- Make sure that your GitHub token has the necessary permissions to access your following and followers data.
- Use this script responsibly and be aware of GitHub's rate limits.
