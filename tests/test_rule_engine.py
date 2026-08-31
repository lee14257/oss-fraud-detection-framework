import unittest
from datetime import datetime, timezone
from src.ingestion.event import TransactionEvent
from src.rules.conditions import HighAmountCondition
from src.rules.engine import RuleEngine
from src.audit.logger import AuditLogger

class TestFraudDetectionFramework(unittest.TestCase):

    def setUp(self):
        self.event = TransactionEvent(
            transaction_id="tx_100928",
            account_id="acc_88411",
            amount=15000.00,
            currency="USD",
            ip_address="192.168.1.1"
        )
        self.high_amount_cond = HighAmountCondition(threshold=10000.00)
        self.engine = RuleEngine(
            rule_id="RULE_LARGE_TRANSFER",
            conditions=[self.high_amount_cond]
        )
        self.audit_logger = AuditLogger()

    def test_rule_trigger_and_audit(self):
        result = self.engine.evaluate_transaction(self.event)
        
        # Assert Rule Execution
        self.assertTrue(result.triggered)
        self.assertTrue(result.evaluations["HIGH_AMOUNT_GT_10000.0"])
        self.assertLess(result.execution_latency_ms, 50.0)  # SLA check

        # Assert Audit Trail
        audit_entry = self.audit_logger.log_decision(self.event, result)
        self.assertEqual(audit_entry["action_taken"], "FLAG")
        self.assertEqual(audit_entry["event_id"], "tx_100928")

if __name__ == "__main__":
    unittest.main()