def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount.
    Otherwise, return the original price.

    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount.
    """
    # Ensure discount percentage is valid
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")

    # Apply discount if it's 20% or higher
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price


def main():
    """
    Main function to prompt the user for input and calculate the discounted price.
    """
    try:
        # Get user input
        original_price = float(input("Enter the original price of the item: "))
        discount_percentage = float(input("Enter the discount percentage: "))

        # Validate price
        if original_price < 0:
            print("Price cannot be negative. Please enter a valid price.")
            return

        # Calculate and display the final price
        final_price = calculate_discount(original_price, discount_percentage)
        if final_price != original_price:
            print(f"The final price after applying a {discount_percentage}% discount is: {final_price:.2f}")
        else:
            print("The discount is less than 20%, so no discount was applied.")
            print(f"The original price remains: {original_price:.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}. Please enter valid numerical values for the price and discount.")


# Run the program
if __name__ == "__main__":
    main()