class Report:
    def generate_report(self, data):
        print("Report Generated:", data)

    def save_to_file(self, filename, data):
        with open(filename, "w") as file:
            file.write(data)


class Report:
    def generate_report(self, data):
        print("Report Generated:", data)

class FileSaver:
    def save_to_file(self, filename, data):
        with open(filename, "w") as file:
            file.write(data)
