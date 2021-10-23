# Αυτό το πρόγραμμα υπολογίζει με δύο τρόπους το πλήθός των δευτερολέπτων
# κάποιας χρονικής διάρκειας

#Μεταβλητές
seconds = 15
minutes = 50
hours = 10

# Πρώτος υπολογισμός
total_time = hours*3600 + minutes*60 + seconds

print(total_time)

# Δεύτερος υπολογισμός

total_time = seconds
total_time +=minutes*60
total_time +=hours*3600

print(total_time)