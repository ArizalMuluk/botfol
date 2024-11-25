import requests

# Your Github Token
GITHUB_TOKEN = "your_github_token"
# Your Username
USERNAME = "your_github_username"

# Fill in the username that you want to exclude, you can add it!
EXCLUDED_USERS = {"username1"}


def get_following():
    url = f"https://api.github.com/users/{USERNAME}/following"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()


def get_followers():
    url = f"https://api.github.com/users/{USERNAME}/followers"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)
    return response.json()


def unfollow_user(user):
    url = f"https://api.github.com/user/following/{user}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.delete(url, headers=headers)
    return response.status_code


def main():
    following = get_following()
    followers = get_followers()

    following_usernames = {user["login"] for user in following}
    followers_usernames = {user["login"] for user in followers}

    not_following_back = following_usernames - followers_usernames

    not_following_back -= EXCLUDED_USERS

    for user in not_following_back:
        print(f"Unfollowing {user}...")
        status_code = unfollow_user(user)
        if status_code == 204:
            print(f"Successfully unfollowed {user}.")
        else:
            print(f"Failed to unfollow {user}. Status code: {status_code}")


if __name__ == "__main__":
    main()
