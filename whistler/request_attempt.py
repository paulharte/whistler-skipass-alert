import requests

""" Simple requests script. This was a fail!"""

s = requests.Session()

BASE_WEBPAGE = "https://www.whistlerblackcomb.com/plan-your-trip/lift-access/check-availability.aspx"
page = s.get(BASE_WEBPAGE)

url = "https://www.whistlerblackcomb.com/api/LiftAccessApi/GetOverAllCapacityPassReservationInventory?resortCode=80&startDate=4%2F1%2F2021&endDate=4%2F30%2F2021&_=1613745199665"
resp = s.get(url)


print(resp)
print(resp.status_code)
print(resp.content)
