class TimeConverter:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def convert_to_words(self):
        nums = [
            "zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen",
            "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen",
            "twenty", "twenty one", "twenty two",
            "twenty three", "twenty four",
            "twenty five", "twenty six", "twenty seven",
            "twenty eight", "twenty nine"
        ]

        if self.minute == 0:
            return f"{nums[self.hour]} o' clock"
        elif self.minute == 1:
            return f"one minute past {nums[self.hour]}"
        elif self.minute == 59:
            return f"one minute to {nums[(self.hour % 12) + 1]}"
        elif self.minute == 15:
            return f"quarter past {nums[self.hour]}"
        elif self.minute == 30:
            return f"half past {nums[self.hour]}"
        elif self.minute == 45:
            return f"quarter to {nums[(self.hour % 12) + 1]}"
        elif self.minute <= 30:
            return f"{nums[self.minute]} minutes past {nums[self.hour]}"
        elif self.minute > 30:
            return f"{nums[60 - self.minute]} minutes to {nums[(self.hour % 12) + 1]}"

while True:
    try:
        h = int(input("Enter the hour (0-23): "))
        m = int(input("Enter the minute (0-59): "))
        
        if 0 <= h <= 23 and 0 <= m <= 59:
            time_converter = TimeConverter(h, m)
            result = time_converter.convert_to_words()
            print(result)
        else:
            print("Invalid input. Please enter a valid hour (0-23) and minute (0-59).")
    except ValueError:
        print("Invalid input. Please enter numeric values for hour and minute.")