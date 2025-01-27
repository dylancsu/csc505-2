
class Dean:
    def __init__(self):
        self.scope = input("Enter the project scope: ")
        self.plan = input("What does the big picture view for the project look like: ")
        self.delegating = input("Explain the different components of the project: ")
        self.prototyping = input("Input the prototype status: ")
        self.integration = input("Input the integration status: ")
        self.iterative = input("Input information regarding iterative development: ")
    def __str__(self):
        return f"SCOPE\n{self.scope}\n\nPLAN\n{self.plan}\n\nDELEGATION\n{self.delegating}\n\nPROTOTYPING\n{self.prototyping}\n\nINTEGRATION\n{self.integration}\n\nITERATION\n{self.iterative}"
    def update(self):
        match input("Enter the field you would like to update: ").lower():
            case "scope":
                self.scope = input("Enter the new project scope: ")
            case "plan":
                self.plan = input("Enter the updated big picture view for the project: ")
            case "delegating":
                self.delegating = input("Explain the updated components of the project: ")
            case "prototyping":
                self.prototyping = input("Input the updated prototype status: ")
            case "integration":
                self.integration = input("Input the updated integration status: ")
            case "iteration":
                self.iterative = input("Input updated information regarding iterative development: ")
            case _:
                print("Invalid field. Please enter one of: scope, plan, delegating, prototyping, integration, iteration.")

            
model = Dean()
print(model)
model.update()
model.update()
print(model)