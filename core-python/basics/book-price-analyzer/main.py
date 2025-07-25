"""Book Price Analyzer"""


def read_books(file_path: str) -> list[tuple[str, float]]:
    """Open a text file and returns a list of (title, price) tuple"""

    books: list[tuple[str, float]] = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Each line: "title,price"
                parts = line.strip().split(",")
                if len(parts) != 2:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue
                try:
                    title, price_str = parts
                    price: float = float(price_str)
                    books.append((title, price))
                except ValueError:
                    print(f"Error: Invalid price format on title: '{parts[0]}'.")
        return books
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return []


def calculate_stats(books: list[tuple[str, float]]) -> tuple[float, float]:
    """Return total and avg price from a list of books"""
    if not books:
        return 0.0, 0.0
    prices = [price for _, price in books]
    total = sum(prices)
    avg = total / len(prices)
    return total, avg


def write_expensive_books(
    books: list[tuple[str, float]], output_file: str, threshold: float = 20.0
) -> None:
    """Save titles and price of expensive books"""

    try:
        with open(output_file, "w", encoding="utf-8") as file:
            for title, price in books:
                if price >= threshold:
                    file.write(f"{title}: ${price:.2f}\n")
        print(f"Expensive books written to {output_file}")
    except IOError as e:
        print(f"Error writing to {output_file}: {e}")


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
