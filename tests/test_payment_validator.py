
import pytest

from app.payment_validator import validate_payment


# Test 1: Valid payment should be approved
def test_valid_payment():
    result = validate_payment(
        vendor_id="V1001",
        vendor_status="Active",
        payment_amount=5000,
        bank_approved=True
    )

    assert result["status"] == "APPROVED"
    assert result["exceptions"] == []


# Test 2: Inactive vendor should be rejected
def test_inactive_vendor():
    result = validate_payment(
        vendor_id="V1002",
        vendor_status="Inactive",
        payment_amount=5000,
        bank_approved=True
    )

    assert result["status"] == "REJECTED"
    assert "Vendor is not active" in result["exceptions"]


# Test 3: Zero payment should be rejected
def test_zero_payment():
    result = validate_payment(
        vendor_id="V1003",
        vendor_status="Active",
        payment_amount=0,
        bank_approved=True
    )

    assert result["status"] == "REJECTED"
    assert "Payment amount must be greater than zero" in result["exceptions"]


# Test 4: Negative payment should be rejected
def test_negative_payment():
    result = validate_payment(
        vendor_id="V1004",
        vendor_status="Active",
        payment_amount=-100,
        bank_approved=True
    )

    assert result["status"] == "REJECTED"


# Test 5: Unapproved bank account should be rejected
def test_unapproved_bank_account():
    result = validate_payment(
        vendor_id="V1005",
        vendor_status="Active",
        payment_amount=5000,
        bank_approved=False
    )

    assert result["status"] == "REJECTED"
    assert "Vendor bank account is not approved" in result["exceptions"]


# Test 6: Multiple control failures
def test_multiple_control_failures():
    result = validate_payment(
        vendor_id="V1006",
        vendor_status="Inactive",
        payment_amount=-500,
        bank_approved=False
    )

    assert result["status"] == "REJECTED"
    assert len(result["exceptions"]) == 3

# Test 7: High-value payment without approval
def test_high_value_without_finance_approval():
    result = validate_payment(
        vendor_id="V2001",
        vendor_status="Active",
        payment_amount=15000,
        bank_approved=True,
        finance_approved=False
    )

    assert result["status"] == "REJECTED"
    assert "Finance approval required for high-value payment" in result["exceptions"]


# Test 8: High-value payment with approval
def test_high_value_with_finance_approval():
    result = validate_payment(
        vendor_id="V2002",
        vendor_status="Active",
        payment_amount=15000,
        bank_approved=True,
        finance_approved=True
    )

    assert result["status"] == "APPROVED"


# Test 9: Payment exactly at threshold
def test_payment_at_threshold():
    result = validate_payment(
        vendor_id="V2003",
        vendor_status="Active",
        payment_amount=10000,
        bank_approved=True,
        finance_approved=False
    )

    assert result["status"] == "APPROVED"
