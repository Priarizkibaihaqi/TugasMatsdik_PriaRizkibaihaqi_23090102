class PhoneNumberValidator:
    def __init__(self):
        self.states = ['start', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'accept']
        self.current_state = 'start'
    
    def validate(self, phone_number):
        for digit in phone_number:
            if digit not in '0123456789':
                return False
            self.current_state = self.transition(self.current_state, digit)
        
        return self.current_state == 'accept'
    
    def transition(self, state, digit):
        if state == 'start':
            if digit == '0':
                return 'q2'
            else:
                return 'q1'
        elif state.startswith('q'):
            next_digit = int(state[1]) + 1
            if next_digit <= 9:
                return 'q' + str(next_digit)
            else:
                return 'accept'
        else:
            return 'reject'


# Example usage:
if __name__ == "__main__":
    validator = PhoneNumberValidator()

    # Test valid phone numbers
    print(validator.validate("1234567890"))  # True
    print(validator.validate("0987654321"))  # True

    # Test invalid phone numbers
    print(validator.validate("123"))         # False
    print(validator.validate("abcdefghij"))  # False
    print(validator.validate("12345abcde"))  # False
