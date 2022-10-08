# AM to 24HRS - subtract 12 from 12 AM and remove 'AM' from any other AM time
# PM to 24HRS - add 12 to all times other than 12PM, remove 'PM' from 12:00 PM
def am_to_24(time: str):
    time_format = time[-2:]
    if (time[:2]) == "12":
        return time.replace(time[:2], "00").replace(time_format, "")
    else:
        return time.replace(time_format, "")


def pm_to_24(time: str):
    time_format = time[-2:]
    if (time[:2]) == "12":
        return time.replace(time_format, "")
    else:
        return time.replace(time[:2], "{0}".format(str(int(time[:2]) + 12))).replace(time_format, "")


def time_conversion(s):
    time_format = s[-2:]
    if time_format == "AM":
        return am_to_24(s)
    else:
        return pm_to_24(s)


if __name__ == '__main__':
    s = input()

    print(time_conversion(s))
