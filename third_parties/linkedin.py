import os
import requests

def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrape information from Linkedin profiles, Manually scrape the information from the LinkedIn profile. 
    This API call costs 1 credit in proxycurl. Use fetch_profile_from_gist() for free profile fetching."""

    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dic = { "Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(
        api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
    )

    return response


def fetch_profile_from_gist():
    """Fetching Haruka Ichinose's linkedin profile from the GitHub gist json file."""
    
    gist_url = "https://gist.githubusercontent.com/Jade1724/e4b9f184855e4ddde2547fec55eb87d4/raw/919bbadd5e071a34a4add264f4d8c6ffc5869202/haruka-ichinose.json"

    response = requests.get(gist_url)

    return response