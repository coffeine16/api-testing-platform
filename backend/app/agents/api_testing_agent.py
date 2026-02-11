import requests

class APITestingAgent:

    def run(self, parsed_data, base_url="http://localhost:8001"):
        results = []

        for ep in parsed_data["endpoints"]:
            if ep["method"] == "GET":
                url = base_url + ep["path"].replace("{user_id}", "1")

                try:
                    r = requests.get(url)

                    results.append({
                        "endpoint": ep["path"],
                        "status_code": r.status_code,
                        "passed": r.status_code < 500
                    })

                except Exception as e:
                    results.append({
                        "endpoint": ep["path"],
                        "error": str(e),
                        "passed": False
                    })

        return {
            "agent": "api_testing",
            "status": "completed",
            "results": results
        }
