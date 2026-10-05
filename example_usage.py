"""Example usage for Proactive Production Incident Remediation."""
from client import IncidentRemediationEngine

if __name__ == "__main__":
    incident = {
        "service": "checkout-gateway",
        "status_code": 504,
        "trace": "Upstream connection refused to redis-cluster:6379 after 5000ms timeout"
    }
    res = IncidentRemediationEngine.analyze_incident(incident)
    print("Severity:", res["severity"])
    print("Root Cause:", res["root_cause"])
    for step in res["remediation_runbook"]:
        print("->", step)
