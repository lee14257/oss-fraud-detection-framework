from abc import ABC, abstractmethod
from typing import List, Dict, Any
from datetime import datetime, timezone
from src.ingestion.event import TransactionEvent

class Condition(ABC):
    """Abstract base class for rule evaluation conditions."""
    
    @property
    @abstractmethod
    def condition_id(self) -> str:
        pass

    @abstractmethod
    def evaluate(self, event: TransactionEvent, context: Dict[str, Any]) -> bool:
        """Evaluates condition logic against an event and state context."""
        pass

@dataclass
class RuleEvaluationResult:
    rule_id: str
    triggered: bool
    evaluations: Dict[str, bool]
    execution_latency_ms: float
    evaluated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

class RuleEngine:
    """Core condition evaluation engine supporting granular condition inspection."""
    
    def __init__(self, rule_id: str, conditions: List[Condition]):
        self.rule_id = rule_id
        self.conditions = conditions

    def evaluate_transaction(self, event: TransactionEvent, context: Dict[str, Any] = None) -> RuleEvaluationResult:
        start_time = datetime.now(timezone.utc)
        context = context or {}
        evaluations = {}
        all_triggered = True

        for condition in self.conditions:
            res = condition.evaluate(event, context)
            evaluations[condition.condition_id] = res
            if not res:
                all_triggered = False

        latency = (datetime.now(timezone.utc) - start_time).total_seconds() * 1000.0

        return RuleEvaluationResult(
            rule_id=self.rule_id,
            triggered=all_triggered,
            evaluations=evaluations,
            execution_latency_ms=latency
        )