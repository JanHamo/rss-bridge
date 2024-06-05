import requests

bearer_token = 'AAAAAAAAAAAAAAAAAAAAANx%2FuAEAAAAA5mqLiMcmDq4RV1MeqeiDoyESWDE%3DRVakS3UWvEzjIcynpnzb16ChC1a19Ya7CRgEwcIJCWy4HcWqAq'

headers = {
    'Authorization': f'Bearer {bearer_token}',
}

response = requests.get('https://api.twitter.com/2/users/by/username/TwitterDev', headers=headers)

if response.status_code == 200:
    print('Bearer Token is valid.')
else:
    print('Bearer Token is invalid or does not have the required permissions.')
    print(response.json())
