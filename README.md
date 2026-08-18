# POSFree
A Free POS App for businesses
<h2>Abstract </h2>
Businesses need a way to keep track of inventory and transactions in an efficient and timely manner. The use of manual tally marking with paper takes too long and is not organized enough to keep track of transactions and inventory.
<h2>Goals</h2>
<ul>
  <li>Have a easy to access POS with inventory tracking and transactions</li>
</ul>
<h2>Features</h2>
<ul>
  <li>Home page with login or create new owner or employee account (both can be added to more than one shop </li>
  <li>Create a new shop that has owners add at least one item type and employee (could be just themself) as well as name of shop and type of shop before shop is officially made </li>
  <li>Transactions(history,add/remove)</li>
  <li>Inventory(history,add/remove stock and item types)</li>
  <li>Calendar with Daily,Weekly,Monthly,Quarterly, and Annually reports on inventory and transactions</li>
  <li>A reminders notification system for transactions needed to be made and what items need to be restocked
</li>
</ul>
<h2>WireFrame</h2>
<ol>
  <li>Home Page: With POSFree (title)  on top with Free POS for Businesses (smaller than title)  below it, space in between will be the following buttons: owner login, employee login, new owner, new employee</li>
  <li>Owner Login Page: Asks for Email,Password, and special owner code with a forgot password button below the login info</li>
  <li>Employee Login Page: Asks for Email and password  with a forgot password button below the login info
</li>
<li>Forgot password page: asks for email to then send reset password link
</li>
<li>Reset password page: reset password then go back to login page
</li>
<li>New Owner Page: Asks for name, email, password, and if they are the owner of a new shop or current shop</li>
<li>New Employee Page: Asks for name, email, password, and shop join pin</li>
<li>Shops Page: shows all the shops that the person is involved with (include edit shops button to remove/add shops)
</li>
<li>Individual Shop</li>
<ol> 
  <li> Main page: has shop's title on top, with buttons below it to inventory, calendar, staff, and transactions 
</li>
  <li>Inventory: shows stock of each type of item, with a edit inventory button to add/remove stock and item types </li>
  <li>Transactions: shows transaction history of shop with a edit transactions button to add/remove transactions</li>
  <li>staff (for owners only): shows all staff members with a edit staff button to add/remove staff 
</li>
  <li>Calendar: shows the calendar for the current month with buttons to daily,weekly,monthly,quarterly,and annually reports 
</li> 
  <ul>
    <li>Report page: shows transactions,inventory, and loss/gain made during the time period on a google sheet like format with the ability to print and shared 
</li>
  </ul>
</ol>
<li>New Shop: asks for shop name, shop type, and items that will be sold (with prices and current stock) and employees.
</li>
  
</ol>

<h2>User Workflow</h2>

### Owner Workflow

1. **Registration & Login**
   - Click "New Owner" on the home page
   - Enter name, email, and password
   - Choose to create a new shop or join an existing one
   - Log in with email and password

2. **Create a New Shop**
   - Navigate to "New Shop" after login
   - Enter shop name, shop type, and business category
   - Add at least one item type with pricing and initial stock
   - Add at least one employee (can be yourself)
   - Confirm shop creation

3. **Manage Inventory**
   - Go to the shop's main page and select "Inventory"
   - View current stock levels for all items
   - Click "Edit Inventory" to:
     - Add new item types with prices
     - Update stock quantities
     - Remove items from inventory
   - Track inventory history for auditing

4. **Process Transactions**
   - Select "Transactions" from the shop dashboard
   - View complete transaction history
   - Click "Add Transaction" to process sales
   - Edit or remove transactions as needed
   - Track transaction records by date and employee

5. **Manage Staff**
   - Select "Staff" from the shop dashboard (owners only)
   - View all employees associated with the shop
   - Click "Edit Staff" to:
     - Add new employees (provide them with shop join PIN)
     - Remove employees from the shop
     - Update employee roles and permissions

6. **Generate Reports**
   - Navigate to "Calendar" section
   - Select desired reporting period:
     - Daily reports
     - Weekly reports
     - Monthly reports
     - Quarterly reports
     - Annually reports
   - View transaction totals, inventory changes, and profit/loss
   - Print or share reports with team members

### Employee Workflow

1. **Registration & Login**
   - Click "New Employee" on the home page
   - Enter name, email, and password
   - Provide the shop join PIN (provided by shop owner)
   - Log in with email and password

2. **Access Your Shop(s)**
   - View all shops you are assigned to
   - Select a shop to access its dashboard

3. **Process Transactions**
   - Select "Transactions" from the shop dashboard
   - View transaction history
   - Add new transactions when processing sales
   - Cannot edit or remove transactions (owner permission required)

4. **View Inventory**
   - Select "Inventory" from the shop dashboard
   - View current stock levels
   - Cannot make changes to inventory (owner permission required)
   - Use this for reference when assisting customers

5. **Check Notifications**
   - Receive reminders for:
     - Pending transactions that need to be recorded
     - Items that need to be restocked
     - Other shop-related alerts

