from src.rules.engine import Condition
from src.ingestion.event import TransactionEvent
from typing import Dict, Any

class HighAmountCondition(Condition):
    def __init__(self, threshold: float):
        self.threshold = threshold

    @property
    def condition_id(self) -> str:
        return f"HIGH_AMOUNT_GT_{self.threshold}"

    def evaluate(self, event: TransactionEvent, context: Dict[str, Any]) -> bool:
        return event.amount > self.threshold