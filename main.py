import easyocr


def text_recognition(file_path):
    reader = easyocr.Reader(["ru"])
    result = reader.readtext(file_path)

    return result



def main():
    file_path = input("Enter a file path: ")
    text_recognition(file_path="file_path")


if __name__ == "__main__":
    main()
