class TransactionError(Exception):
    pass

class InMemoryDB:
    def __init__(self):
        self.data = {}  # permanent data storage (global)
        self.transaction_data = None  # transaction data storage

    def get(self, key):
        # we ignore any current transaction ("new" values are not visible until committed)
        return self.data.get(key, None) # otherwise check the persistent data

    def put(self, key, val):
        if self.transaction_data is None:
            raise TransactionError("Cannot perform put operation (no active transaction).")
        self.transaction_data[key] = val # create new key (or, if it exists, update its value)

    def begin_transaction(self):
        if self.transaction_data is not None:
            raise TransactionError("Transaction already in progress - cannot start new one.")
        self.transaction_data = {} # make transaction_data a list to indicate the transaction is active

    def commit(self):
        if self.transaction_data is None:
            raise TransactionError("Cannot commit - no active transaction")

        for key, val in self.transaction_data.items():
            self.data[key] = val # assign all the transaction entries to permanent data storage (they will now be visible to get())
        self.transaction_data = None # reset transaction_data to indicate the transaction as completed (end transaction)

    def rollback(self):
        if self.transaction_data is None:
            raise TransactionError("Cannot rollback - no active transaction")
        self.transaction_data = None # reset the transaction_data (any changes will be erased)(end transaction)


# sample implementation from instructions
if __name__ == "__main__":
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