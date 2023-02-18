import json
import requests
import Common.conf as conf


def api_check_version(version):
    try:
        params = {"version": version}
        res = requests.get(url=conf.API_NICEME_CHECK_VERSION, params=params)
        if json.loads(res.text).get("code") == "1":
            return True
        else:
            return False
    except Exception as e:
        return False
