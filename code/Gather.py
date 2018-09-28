
import requests
import json
# curl -X POST -d '{"instanceID":"-1218240877"}' -H "Content-Type: application/json" 192.168.1.10:8080/api/getStats | python -m json.tool | less
class Gather:
    def __init__(self):
        pass

    def pull(self):
        r = requests.post(
            "http://192.168.1.10:8080/api/getStats",
            json={"instanceID":"-1218240877"},
        )
        return r.json()