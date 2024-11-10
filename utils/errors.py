class CSVFormatError(Exception):
    def __init__(
        self,
        message="Invalid number of columns in input CSV file. Please check the file, Upload Config Parameters and try again.",
        html_message="Invalid number of columns in input CSV file.<br> Please check the file, Upload Config Parameters and try again.",
    ):
        self.message: str = message
        self.html_message: str = html_message
        super().__init__(self.message)
