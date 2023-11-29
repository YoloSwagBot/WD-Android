# script to streamline setup for a new Android project
# "CLEAN" Architecture
# (1) Creates common directeories
# (2) Option to add common dependencies(manually kept up to date for now)
# (3) Option to create common modules

import sys
import os

# find root code_directory of newly created project, assuming a default "xyzActivity.kt" file was created.
def find_activity_directory(root_path):
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.endswith("Activity.kt"):
                return dirpath



# "Are you in the root directory of the new Android Project? (Yes/y, No/n)"
# No/no/N/n -> stop script
# Yes/yes/Y/y -> (1) look for build.gradle.kts 
#				 (2) looks for app folder
#				 (3) look for "app/src/main/java/.../.../projectName_lowercase"
while True:
    user_input = input("Are you in the root directory of a newly created Android Project? (Yes/No): ").strip().lower()
    if user_input in ['yes', 'y']:
        break
    elif user_input in ['no', 'n']:
        sys.exit()
    else:
        print("Invalid input. (Yes/y - No/n)")






hasUserAnsweredFirstQuestion = False
hasUserAnsweredSecondQuestion = False
hasUserAnsweredThirdQuestions = False


# (1) top level build.gradle.kts
topLevelGradleFile = None # "/build.gradle.kts"
if (os.path.isfile("build.gradle.kts")):
	topLevelGradleFile = "build.gradle.kts" 
else: 
	topLevelGradleFile = None

# (2) app level build.gradle.kts
appLevelGradleFile = None # "/app/build.gradle.kts"
if (os.path.isfile("app/build.gradle.kts")):
	appLevelGradleFile = "app/build.gradle.kts" 
else: 
	appLevelGradleFile = None

# (3) root code_directory
currDir = os.getcwd()
src_main_java_path = os.path.join(currDir, "app", "src", "main", "java")
codeDir = find_activity_directory(src_main_java_path)


if (topLevelGradleFile is None):
	print("topLevelGradleFile not found. exiting")
	sys.exit()
# else:
# 	print(f"topLevelGradleFile -> {topLevelGradleFile}")

if (appLevelGradleFile is None):
	print("appLevelGradleFile not found. exiting")
	sys.exit()
# else:
# 	print(f"appLevelGradleFile -> {appLevelGradleFile}")

if (codeDir is None):
	print("Initial code directory not found. fix script. exiting")
	sys.exit()
# else:
#     print("xyzActivity.kt' files found.")


# ========================================================================
#===================== All 3 Files/Directories Found =====================
# ========================================================================


# "Setting up "CLEAN" architecture.""
# "What is the name of the initial feature?"
# while (!hasUserAnsweredSecondQuestion)
	


# "Would you like to add common project modules(ie: network, analytics, logger, etc)?"
# while (!hasUserAnsweredThirdQuestions)







# "Good to go!"



