import re


class PhoneNumber:
    def __init__(self, number):

        numbers_only = re.sub("[^0-9]", "", number)
        num_no_intl_prefix = re.sub("^(00)*1", "", numbers_only)

        if len(num_no_intl_prefix) != 10:
            raise ValueError("Number {} does not have 10 digits to satisfy NANP".format(number))

        self.number = num_no_intl_prefix

        m = re.match("^([0-9]{3})(([0-9]{3})([0-9]{4}))$", num_no_intl_prefix)

        self.area_code = m[1]
        self.local_number = m[2]
        self.exchange_code = m[3]
        self.subscriber_number = m[4]

        if re.match("^[01]", self.area_code):
            raise ValueError("Area Code {} Cannot start with 0 or 1 to satisfy NANP".format(self.area_code))

        if re.match("^[01]", self.exchange_code):
            raise ValueError("Exchange Code {} Cannot start with 0 or 1 to satisfy NANP".format(self.exchange_code))

    def pretty(self):
        return "({})-{}-{}".format(self.area_code, self.exchange_code, self.subscriber_number)