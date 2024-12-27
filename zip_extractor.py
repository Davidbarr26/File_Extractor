import zipfile

def extract_file(filepath, destin_dir):
    with zipfile.ZipFile(filepath, 'r') as file:
        file.extractall(destin_dir)

if __name__ == '__main__':
    extract_file('compressed.zip', 'destin')