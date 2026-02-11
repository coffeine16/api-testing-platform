import requests

class DeploymentAgent:

    def run(self, base_url="http://localhost:8000"):
        try:
            r = requests.get(f"{base_url}/health")

            return {
                "agent": "deployment",
                "status": "healthy" if r.status_code == 200 else "unhealthy",
                "status_code": r.status_code
            }

        except Exception as e:
            return {
                "agent": "deployment",
                "status": "unreachable",
                "error": str(e)
            }
