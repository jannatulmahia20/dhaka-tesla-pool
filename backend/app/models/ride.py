import uuid
from datetime import datetime

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    BigInteger,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.enums import RideStatus


class RideRequest(Base):
    __tablename__ = "ride_requests"

    __table_args__ = (
        CheckConstraint(
            "seats_requested > 0",
            name="check_ride_seats_positive",
        ),
        CheckConstraint(
            "estimated_fare_paisa >= 0",
            name="check_ride_fare_non_negative",
        ),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    passenger_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    pickup_zone_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("zones.id"),
        nullable=False,
    )

    destination_zone_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("zones.id"),
        nullable=False,
    )

    seats_requested: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    estimated_fare_paisa: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    status: Mapped[RideStatus] = mapped_column(
        Enum(RideStatus),
        nullable=False,
        default=RideStatus.REQUESTED,
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    passenger = relationship("User")

    pickup_zone = relationship(
        "Zone",
        foreign_keys=[pickup_zone_id],
    )

    destination_zone = relationship(
        "Zone",
        foreign_keys=[destination_zone_id],
    )