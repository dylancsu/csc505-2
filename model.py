
class Dean:
    def __init__(self):
        self.scope = input("Enter the project scope: ")
        self.plan = input("What does the big picture view for the project look like: ")
        self.delegating = input("Explain the different components of the project: ")
        self.prototyping = input("Input the prototype status: ")
        self.integration = input("Input the integration status: ")
        self.iterative = input("Input information regarding iterative development")
    def __str__(self):
        return f"SCOPE\n{self.scope}\n\nPLAN\n{self.plan}\n\nDELEGATION\n{self.delegating}\n\nPROTOTYPING\n{self.prototyping}\n\nINTEGRATION\n{self.integration}\n\nITERATION\n{self.iterative}"

model = Dean()
print(model)