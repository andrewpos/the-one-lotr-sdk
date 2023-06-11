# LOTR SDK Design Document

## Architecture

The LOTR SDK is structured around a central `LotrSDK` class, which interacts with the Lord of the Rings API. It includes a number of internal helper methods and public facing methods to fetch data from the API.

The SDK is written in Python, and makes heavy use of the `requests` library for sending HTTP requests. It also uses the `typing` module to enable static type checking, which can help catch bugs and make the code easier to understand.

The SDK also includes several custom exception classes which extend the built-in `Exception` class. These are used to provide more specific error messages in certain situations.

## Error Handling

Errors in the SDK are handled by raising exceptions. We have custom exception classes for different error scenarios, such as `InvalidMovieNameException`, `InvalidCharacterNameException`, and `APIException`.

When an error occurs, an appropriate exception is raised with a message detailing what went wrong. This makes it easy for users of the SDK to handle errors in a way that makes sense for their application.

For instance, if an API request returns a status code other than 200, an `APIException` is raised with a message indicating the status code.

## Filtering and Sorting

The SDK provides a mechanism to filter and sort the data returned from the API. For filtering, users can pass a dictionary specifying the fields to filter on and the values to filter for.

The `_create_filtering_query` method is used to create a query string from this dictionary. It uses the `_operator_to_api_format` method to convert comparison operators into a format that the API can understand.

For sorting, users can pass a dictionary specifying the fields to sort on and the direction of the sort (either ascending or descending). The `_create_sorting_query` method is used to create a query string from this dictionary.

## Code Organization

The SDK is organized into a single class `LotrSDK`, which contains methods for interacting with the API.

- The `_send_request` and `_fetch_paginated_data` methods are responsible for sending requests to the API and handling the responses.
- The `_create_sorting_query` and `_create_filtering_query` methods are used to create query strings for sorting and filtering data.
- The `_validate_movie_name`, `_validate_character_name`, and `_validate_filter` methods are used to validate input from users.
- The `get_movie`, `get_quote_by_id`, and `get_quotes` methods are the primary methods users will interact with to fetch data from the API.

## Abstraction of UIDs

We chose to abstract away the UIDs used by the API and instead allow users to interact with the SDK using movie and character names. This makes the SDK more intuitive to use, as users are more likely to know the names of movies and characters than their UIDs.

The `_get_movie_id_map` and `_get_character_id_map` methods are used to build dictionaries mapping movie and character names to their respective UIDs. These dictionaries are built when the `LotrSDK` class is instantiated.

The `_get_movie_id` and `_get_character_id` methods are used to look up the UID for a given movie or character name. These methods use the `_sanitize_name` method to normalize the names for comparison.

## String Normalization

To facilitate comparison of names, we normalize the strings by converting them to lowercase and removing spaces. This makes the SDK more forgiving of minor differences in the way names are entered.

## Overall Design Decisions

Our primary goal in designing the SDK was to make it as easy to use as possible. We made several decisions with this goal in mind:

- We chose to abstract away the details of the API, so users can fetch data with a single method call.
- We decided to allow users to interact with the SDK using movie and character names instead of UIDs. This makes the SDK more intuitive to use.
- We built in robust error handling to provide clear error messages when something goes wrong.
- We provided mechanisms for filtering and sorting data, giving users more flexibility in how they interact with the data.
