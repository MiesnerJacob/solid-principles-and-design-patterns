from abc import ABC, abstractmethod


class TicketState(ABC):

    @abstractmethod
    def assign(self, ticket):
        pass

    @abstractmethod
    def resolve(self, ticket):
        pass

    @abstractmethod
    def close(self, ticket):
        pass


class NewState(TicketState):
    def assign(self, ticket):
        print("Assigning ticket...")
        ticket.state = AssignedState()

    def resolve(self, ticket):
        print("Cannot resolve a new ticket. It must be assigned first")

    def close(self, ticket):
        print("Closing new ticket...")
        ticket.state = ClosedState()


class AssignedState(TicketState):
    def assign(self, ticket):
        print("Ticket is already assigned.")

    def resolve(self, ticket):
        print("Resolving assigned ticket...")
        ticket.state = ResolvedState()

    def close(self, ticket):
        print("Closing assigned ticket...")
        ticket.state = ClosedState()
    

class ResolvedState(TicketState):
    def assign(self, ticket):
        print("Cannot assign a resolved ticket.")

    def resolve(self, ticket):
        print("Ticket is already resolved.")

    def close(self, ticket):
        print("Closing resolved ticket...")
        ticket.state = ClosedState()


class ClosedState(TicketState):
    def assign(self, ticket):
        print("Cannot assign a closed ticket.")

    def resolve(self, ticket):
        print("Cannot resolve a closed ticket.")

    def close(self, ticket):
        print("Ticket is already closed.")


class Ticket:

    def __init__(self):
        self.state = NewState()

    def assign(self):
        self.state.assign(self)

    def resolve(self):
        self.state.resolve(self)

    def close(self):
        self.state.close(self)

def main():
    ticket = Ticket()

    # Test the initial state and transitions
    ticket.assign()
    ticket.resolve()
    ticket.close()

    # Test invalid transitions
    ticket.assign()
    ticket.resolve()

if __name__ == "__main__":
    main()