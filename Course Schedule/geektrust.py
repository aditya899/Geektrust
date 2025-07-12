from sys import argv
from src.lms import LMS


def main():
    
    """
    Sample code to read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    //Add your code here to process the input commands
    """
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    # file_path = "sample_input/input1.txt"
    lms = LMS()
    with open(file_path, 'r') as file:
        for command in file:
            _command = command.strip().split(' ')
            # print(_command)
            if _command[0] == "ADD-COURSE-OFFERING":
                print(lms.add_course(_command))
            elif _command[0] == "REGISTER":
                print(lms.register_course(_command))
            elif _command[0] == "ALLOT":
                lms.course_allotment(_command)
            elif _command[0] == "CANCEL":
                print(lms.cancel_registration(_command))

        # lms.print_added_course()

    
if __name__ == "__main__":
    main()
