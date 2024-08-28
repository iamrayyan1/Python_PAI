def url():
    url = input("Enter a URL starting with 'http://www.': ")

    if url.startswith("http://www."):
        # Removing the 'http://www.' part from the URL
        main_part = url[len("http://www."):]

        new_url = f"{main_part}.com"
        return new_url
    else:
        return "The URL must start with 'http://www.'."

# Example usage
print(url())
