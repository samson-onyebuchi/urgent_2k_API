import datetime
from app.service import users_collection
def lock_account(attempts, time_range):
  # Check if the number of attempts is greater than three
    if attempts > 3:
    # Calculate the current time
        current_time = datetime.datetime.now()

    # Calculate the time that the account should be locked until
        lock_time = current_time + datetime.timedelta(minutes=time_range)

    # Lock the account by setting the lock time and returning True
        users_collection.lock_time = lock_time
        return True
    else:
    # Return False if the number of attempts is not greater than three
        return False