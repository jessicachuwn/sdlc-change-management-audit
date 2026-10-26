
def validate_payment(vendor_id, vendor_status, payment_amount, bank_approved):
    """
    Simulated automated application control AP-001.

    Validate a vendor payment against three business rules.
    Returns a decision and the reasons for rejection.
    """

    exceptions = []

    # Control AP-001A: Vendor must be active
    if vendor_status != "Active":
        exceptions.append("Vendor is not active")

    # Control AP-001B: Payment amount must be positive
    if payment_amount <= 0:
        exceptions.append("Payment amount must be greater than zero")

    # Control AP-001C: Bank account must be approved
    if bank_approved is not True:
        exceptions.append("Vendor bank account is not approved")

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


# Simulated payment request
payment = validate_payment(
    vendor_id="V1001",
    vendor_status="Active",
    payment_amount=5000,
    bank_approved=False
)

print(payment)
