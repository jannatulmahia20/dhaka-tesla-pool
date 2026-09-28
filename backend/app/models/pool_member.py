import uuid
from datetime import datetime

from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class PoolMember(Base):
    __tablename__ = "pool_members"

    __table_args__ = (
        UniqueConstraint(
            "pool_id",
            "ride_request_id",
            name="uq_pool_ride",
        ),
        CheckConstraint(
            "seats_allocated > 0",
            name="check_allocated_seats_positive",
        ),
        CheckConstraint(
            "fare_paisa >= 0",
            name="check_member_fare_non_negative",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    pool_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("pools.id"),
        nullable=False,
        index=True,
    )

    ride_request_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("ride_requests.id"),
        nullable=False,
        index=True,
    )

    seats_allocated: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    fare_paisa: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    joined_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    pool = relationship(
        "Pool",
        back_populates="members",
    )

    ride_request = relationship("RideRequest")