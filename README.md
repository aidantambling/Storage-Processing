# In-Memory Database with Transaction Support (Data Processing and Storage Extra Credit Assignment)

## Overview
The database is implemented in Python. It is a key-value database centered on transaction support. The primary functions are:
- **get(key)**: Retrieve the value of a key (excludes current transaction).
- **put(key, value)**: Insert a key / update the value of a key (transaction must be active).
- **begin_transaction()**: Start a new transaction.
- **commit()**: Commit the current transaction (all changes will be applied to the database).
- **rollback()**: Rollback the current transaction (all changes will be discarded, database will be unchanged).

## How to Run

### Prerequisites
- Python 3.7 or higher.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/aidantambling/Storage-Processing.git
   cd Storage-Processing
   ```
2. Run the script
   ```bash
   python inmemory_db.py
   ```
3. Test the code
   There is a sample test case used in the main function of inmemory_db.py:
   ```bash
    db = InMemoryDB()

    print(db.get("A"))  # None

    try:
        db.put("A", 5)  # Error
    except TransactionError as e:
        print(e)

    db.begin_transaction()
    db.put("A", 5)
    print(db.get("A"))  # None

    db.put("A", 6)
    db.commit()
    print(db.get("A"))  # 6

    try:
        db.commit()  # Error
    except TransactionError as e:
        print(e)
 
    try:
        db.rollback()  # Error
    except TransactionError as e:
        print(e)

    print(db.get("B")); # Null

    db.begin_transaction()
    db.put("B", 10);
    db.rollback()
    print(db.get("B")) # Null
    ```

## Assignment Reflection
I found this assignment to be very enjoyable and think it would be great as an official assignment for the course: it is simple yet informative enough to introduce students to basic database principles. One simple modification could be a delete() function to remove entries from the database. A more advanced modification might be expanding value support from just integers to all sorts of values (e.g. strings, decimals, ints, etc.) and introducing some sort of type specifications, to add more considerations for the student. For grading, one way to simplify the assignment might be more strict requirements (e.g., you must implement in C++, and the class must be named X, etc.) - then, tests could be written, which might expedite the grading process and also allow students to familiarize themselves with testing situations. At the same time, this does restrict freedom of implementation, which might introduce some downsides. 

