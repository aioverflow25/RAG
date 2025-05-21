from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text = '''
def sum_natural_numbers(n):
    """Returns the sum of the first n natural numbers."""
    return n * (n + 1) // 2

def sum_squares_natural_numbers(n):
    """Returns the sum of the squares of the first n natural numbers."""
    return n * (n + 1) * (2 * n + 1) // 6

# Example usage:
n = 5
print("Sum of first", n, "natural numbers:", sum_natural_numbers(n))
print("Sum of squares of first", n, "natural numbers:", sum_squares_natural_numbers(n))

'''

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0,
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[1])