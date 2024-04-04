class Movie:
    def __init__(self, name, showtime, available_seats):
        self.name = name
        self.showtime = showtime
        self.available_seats = available_seats

class Ticket:
    def __init__(self, movie_name, seat_number, price):
        self.movie_name = movie_name
        self.seat_number = seat_number
        self.price = price

class BookingSystem:
    def __init__(self):
        self.movie_database = []
        self.booked_tickets = []

    def add_movie(self, name, showtime, available_seats):
        movie = Movie(name, showtime, available_seats)
        self.movie_database.append(movie)

    def display_movies(self):
        print("Available Movies:")
        for i, movie in enumerate(self.movie_database):
            print(f"{i + 1}. {movie.name} ({movie.showtime})")

    def book_ticket(self, movie_index, seat_number):
        selected_movie = self.movie_database[movie_index]
        if selected_movie.available_seats > 0:
            ticket_price = 200.0  
            ticket = Ticket(selected_movie.name, seat_number, ticket_price)
            self.booked_tickets.append(ticket)
            selected_movie.available_seats -= 1
            print("Ticket booked successfully!")
        else:
            print("Sorry, no available seats for this movie.")

    def display_booked_tickets(self):
        print("Booked Tickets:")
        for ticket in self.booked_tickets:
            print(f"Movie: {ticket.movie_name}, Seat: {ticket.seat_number}, Price: INR{ticket.price:.2f}")

if __name__ == "__main__":
    booking_system = BookingSystem()

    # Add sample movies to the database
    booking_system.add_movie("Movie 1", "10:00 AM", 50)
    booking_system.add_movie("Movie 2", "2:30 PM", 60)
    booking_system.add_movie("Movie 3", "7:00 PM", 70)

    while True:
        print("\n1. Display Movies")
        print("2. Book a Ticket")
        print("3. Display Booked Tickets")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            booking_system.display_movies()
        elif choice == 2:
            booking_system.display_movies()
            movie_index = int(input("Select a movie (Enter the number): ")) - 1
            seat_number = int(input("Enter seat number: "))
            booking_system.book_ticket(movie_index, seat_number)
        elif choice == 3:
            booking_system.display_booked_tickets()
        elif choice == 4:
            print("Thank you for using our system!")
            break
        else:
            print("Invalid choice. Please try again.")