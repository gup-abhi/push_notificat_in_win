# importing ToastNotifier from win10toast
from win10toast import ToastNotifier

# creating object of ToastNotifier class
toaster = ToastNotifier()

# Pushing notification
toaster.show_toast("Notification Title", "Notification Body here", duration = 10, threaded = False)
# Pushing another notification
toaster.show_toast("BBC News", "News on Covid-19", duration = 10, threaded = False)