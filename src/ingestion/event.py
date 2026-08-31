from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Any

@dataclass(frozen=True)
class TransactionEvent:
    """Immutable representation of a financial transaction event."""
    transaction_id: str
    account_id: str
    amount: float
    currency: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    ip_address: str = ""
    device_id: str = ""
    attributes: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "transaction_id": self.transaction_id,
            "account_id": self.account_id,
            "amount": self.amount,
            "currency": self.currency,
            "timestamp": self.timestamp.isoformat(),
            "ip_address": self.ip_address,
            "device_id": self.device_id,
            "attributes": self.attributes
        }