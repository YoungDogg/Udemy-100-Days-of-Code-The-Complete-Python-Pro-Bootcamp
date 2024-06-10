# Application Flow

This document outlines the flow of the Coffee Machine Project, detailing the steps the application takes from start to finish.

## Flow Overview

1. **Start Machine**
    - The application starts and continuously prompts the user for input.

2. **Prompt User for Drink Selection**
    - The user is asked: "What would you like? (espresso/latte/cappuccino):"

3. **Process User Input**
    - **Turn Off Machine**: If the user inputs "off", the machine stops running.
    - **Print Report**: If the user inputs "report", the machine prints the current resources and money collected.
    - **Make Drink**: If the user inputs a valid drink name, the machine proceeds to check resources and process the order.

4. **Check Resources**
    - The machine checks if there are enough ingredients to make the selected drink.
    - If there are not enough resources, the machine notifies the user and returns to the prompt.

5. **Process Coins**
    - If resources are sufficient, the machine prompts the user to insert coins.
    - The user inserts coins, and the machine calculates the total amount.

6. **Check Transaction**
    - The machine checks if the inserted money is enough for the selected drink.
    - **Sufficient Money**: If enough money is inserted, the machine makes the drink, updates the resources, and provides change if applicable.
    - **Insufficient Money**: If not enough money is inserted, the machine refunds the money and returns to the prompt.

7. **Make Coffee**
    - The machine deducts the required ingredients from the resources.
    - The machine dispenses the drink and notifies the user: "Here is your [drink_name]. Enjoy!"

8. **Repeat or Exit**
    - The process repeats until the machine is turned off by entering "off".

## Detailed Steps

### 1. Start Machine
- The machine initializes and enters a loop, waiting for user input.

### 2. Prompt User for Drink Selection
- The user is presented with options to select a drink, request a report, or turn off the machine.

### 3. Process User Input
- If the input is "off", the machine stops.
- If the input is "report", the machine prints the current status of resources and money.
- If the input is a drink name (espresso, latte, cappuccino), the machine proceeds to check resources.

### 4. Check Resources
- The machine compares the required ingredients for the selected drink with the available resources.
- If any ingredient is insufficient, a message is displayed, and the user is prompted again.
~~~~~~~~
### 5. Process Coins
- If resources are sufficient, the machine asks the user to insert coins.
- The total value of the inserted coins is calculated.

### 6. Check Transaction
- The machine checks if the inserted money meets or exceeds the cost of the selected drink.
- If enough money is inserted, the machine proceeds to make the drink.
- If not enough money is inserted, the machine refunds the money and prompts the user again.

### 7. Make Coffee
- The required ingredients are deducted from the resources.
- The machine dispenses the drink and informs the user.

### 8. Repeat or Exit
- The process continues, allowing the user to make more selections until the machine is turned off.

### Flow Diagram (Optional)

```plaintext
+-------------------+
| Start Machine     |
+-------------------+
         |
         v
+-------------------------+
| Prompt for Drink Choice |
+-------------------------+
         |
         v
+---------------------+      +--------------------+       +------------------+
| User Enters Choice  |----->| Check for "off"    |------>| Turn Off Machine |
+---------------------+      +--------------------+       +------------------+
         |                                 |
         v                                 |
+--------------------+                     |
| Check for "report" |---------------------+
+--------------------+                     |
         |                                 |
         v                                 |
+-----------------------+                  |
| Print Resource Report |<-----------------+
+-----------------------+
         |
         v
+---------------------+
| Check Resources     |
+---------------------+
         |
         v
+------------------------+
| Resources Sufficient?  |
+------------------------+
         |                
         v                
+-------------------------+     +-----------------------------+
| Notify Insufficient     |---->| Go back to prompt for Drink |
| Resources               |     +-----------------------------+
+-------------------------+
         |
         v
+-------------------------+
| Process Coins           |
+-------------------------+
         |
         v
+----------------------------+      +-------------------------------+
| Check Transaction          |----->| Sufficient Money?             |
+----------------------------+      +-------------------------------+
         |                                    |
         v                                    |
+-----------------------------+               |
| Notify Insufficient Money   |<--------------+
| and Refund                  |
+-----------------------------+
         |
         v
+-------------------------+
| Make Coffee             |
+-------------------------+
         |
         v
+-------------------------+
| Notify User             |
| "Here is your [drink]"  |
+-------------------------+
         |
         v
+-------------------------+
| Repeat or Exit          |
+-------------------------+
