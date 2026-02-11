class SecurityAgent:

    def run(self, parsed_data):
        findings = []

        for ep in parsed_data["endpoints"]:
            if ep.get("is_id_based") and ep["method"] == "GET":
                findings.append({
                    "endpoint": ep["path"],
                    "issue": "Potential BOLA",
                    "risk": "HIGH",
                    "confidence": "POTENTIAL",
                    "reason": "ID-based object access detected"
                })

        return {
            "agent": "security",
            "status": "completed",
            "total_findings": len(findings),
            "findings": findings
        }
