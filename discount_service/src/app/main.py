from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Discount Service")


class DiscountRequest(BaseModel):
    product_id: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    promo_code: str | None = None


class DiscountResponse(BaseModel):
    discount_percent: float
    reason: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "discount-service"}


@app.post("/discounts/calculate", response_model=DiscountResponse)
def calculate_discount(request: DiscountRequest) -> DiscountResponse:
    promo_code = request.promo_code.upper() if request.promo_code else None

    if promo_code == "STUDENT10":
        return DiscountResponse(
            discount_percent=10.0,
            reason="Promo code STUDENT10 was applied",
        )

    if request.quantity >= 10:
        return DiscountResponse(
            discount_percent=7.0,
            reason="Bulk discount for quantity greater than or equal to 10 was applied",
        )

    return DiscountResponse(
        discount_percent=0.0,
        reason="No discount rule was matched",
    )
