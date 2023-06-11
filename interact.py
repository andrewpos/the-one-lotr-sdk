from lotr_sdk import LotrSDK
import os
from dotenv import load_dotenv

load_dotenv()

sdk = LotrSDK(os.getenv("LOTR_API_KEY"))

filter = {"dialog": {"operator": "eq", "value": "Hobbits!"}}

quotes = sdk.get_quotes(
    movies=["The Fellowship of the Ring", "The Return of the king"], 
    characters=["Gandalf", "Gimli"],
    sort={"dialog": "asc"},  # Sorting the quotes in ascending order based on dialog
    filter=filter,  # Filtering quotes to only include those which have 'ring' in dialog
    limit=1000
)
for quote in quotes:
    print(f'Quote: {quote.dialog}\nMovie: {quote.movie}\nCharacter: {quote.character}\n{"-"*50}\n')
