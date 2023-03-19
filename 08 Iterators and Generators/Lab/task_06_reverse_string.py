def reverse_text(text: str):
    text_as_list = list(text)

    while text_as_list:
        yield text_as_list.pop()


# def reverse_text(text: str):
#     index = len(text) - 1
#
#     while index >= 0:
#         yield text[index]
#         index -= 1


for char in reverse_text("step"):
    print(char, end='')
