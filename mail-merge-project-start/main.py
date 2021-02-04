content = '';
with open("Input/Letters/starting_letter.txt", mode="r") as context:
  content = context.read();
  print(content)

with open("Input/Names/invited_names.txt", mode="r") as letters:
  names = letters.readlines()
  crctNames = []
  for name in names:
    correct = name.replace("\n", " ");
    crctNames.append(correct)
  
  print(crctNames)
  for name in crctNames:
    namedContent = content.replace("[name],", f"{name},")
    with open(f"./Output/ReadyToSend/{name}letter.txt", mode="w") as namingContent:
      namingContent.write(namedContent);