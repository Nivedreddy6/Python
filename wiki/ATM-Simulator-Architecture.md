# 🏧 ATM Simulator System Architecture

The **ATM Simulation System** (`ATM__Project.py`) is an interactive terminal application designed using Object-Oriented Programming (OOP) principles.

---

## 🏛️ Class & Data Structure Design

The core `ATM` class manages user data in an internal dictionary (`user_info`) and tracks session state.

```python
class ATM:
    def __init__(self, name, mobile, pin, balance):
        self.user_info = {
            "Name": name,
            "Mobile Number": mobile,
            "ATM PIN": pin,
            "Balance": balance,
            "Transaction History": []
        }
        self.remaining_attempts = 3
```

---

## 🔄 System State Machine & Workflow

```mermaid
graph TD
    Start([User Inserts Card / Starts]) --> ValidatePIN{Enter 4-Digit PIN}
    ValidatePIN -->|Correct PIN| MainMenu[ATM Operations Menu]
    ValidatePIN -->|Incorrect PIN| CheckAttempts{Attempts > 0?}
    CheckAttempts -->|Yes| ValidatePIN
    CheckAttempts -->|No| CardBlocked([Card Blocked / Contact Support])

    MainMenu --> Option1[1. Check Balance]
    MainMenu --> Option2[2. Cash Deposit]
    MainMenu --> Option3[3. Cash Withdrawal]
    MainMenu --> Option4[4. Mini Statement / History]
    MainMenu --> Option5[5. Change PIN]
    MainMenu --> Option6[6. Fast Cash]
    MainMenu --> Option7[7. Exit]

    Option2 --> ValidateDeposit{Amount >= 1000 & Multiples of 100?}
    ValidateDeposit -->|Yes| UpdateBalDep[Credit Balance & Log Transaction]
    ValidateDeposit -->|No| RejectDep[Show Error Message]

    Option3 --> ValidateWithdraw{Amount <= Balance & Multiples of 100?}
    ValidateWithdraw -->|Yes| UpdateBalWith[Debit Balance & Log Transaction]
    ValidateWithdraw -->|No| RejectWith[Insufficient Funds / Invalid Denomination]
```

---

## 🛡️ Business & Security Rules

1. **Lockout Mechanism**:
   - Maximum 3 PIN attempts before the account/card is blocked.
2. **Deposit Rules**:
   - Minimum single deposit threshold is ₹1,000.
   - Denominations must be multiples of 100 (`amount % 100 == 0`).
3. **Withdrawal Rules**:
   - Withdrawal amount cannot exceed available balance.
   - Amount must be in multiples of 100.
4. **Audit Trail**:
   - Every successful deposit, withdrawal, and fast cash action is appended to the `Transaction History` list for statement generation.
