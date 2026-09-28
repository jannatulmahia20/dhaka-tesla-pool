import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.enums import RideStatus


class RideStatusHistory(Base):
    __tablename__ = "ride_status_history"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    ride_request_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("ride_requests.id"),
        nullable=False,
        index=True,
    )

    old_status: Mapped[RideStatus | None] = mapped_column(
        Enum(RideStatus),
        nullable=True,
    )

    new_status: Mapped[RideStatus] = mapped_column(
        Enum(RideStatus),
        nullable=False,
    )

    changed_by: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    changed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )