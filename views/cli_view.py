class CLIView:
    def __init__(self):
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def run(self):
        email = input("Enter your email: ")
        self.controller.save(email)

    def print_error(self, message):
        print(message)
        self.run()

    def print_success(self, message):
        print(message)
