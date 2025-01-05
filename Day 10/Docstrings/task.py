def format_name(f_name, l_name):
    """ Returns concatenated name and last name in title case."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)

def squared(a):
    """ Returns the square of a number."""

    return a * a


print(squared(10))

