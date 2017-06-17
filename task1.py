class Histogram(object):

    def __init__(self):
        pass

    def use_success_parameter(self,x):
        return {
            True: 'S',
            False: 'F',
        }.get(x, 'None')

    def group_by(self, stream, field, success=None):

        hist = {}
        data = stream.readlines()[2:]
        success_parameter = self.use_success_parameter(success)

        for line in data:
            # not filtered
            if success_parameter == 'None':
                if field == 'year':
                    hist[line[40:44]] = hist.get(line[40:44], 0) + 1

                elif field == 'month':
                    hist[line[18:21]] = hist.get(line[18:21], 0) + 1
                else:
                    print("Incorrect field")
            else:
            # filtered according 'S' or 'F'
                if field == 'year':
                    if line[193:194] == success_parameter:
                        hist[line[40:44]] = hist.get(line[40:44], 0) + 1

                elif field == 'month':
                    if line[193:194] == success_parameter:
                        hist[line[18:21]] = hist.get(line[18:21], 0) + 1
                else:
                    print("Incorrect field")
        return hist


def main():
    reader = Histogram()
    result = reader.group_by(open("launchlog.txt"), 'year', success=True)
    print(result)

if __name__ == "__main__":
    main()
