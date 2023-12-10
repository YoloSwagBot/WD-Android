# Carson Bath
# [ https://github.com/yoloswagbot ]

# script to streamline setup for a new Android project
# "CLEAN" Architecture
# (1) Creates common directeories
# (2) Option to add common dependencies(manually kept up to date for now)
# (3) Option to create common modules

import sys
import os
import shutil #moving files/dirs


# ========================================================================
# ============= First Script Question, file/dir variable =================
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
# ======= Ask Application file name, ie: MyApp, MyApplication ============
# ========================================================================

while True:
	applicationFileName = input("Name of Application file to create(ie: MyApp, MyApplication)?  ").strip()
	confirmAppName = input(f"Confirm app file name:  '{applicationFileName}'  (yes/no): ").lower()
	if (confirmAppName) in ['yes', 'y']:
		break
	else:
		print("Invalid input. (Yes/y - No/n)")

# ========================================================================
# ======================== initial Feature name ==========================
# ========================================================================

while True:
	feature_input = input("Setting up \"CLEAN\" architecture, name of intial Feature? (ie: GithubUsers, UserData, etc):  ").strip()
	confirmation = input(f"Confirm feature name:  '{feature_input}'  (yes/no): ").lower()
	if (confirmation) in ['yes', 'y']:
		break
	else:
		print("Invalid input. (Yes/y - No/n)")

# ========================================================================
# ========================== Create Directories ==========================
# ========================================================================

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

packageName = codeDir.split('java/')[-1].replace('/', '.')
# print(f"packageName is: {packageName}")

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

base_code_dir_path = f"app/src/main/java/{packageName}".replace('.', '/')

create_folders_and_files(clean_struct, base_code_dir_path)

# ========================================================================
# ========== Edit Manifest file, Application/MainActivity ================
# ========================================================================

def move_file(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"File moved from {source_path} to {destination_path}")
    except FileNotFoundError:
        print(f"Error: File not found at {source_path}")
    except Exception as e:
        print(f"Error: {e}")

# Activity
# (1) Move MainActivity.kt to ui/MainActivity.kt
# (2) Change manifest ".MainActivity" to "ui.MainAcitivity"
activityFileName = "MainActivity.kt"
pathOfActivityFile = os.path.join(base_code_dir_path, activityFileName)
newActivityFilePath = os.path.join(base_code_dir_path, "ui", activityFileName)
move_file(pathOfActivityFile, newActivityFilePath)
# (3a) add ".ui" to package at top of file
# 	(ie: package com.appstr.testsetupproject -> package com.appstr.testsetupproject.ui)
# Read the content of the file
with open(newActivityFilePath, 'r') as file:
    lines = file.readlines()
# (3b) Modify the first line by adding ".ui" to the end
if lines:
    lines[0] = lines[0].rstrip('\n') + ".ui\n"
# (3c) Write the modified content back to the file
with open(newActivityFilePath, 'w') as file:
    file.writelines(lines)


# Application
# (1) Create the Application file by name
applicationFile = f"package {packageName}\n\nimport android.app.Application\n\nclass {applicationFileName}: Application() {{\n\n}}\n\n"
applicationFilePath = os.path.join(base_code_dir_path, f"{applicationFileName}.kt")
with open(applicationFilePath, 'w') as file:
    file.write(applicationFile)

# (2a) Add the "android:name=\".applicationFileName\"" to <application, new line
# Read the content of the file
manfiestFilePath = f"app/src/main/AndroidManifest.xml"
with open(manfiestFilePath, 'r') as file:
    lines = file.readlines()
# (2b) Find the line with the search string and insert a new line after it
for i, line in enumerate(lines):
    if "<application" in line:
        lines.insert(i + 1, f"\t\tandroid:name=\".{applicationFileName}\"\n")
    # (2c) Replace .MainActivity with .ui.MainActivity
    elif (".MainActivity") in line:
        lines[i] = line.replace(".MainActivity", ".ui.MainActivity")
# (2d) Write the modified content back to the file
with open(manfiestFilePath, 'w') as file:
    file.writelines(lines)





# Carson Bath
# [ https://github.com/yoloswagbot ]

