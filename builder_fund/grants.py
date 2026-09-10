if failsafe_active():
    print("Grant automation disabled under martial law.")
    return manual_grant_review()
