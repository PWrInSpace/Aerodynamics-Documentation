class CSVReader:
    def readCSV(self, path):
        content = []
        with open(path, 'r') as file:
            for line in file:
                content.append(line.strip().split(','))
        # Transpose the 2D array
        content = list(map(list, zip(*content)))

        return content
