from lotr_sdk import LotrSDK
import os
from dotenv import load_dotenv

load_dotenv()

sdk = LotrSDK(os.getenv("LOTR_API_KEY"))

# # get all Gimli's quotes from The Return of the King and The Two Towers
# quotes = sdk.get_quotes(movies=["The Return of the King", "The Two Towers"], characters=["Gimli"])

# # Print out the quotes
# for quote in quotes:
#     print(f'"{quote.dialog}" - Gimli')


# quotes = sdk.get_quotes(movies=["The Fellowship of the Ring"], characters=['Gimli'], sort={'character': 'asc'}, limit=1000)
filter = {"dialog": {"operator": "eq", "value": "Aragorn is right. We cannot use it."}}
# mov_filter = {}

quotes = sdk.get_quotes(
    movies=["The Fellowship of the Ring", "The Return of the king"], 
    characters=["Gandalf", "Gimli"],
    sort={"dialog": "asc"},  # Sorting the quotes in ascending order based on dialog
    # filter=filter,  # Filtering quotes to only include those which have 'ring' in dialog
    limit=1000
)
for quote in quotes:
    print(f'Quote: {quote.dialog}\nMovie: {quote.movie}\nCharacter: {quote.character}\n{"-"*50}\n')

# # Print out the quotes
# for quote in quotes:
#     print(f'"{quote.dialog}" - {quote.character} ({quote.movie})')
