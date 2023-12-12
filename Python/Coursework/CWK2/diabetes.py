"""
Please write your name
@author: Cal Levitt

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Diabetes:
    def __init__(self, filepath: str) -> None:
        self.header = []
        self.data = []
        try:
            with open(filepath) as diabetes_csv:
                reader = csv.reader(diabetes_csv, delimiter=",")
                line = 0
                for row in reader:
                    if line == 0:
                        self.header = row
                        line += 1
                    else:
                        self.data.append(row)
                        line += 1
        except Exception:
            raise (FileNotFoundError)

    def get_dimension(self) -> list:
        dimensions = []
        dimensions.append(len(self.data))
        dimensions.append(len(self.headers))
        return dimensions

    def web_summary(self, filepath: str) -> None:
        data_count = []
        positiveDataCount = []
        negativeDataCount = []
        for item in self.headers[2:-1]:
            positiveDataCount.append([item, 0, 0])
            negativeDataCount.append([item, 0, 0])
        for row in self.data:
            for i in range(2, len(row)-1):
                if row[-1] == "Positive":
                    if row[i] == "Yes":
                        positiveDataCount[i-2][1] += 1
                    elif row[i] == "No":
                        positiveDataCount[i-2][2] += 1
                elif row[-1] == "Negative":
                    if row[i] == "Yes":
                        negativeDataCount[i-2][1] += 1
                    elif row[i] == "No":
                        negativeDataCount[i-2][2] += 1

        with open(filepath, "w") as html:
            html.write("<html>\n")
            html.write("<head>\n")
            html.write("<title>Table</title>\n")
            # I used information to help with table styling
            # and structure of HTML tables
            # found at https://www.w3schools.com/html/html_tables.asp
            html.write("<style>")
            html.write("th, td {text-align: middle;padding: 8px;border: \
                       1px solid black;border-collapse: collapse;}")
            html.write("tr:nth-child(even) {background-color: #D6EEEE;}")
            html.write("</style>")
            html.write("</head>\n")
            html.write("<body>\n")
            html.write("<table>\n")
            html.write("<tr>\n")
            html.write("<th colspan=\"2\" rowspan=\"3\">Attributes</th>\n")
            html.write("<th colspan=\"4\">Class</th>\n")
            html.write("</tr>\n")
            html.write("<tr>\n")
            html.write("<th colspan=\"2\">Positive</th>\n")
            html.write("<th colspan=\"2\">Negative</th>\n")
            html.write("</tr>\n")
            html.write("<tr>\n")
            html.write("<th>Yes</td>")
            html.write("<th>No</td>")
            html.write("<th>Yes</td>")
            html.write("<th>No</td>")
            html.write("</tr>\n")

            # Populate table with data
            for i in range(len(positiveDataCount)):
                html.write("<tr>\n")
                html.write("<th colspan=\"2\">" + positiveDataCount[i][0] +
                           "</th>")
                html.write("<th>"+str(positiveDataCount[i][1])+"</td>")
                html.write("<th>"+str(positiveDataCount[i][2])+"</td>")
                html.write("<th>"+str(negativeDataCount[i][1])+"</td>")
                html.write("<th>"+str(negativeDataCount[i][2])+"</td>")
                html.write("</tr>\n")

            html.write("</table>\n")
            html.write("</body>\n")
            html.write("</html>\n")

    def count_instances(self, criteria) -> int:

        """
        This method counts the instances that meets specific given
        search criteria in a CSV file on diabetes

        Args:
            criteria: A dictionary containing the required search criteria,
            Keys are column names, values are the desired value for that column

        Returns:
            int: The number of instances that satisfy the search criteria

        Examples:
            To count instances in which Age=20 and Gender="Male":
            diabetes_instance.count_instances({"Age": 20, "Gender": "Male"})

            To count instances in which
            Gender="Female"; weakness="Yes" and class="Positive":
            diabetes_instance.count_instances({"Gender": "Female",
                            "weakness": "Yes", "class": "Positive"})
        """

        count = 0

        # Iterate over each row in the data
        for row in self.data:
            # Check if the row satisfies all criteria
            match = True
            for key in criteria:

                column = self.headers.index(key)

                if row[column].isnumeric():
                    item = int(row[column])
                else:
                    item = row[column]

                if item != criteria[key]:
                    match = False

            if match:
                count += 1

        return count


if __name__ == "__main__":
    # You can comment the following when you are testing your code
    # You can add more tests as you want

    # test diabetes_data.csv
    d1 = Diabetes("diabetes_data.csv")
    print(d1.get_dimension())
    d1.web_summary('stat01.html')
    print(d1.count_instances({"Gender": "Female", "weakness":
                              "Yes", "class": "Positive"}))

    # test diabetes2_data.csv
    d2 = Diabetes("diabetes2_data.csv")
    print(d2.get_dimension())
    d2.web_summary('stat02.html')
    print(d2.count_instances({"Age": 58, "Gender": "Male"}))
    # change according to your criteria
