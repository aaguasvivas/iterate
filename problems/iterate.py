import os
import sys

# We start at problems directory
directory = '/home/aaguasvivas/Documents/DataSets/IntroClass/problems'
# Checksum path
path = '/home/aaguasvivas/Documents/DataSets/IntroClass/problems/checksum'

for filename in os.listdir(directory):
    # We don't want to include iterate into this
    if filename.endswith(".py"):
        continue
    # We want to CD to checksum
    if os.path.isdir(filename):
        print(os.path.abspath(filename))
        problemDir = os.path.abspath(filename)
        cwd = os.getcwd()
        os.chdir(problemDir)
        print(os.listdir(problemDir))
        stdDirs = os.listdir(problemDir)
        # count directories -- count students
        # Initialize count
        count = 0
        # If we are in the problems directory
        if os.path.isdir(problemDir):
            # for directory in students,
            for dir in stdDirs:
                # if directory starts with period, continue
                if (dir.startswith(".")):
                    continue
                # other directories would be students
                if (os.path.isdir(dir)):
                    # for every student found, increment
                    count =+ 1
                    # cd into these directories
                    os.chdir(dir)
                    # cd into submission
                    print(os.path.abspath(dir))
                    # ***To this point we are inside a student directory
                    submission = os.path.abspath(dir)
                    # Need to cd into attemptsssssss - MAJOR KEY
                    #for direct in submission:
                    # stops here, gotta cd into attempts
                    if (os.path.isdir(submission)):
                        for direct in os.listdir(submission):
                            if filename.startswith("0"):
                                os.chdir(direct)
                                print(os.path.abspath(direct))
                                attempts = os.path.abspath(direct)
                                os.chdir(attempts)
                                for filename in os.listdir(attempts):
                                # if the file ends with c in submissions, we want to print
                                    if filename.endswith(".c"):
                                        print(os.path.abspath(filename))
                                        lineList = list()
                                        fileName = filename
                                        with open(fileName) as f:
                                            lineList = f.readlines()
                                        for l in lineList:
                                            print(l)
                                            continue
                                    else:
                                        continue
            # print number of student submissions
            print("Number of students:", count)
            # print where we are at
            print(os.path.abspath(filename))
        os.chdir(cwd)
        print (os.listdir(cwd))

        # go into each  then count dirs with c source code
        # then go into each dir submission
        # get c source code into string
        # count how many source code

    # Now we are inside checksum
    # Inside checksum, print number of students, then cd into each student submission
    """ for filename in os.listdir(path):
        # print number of students
        print(filename)
        # cd into each students directory
        os.chdir(filename)
        # if the file ends with .c, print each line as list
        if filename.endswith(".c"):
            lineList = list()
            fileName = filename
            with open(fileName) as f:
                lineList = f.readlines()
            for l in lineList:
                print(l)
            continue
        else:
            continue """