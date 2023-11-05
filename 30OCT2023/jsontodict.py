dict = {

    "bookingid": 2384,

    "booking": {

        "firstname": "PRAMOD",

        "lastname": "Dutta",

        "totalprice": 432,

        "depositpaid": False,

        "bookingdates": {

            "checkin": "2022-01-01",

            "checkout": "2022-01-01"

        },

        "additionalneeds": "Lunch"

    }

}

def passDetails(dict):
    print(dict["bookingid"])
    print(dict["booking"]["bookingdates"]["checkin"])
    print(dict["booking"]["bookingdates"]["checkout"])

passDetails(dict)