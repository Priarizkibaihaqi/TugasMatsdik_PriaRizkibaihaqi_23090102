class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)


class OrganizationTree:
    def __init__(self):
        self.ceo = None

    def hire_ceo(self, name, position):
        self.ceo = Employee(name, position)

    def add_employee(self, manager_name, name, position):
        new_employee = Employee(name, position)
        manager = self._find_employee(manager_name, self.ceo)
        if manager:
            manager.add_subordinate(new_employee)
        else:
            print(f"Manager '{manager_name}' not found.")

    def _find_employee(self, name, node):
        if not node:
            return None
        if node.name == name:
            return node
        for subordinate in node.subordinates:
            found_employee = self._find_employee(name, subordinate)
            if found_employee:
                return found_employee
        return None

    def display_organization(self):
        if not self.ceo:
            print("No CEO hired yet.")
            return
        self._display_employee(self.ceo, 0)

    def _display_employee(self, employee, level):
        print("  " * level + f"{employee.name} - {employee.position}")
        for subordinate in employee.subordinates:
            self._display_employee(subordinate, level + 1)


# Example usage:
if __name__ == "__main__":
    organization = OrganizationTree()

    # Hire CEO
    organization.hire_ceo("John Doe", "CEO")

    # Add employees
    organization.add_employee("John Doe", "Jane Smith", "COO")
    organization.add_employee("Jane Smith", "Michael Johnson", "Manager")
    organization.add_employee("Jane Smith", "Emily Davis", "Manager")
    organization.add_employee("Michael Johnson", "Peter Brown", "Staff")
    organization.add_employee("Emily Davis", "Sarah Wilson", "Staff")

    # Display organization structure
    print("Organization Structure:")
    organization.display_organization()
