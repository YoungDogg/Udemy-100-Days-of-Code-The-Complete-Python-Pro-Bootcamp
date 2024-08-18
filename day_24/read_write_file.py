# # Reading from a file
# with open('workfile', 'r') as f:
#     content = f.read()
#
# # Providing feedback on the contents
# print("Current file contents:")
# print(content)

# Let's modify the content and write it back
# new_content = content + "\nAdding some more content for practice."
new_content = "\nAdding some more content for practice."

# Writing back to the file
with open('workfile', 'w') as f:
    f.write(new_content)

# Reading again to verify the changes
with open('workfile', 'r') as f:
    updated_content = f.read()

print('\nUpdated file contents:')
print(updated_content)

appended_content = "\n Appended content"
with open('workfile', 'r+') as f:
    f.write(appended_content)
    read_content = f.read()
# with open('workfile', 'r') as f:
#     read_content = f.read()

print('\nAppend file contents:')
print(read_content)
