"""MCP server for Proactive Production Incident Remediation."""
import sys
import json
from client import IncidentRemediationEngine

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "analyze_production_incident",
                "description": "Evaluates stack trace, isolates root cause, and generates runbook steps",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "log_payload": {"type": "object"}
                    },
                    "required": ["log_payload"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "analyze_production_incident":
            payload = params.get("arguments", {}).get("log_payload", {})
            res = IncidentRemediationEngine.analyze_incident(payload)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
