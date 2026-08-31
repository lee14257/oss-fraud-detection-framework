import logging
import json
from src.ingestion.event import TransactionEvent
from src.rules.engine import RuleEvaluationResult

class AuditLogger:
    """Immutable decision and execution auditor for compliance verification."""
    
    def __init__(self):
        self.logger = logging.getLogger("FraudAuditLogger")
        self.logger.setLevel(logging.INFO)

    def log_decision(self, event: TransactionEvent, result: RuleEvaluationResult) -> Dict[str, Any]:
        audit_entry = {
            "event_id": event.transaction_id,
            "account_id": event.account_id,
            "rule_id": result.rule_id,
            "action_taken": "FLAG" if result.triggered else "PASS",
            "latency_ms": result.execution_latency_ms,
            "condition_breakdown": result.evaluations,
            "timestamp": result.evaluated_at.isoformat()
        }
        self.logger.info(json.dumps(audit_entry))
        return audit_entry