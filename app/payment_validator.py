
def validate_payment(
    vendor_id,
    vendor_status,
    payment_amount,
    bank_approved,
    finance_approved=False
):
    """
    Simulated automated application control.

    AP-001: Basic vendor payment validation.
    AP-002: High-value payment approval.
    """

    exceptions = []

    # AP-001A: Vendor must be active
    if vendor_status != "Active":
        exceptions.append("Vendor is not active")

    # AP-001B: Payment amount must be positive
    if payment_amount <= 0:
        exceptions.append("Payment amount must be greater than zero")

    # AP-001C: Bank account must be approved
    if bank_approved is not True:
        exceptions.append("Vendor bank account is not approved")

    # AP-002: High-value payment requires Finance approval
    if payment_amount > 10000 and finance_approved is not True:
        exceptions.append("Finance approval required for high-value payment")

    if exceptions:
        return {
            "vendor_id": vendor_id,
            "status": "REJECTED",
            "exceptions": exceptions
        }

    return {
        "vendor_id": vendor_id,
        "status": "APPROVED",
        "exceptions": []
    }


if __name__ == "__main__":
    payment = validate_payment(
        vendor_id="V1001",
        vendor_status="Active",
        payment_amount=15000,
        bank_approved=True,
        finance_approved=False
    )

    print(payment)
