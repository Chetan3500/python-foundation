"""Book Price Analyzer"""

from module.book_price_analyzer import read_books, calculate_stats, write_expensive_books

def main() -> None:
    """Execute main program"""
    input_file: str = "books.txt"
    output_file: str = "expensive_books.txt"
    books: list[tuple[str, float]] = read_books(input_file)

    if books:
        total, avg = calculate_stats(books)
        print("Book Price Summary:")
        print(f"Total Price: ${total:.2f}")
        print(f"Average Price: ${avg:.2f}")
        write_expensive_books(books, output_file)
    else:
        print("No valid book data to process.")


if __name__ == "__main__":
    main()
