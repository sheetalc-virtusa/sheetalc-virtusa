import re
image = []
pattern = re.compile("image:")
with open ('deployment.yaml', 'rt') as myfile:    
    for line in myfile:
        if pattern.search(line) != None:
            clean_data_1 = (line.replace('image:', '')).strip()
            clean_data = (clean_data_1.replace('- ', '')).strip()
            image.append(clean_data)
print(image)
