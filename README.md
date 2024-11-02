# ☕ Coffee Machine Project ☕

This Coffee Machine program simulates a vending machine that serves three types of coffee: **Espresso**, **Latte**, and **Cappuccino**. Users can select a drink, insert coins, and the machine will deduct the resources used to make the coffee.

## 📋 Table of Contents
- [Features](#features)
- [Menu](#menu)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Code Structure](#code-structure)
- [Example Usage](#example-usage)

## ✨ Features

- Three types of coffee: **Espresso**, **Latte**, and **Cappuccino**
- Resource management with ingredient tracking
- Coin-based payment processing
- Reports current resource status
- Tracks profit from drink sales

## ☕ Menu

| Drink      | Ingredients                            | Cost  |
|------------|----------------------------------------|-------|
| Espresso   | Water: 50ml, Coffee: 18g               | $1.50 |
| Latte      | Water: 200ml, Milk: 150ml, Coffee: 24g | $2.50 |
| Cappuccino | Water: 250ml, Milk: 100ml, Coffee: 24g | $3.00 |

## ⚙️ How It Works

1. **User Prompt**: The user selects a coffee type or enters `"report"` to view resources or `"off"` to turn off the machine.
2. **Resource Check**: The machine verifies it has sufficient resources for the drink.
3. **Payment Processing**: The user inserts coins, and the machine calculates if the amount is enough.
4. **Transaction Success**: If the payment is sufficient, the machine makes the coffee and deducts resources. Any extra amount is returned as change.

## 🧩 Code Structure

- **MENU**: Contains drink details including ingredients and costs.
- **resource**: Tracks current levels of water, milk, and coffee.
- **Functions**:
  - `isResourceSufficient()`: Checks if there are enough ingredients.
  - `processCoins()`: Collects and calculates total money inserted by the user.
  - `isTransactionSuccessful()`: Verifies payment and calculates change if necessary.
  - `makeCoffee()`: Prepares the coffee by deducting resources.

## 🛠️ Requirements

- **Python 3.x** is required to run the program.

## 🖥️ Example Usage

1. Run the program in a Python environment.
2. Follow the prompt:
   - Enter the coffee type (e.g., `espresso`, `latte`, `cappuccino`).
   - Enter `report` to see current resources.
   - Enter `off` to turn off the machine.

### Sample Output

```plaintext
What would you like? (espresso, latte, cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 5
How many nickles?: 0
How many pennies?: 4
Here is your latte 🍵
```
