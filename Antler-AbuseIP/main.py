from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()

@app.get('/')
def read_main():
     html_content = """
    <html>
        <head>
            <title>Antler</title>
        </head>
        <body>
            <h1>Welcome</h1>
        </body>
    </html>
    """
     return HTMLResponse(content=html_content, status_code=200)


@app.get('/abuse/{abip}')
async def abusescan(abip: str):
    contents = "YOUR_KEY"

    url = 'https://api.abuseipdb.com/api/v2/check'

    querystring = {
        'ipAddress': abip,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': contents
    }

    response = httpx.get(url, headers=headers, params=querystring)

    return response.json()