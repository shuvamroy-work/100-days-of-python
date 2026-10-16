
"""
Day 03: Movie Ticket Price & Discount Calculator
Topic: Conditionals (if, elif, else) & Logical Operators (and, or, not)
Author: [Your Name]
"""


def calculate_ticket_price(age: int, is_student: bool, day: str) -> float:
    """Calculate the final ticket price based on age, student status, and day."""
    # Base price based on age tier
    if age < 5:
        base_price = 0.0
    elif age <= 18:
        base_price = 150.0
    elif age < 60:
        base_price = 250.0
    else:
        base_price = 180.0  # Senior citizen

    # Apply discounts if ticket is not already free
    if base_price > 0:
        # 20% discount for students OR on Tuesdays
        if is_student or day.strip().lower() == "tuesday":
            discount = base_price * 0.20
            return base_price - discount

    return base_price


def main():
    print("=" * 40)
    print("      CINEMA TICKET PRICING SYSTEM      ")
    print("=" * 40)

    try:
        age = int(input("Enter your age: ").strip())
        student_input = input("Are you a student? (yes/no): ").strip().lower()
        day = input("Enter day of the week (e.g., Monday, Tuesday): ").strip()

        is_student = student_input in ["yes", "y"]

        final_price = calculate_ticket_price(age, is_student, day)

        print("-" * 40)
        if final_price == 0:
            print("Status: Ticket is FREE for kids under 5!")
        else:
            print(f"Final Payable Amount: ₹{final_price:.2f} INR")
        print("-" * 40)

    except ValueError:
        print("\n[Error]: Please enter a valid integer for age.")


if __name__ == "__main__":
    main()