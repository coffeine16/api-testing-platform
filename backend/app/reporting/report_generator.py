class ReportGenerator:

    def generate(self, agent_output):
        security = agent_output["security"]
        api = agent_output["api_testing"]
        deployment = agent_output["deployment"]

        high_risks = len(security["findings"])
        failed_tests = len([r for r in api["results"] if not r.get("passed")])

        report = {
            "summary": {
                "high_risks": high_risks,
                "failed_tests": failed_tests,
                "deployment_status": deployment["status"]
            },
            "security_findings": security["findings"],
            "api_test_results": api["results"],
            "deployment": deployment,
            "recommendations": self._generate_recommendations(security, deployment)
        }

        return report

    def _generate_recommendations(self, security, deployment):
        recs = []

        if security["findings"]:
            recs.append("Implement object-level authorization checks (BOLA protection).")

        if deployment["status"] != "healthy":
            recs.append("Investigate deployment health and service availability.")

        if not recs:
            recs.append("No critical risks detected.")

        return recs
