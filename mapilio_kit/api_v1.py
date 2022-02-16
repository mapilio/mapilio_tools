import os
import requests
from typing import Union

MAPILIO_GRAPH_API_ENDPOINT = os.getenv(
    "MAPILIO_GRAPH_API_ENDPOINT", "https://end.mapilio.com/api"
)
MAPILIO_GRAPH_API_URL_FUNCTION = '/function/mapilio/imagery/'
MAPILIO_GRAPH_API_ENDPOINT_UPLOAD = MAPILIO_GRAPH_API_ENDPOINT + MAPILIO_GRAPH_API_URL_FUNCTION + 'upload'
MAPILIO_GRAPH_API_ENDPOINT_DOWNLOAD = MAPILIO_GRAPH_API_ENDPOINT + MAPILIO_GRAPH_API_URL_FUNCTION + 'uploadDetails'
MAPILIO_UPLOAD_ENDPOINT_ZIP = "https://cdn.mapilio.com/upload/"


URL_Sequences = "https://end.mapilio.com/api/function/mapilio/imagery/getUploadsWithProject"
URL_Images = "https://end.mapilio.com/api/function/mapilio/imagery/getUploadsImagesWithProject"
URL_CDN = "https://cdn.mapilio.com/im/"

def get_upload_token(email: str, password: str) -> dict:
    resp = requests.post(
        f"{MAPILIO_GRAPH_API_ENDPOINT}/login",
        json={"email": email, "password": password},
    )
    resp.raise_for_status()

    return resp.json()


def fetch_organization(
        user_access_token: str, organization_id: Union[int, str]
) -> requests.Response:
    resp = requests.get(
        f"{MAPILIO_GRAPH_API_ENDPOINT}/{organization_id}",
        params={
            "fields": ",".join(["slug", "description", "name"]),
        },
        headers={
            "Authorization": f"OAuth {user_access_token}",
        },
    )
    resp.raise_for_status()
    return resp