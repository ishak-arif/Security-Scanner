import subprocess
import json
import sys

def scan_file(target_path):
    # semgrep command
    command = [
        "semgrep", "scan", "--json", 
        "--config", "p/python",
        "--config", "p/security-audit",
        "--config", "p/secrets",
        "--config", "p/owasp-top-ten",
        "--quiet", target_path]

    try:
        # start scan
        result = subprocess.run(command, capture_output=True, text=True)
        
        # parse json
        data = json.loads(result.stdout)
        
        results = data.get("results", [])
        
        if not results:
            print(f"No vulnerabilities found in {target_path}")
            return
        
        severity_counter = {"ERROR": 0, "WARNING": 0, "INFO": 0}
        for result in results:
            severity = result.get("extra").get("severity")

            if severity in severity_counter:
                severity_counter[severity] += 1
            else:
                severity_counter[severity] = 1
        

        # list vulnerabilities
        print("Summary of vulnerabilities:")
        for level, count in severity_counter.items():
            print(f"{level}: {count}")
        
        print("List of vulnerabilities:")

        # severity weighting
        severity_order = {"ERROR": 0, "WARNING": 1, "INFO": 2, "UNKNOWN": 3}

        # sort results by severity
        sorted_results = sorted(results, key=lambda r: severity_order.get(
            r.get("extra", {}).get("severity", "UNKNOWN"), 999
        ))

        for result in sorted_results:
            severity = result.get("extra").get("severity")
            rule_id = result.get("check_id")
            line = result.get("start", {}).get("line")
            message = result.get("extra", {}).get("message")
            
            print(f"{severity.upper()} [{rule_id}] : Line {line}:")
            print(f"-> {message}\n")

    except Exception as e:
        print(f"Error running Semgrep: {e}")

if __name__ == "__main__":
    target = "target_file.py" 
    scan_file(target)