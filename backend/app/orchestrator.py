from app.agents.security_agent import SecurityAgent
from app.agents.api_testing_agent import APITestingAgent
from app.agents.deployment_agent import DeploymentAgent
from app.reporting.report_generator import ReportGenerator

class Orchestrator:
    def __init__(self):
        self.reporter = ReportGenerator()

    def run_all(self, parsed_data):
        sec = SecurityAgent().run(parsed_data)
        api = APITestingAgent().run(parsed_data)
        dep = DeploymentAgent().run()

        agent_output = {
            "security": sec,
            "api_testing": api,
            "deployment": dep
        }
        
        report = self.reporter.generate(agent_output)

        return report