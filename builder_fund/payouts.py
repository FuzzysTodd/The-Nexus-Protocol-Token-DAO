
from failsafe import failsafe_active
if failsafe_active():
    raise SystemExit("Builder Fund payouts disabled under martial law.")
