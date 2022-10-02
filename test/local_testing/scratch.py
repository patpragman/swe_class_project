import base64
wtf = {'version': '1.0',
       'resource': '/dev-get',
       'path': '/default/dev-get',
       'httpMethod': 'GET',
       'headers':
           {'Content-Length': '0', 'Cookie': 'awsccc=eyJlIjoxLCJwIjoxLCJmIjoxLCJhIjoxLCJpIjoiNDNiOGYzYmYtZTU1ZC00ODgxLTlmY2MtNDA3YTM5YmFiZTIzIiwidiI6IjEifQ==', 'Host': 'botp4w3ryj.execute-api.us-west-2.amazonaws.com', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0', 'X-Amzn-Trace-Id': 'Root=1-6338f543-3e7155e35e67d4fd6b4da491', 'X-Forwarded-For': '24.237.81.149', 'X-Forwarded-Port': '443', 'X-Forwarded-Proto': 'https', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.5', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1'},
       'multiValueHeaders':
           {'Content-Length': ['0'],
            'Cookie': ['awsccc=eyJlIjoxLCJwIjoxLCJmIjoxLCJhIjoxLCJpIjoiNDNiOGYzYmYtZTU1ZC00ODgxLTlmY2MtNDA3YTM5YmFiZTIzIiwidiI6IjEifQ=='],
            'Host': ['botp4w3ryj.execute-api.us-west-2.amazonaws.com'],
            'User-Agent': ['Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0'],
            'X-Amzn-Trace-Id': ['Root=1-6338f543-3e7155e35e67d4fd6b4da491'],
            'X-Forwarded-For': ['24.237.81.149'],
            'X-Forwarded-Port': ['443'],
            'X-Forwarded-Proto': ['https'],
            'accept': ['text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'],
            'accept-encoding': ['gzip, deflate, br'],
            'accept-language': ['en-US,en;q=0.5'],
            'sec-fetch-dest': ['document'],
            'sec-fetch-mode': ['navigate'],
            'sec-fetch-site': ['none'],
            'sec-fetch-user': ['?1'],
            'upgrade-insecure-requests': ['1']},
       'queryStringParameters':
           {'type': 'image?path="/main.html"'},
       'multiValueQueryStringParameters': {'type': ['image?path="/main.html"']}, 'requestContext': {'accountId': '545455113134', 'apiId': 'botp4w3ryj', 'domainName': 'botp4w3ryj.execute-api.us-west-2.amazonaws.com', 'domainPrefix': 'botp4w3ryj', 'extendedRequestId': 'ZWtClgA0PHcEPiw=', 'httpMethod': 'GET', 'identity': {'accessKey': None, 'accountId': None, 'caller': None, 'cognitoAmr': None, 'cognitoAuthenticationProvider': None, 'cognitoAuthenticationType': None, 'cognitoIdentityId': None, 'cognitoIdentityPoolId': None, 'principalOrgId': None, 'sourceIp': '24.237.81.149', 'user': None, 'userAgent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0', 'userArn': None}, 'path': '/default/dev-get', 'protocol': 'HTTP/1.1', 'requestId': 'ZWtClgA0PHcEPiw=', 'requestTime': '02/Oct/2022:02:19:47 +0000', 'requestTimeEpoch': 1664677187585, 'resourceId': 'ANY /dev-get', 'resourcePath': '/dev-get', 'stage': 'default'}, 'pathParameters': None, 'stageVariables': None, 'body': None, 'isBase64Encoded': False}


with open("../../web_content/images/uaastudents.jpg", "rb") as jpg_file:
    print(base64.b64encode(jpg_file.read()).decode("utf-8"))