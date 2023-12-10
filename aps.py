# Carson Bath
# [ https://github.com/yoloswagbot ]

# script to streamline setup for a new Android project
# "CLEAN" Architecture
# (1) Creates common directeories
# (2) Option to add common dependencies(manually kept up to date for now)
# (3) Option to create common modules

import sys
import os



# ========================================================================
#============= First Script Question, file/dir variable ==================
# ========================================================================

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
		print("Go to the root directory of a brand new Android project.")
		sys.exit()
	else:
		print("Invalid input. (Yes/y - No/n)")


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
# find root code_directory of newly created project, assuming a default "xyzActivity.kt" file was created.
def find_activity_directory(root_path):
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.endswith("Activity.kt"):
                return dirpath

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
#     print(f"codeDir is : {codeDir}")


# ========================================================================
#============= Setup CLEAN architecture, ask Feature name ================
# ========================================================================

packageName = codeDir.split('java/')[-1].replace('/', '.')
print(f"packageName is: {packageName}")


while True:
	feature_input = input("Setting up \"CLEAN\" architecture, name of intial Feature? (ie: GithubUsers, UserData, etc):  ").strip()
	confirmation = input(f"Confirm feature name:  '{feature_input}'  (yes/no): ").lower()
	if (confirmation) in ['yes', 'y']:
		break
	elif (confirmation) in ['no', 'n']:
		print("Enter the feature name you want.")
	else:
		print("Invalid input. (Yes/y - No/n)")


def create_folders_and_files(folder_structure, base_path="."):
    for item_name, content in folder_structure.items():
        item_path = os.path.join(base_path, item_name)

        if isinstance(content, dict):
            # If the content is a dictionary, it's a subfolder
            if not os.path.exists(item_path):
                os.makedirs(item_path)
            create_folders_and_files(content, item_path)
        elif isinstance(content, str):
            # If the content is a string, it's a file with the given content
            with open(item_path, 'w') as file:
                file.write(content)

clean_struct = {
	codeDir : {
		"data" : {

		},
		"domain" : {
			"interfaces" : {},
			"models" : {},
			"usecases" : {}
		},
		"ui" : {
			feature_input.lower() : {
				"screens" : {

				},
				"viewmodels" : {

				}
			}
		},
		"util" : {
			"Constants.kt" : ''
		},
		"di" : {

		}
	}
}

base_code_dir_path = "app/src/main/java/{packageName}"

create_folders_and_files(clean_struct, base_code_dir_path)


# TODO - EDIT THE MANIFEST FILE

# "Would you like to add common project modules(ie: network, analytics, logger, etc)?"
# while (!hasUserAnsweredThirdQuestions)







# "Good to go!"










# Carson Bath
# [ https://github.com/yoloswagbot ]
