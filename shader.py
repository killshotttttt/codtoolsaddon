import bpy
import subprocess
import sys

# Ensure pip is available
try:
    import ensurepip
    ensurepip.bootstrap()
except ImportError:
    pass

# Install mysql-connector-python
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

install('mysql-connector-python')
the module button
KiLLSHOT — 7/6/2024 8:55 PM
and this is the Script which actually need the module
SkdSam — 7/6/2024 9:04 PM
That code works for me
Image
KiLLSHOT — 7/6/2024 9:10 PM
it works but the issue i have it as the part of the addon……it won’t let one use the button
Only if i make just this as separate addon
SkdSam — 7/6/2024 9:11 PM
Why cant you use the button, send me your file as this should work if it is in the preferences
KiLLSHOT — 7/6/2024 9:12 PM
Attachment file type: archive
COD_TOOL_RIGUPDATE.zip
7.85 KB
this is the full addon
KiLLSHOT — 7/6/2024 9:12 PM
i can but i already have it installed ...but one who doesnot couldnot
KiLLSHOT — 7/6/2024 9:13 PM
.
KiLLSHOT — 7/6/2024 9:13 PM
they had to run the code this way ... and the they could use it
but now its already istalled
SkdSam — 7/6/2024 9:21 PM
Image
Maybe they dont have pip installed
KiLLSHOT — 7/6/2024 9:23 PM
does this code take care of that too ?
SkdSam — 7/6/2024 9:23 PM
# Specify the path to your .bat file
bat_file_path = PIPS

# Open a CMD window and execute the .bat file
# The 'cmd /c' prefix is necessary to run the script within the command prompt
subprocess.Popen(['cmd', '/c', bat_file_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
Attachment file type: archive
python install.rar
446 bytes
That will work on windows only but will install PIP
KiLLSHOT — 7/6/2024 9:29 PM
why can’t blender just install the necessary stuff😭
SkdSam — 7/6/2024 9:32 PM
import bpy
import os
import subprocess
import sys

# Function to ensure pip is installed
def install_pip():
    # Check if pip is already installed
    try:
        import pip
        print("pip is already installed.")
    except ImportError:
        print("pip not found. Installing pip...")
        # Path to Blender's Python
        blender_python = os.path.join(bpy.app.binary_path_python)

        # URL to get-pip.py
        get_pip_url = "https://bootstrap.pypa.io/get-pip.py"
        
        # Temporary path to save get-pip.py
        get_pip_script = os.path.join(os.path.expanduser("~"), "get-pip.py")

        # Download get-pip.py
        try:
            import urllib.request
            with urllib.request.urlopen(get_pip_url) as response, open(get_pip_script, 'wb') as out_file:
                data = response.read() 
                out_file.write(data)
        except Exception as e:
            print(f"Failed to download get-pip.py: {e}")
            return
        
        # Run get-pip.py using Blender's Python
        try:
            subprocess.check_call([blender_python, get_pip_script])
            print("pip installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install pip: {e}")
        finally:
            # Clean up by removing the get-pip.py script
            if os.path.exists(get_pip_script):
                os.remove(get_pip_script)

# Run the function to install pip
install_pip()
try this
KiLLSHOT — 7/6/2024 9:36 PM
Image
SkdSam — 7/6/2024 9:37 PM
Yeah if you dont have it installed it should install it, you should fix them other errors
KiLLSHOT — 7/6/2024 9:38 PM
i will lets some without these test again if it works
Image
i tried installing the addon in different version
Image
SkdSam — 7/6/2024 9:41 PM
Yeah, something is running and should not be until you have the installed mysql
KiLLSHOT — 7/6/2024 9:41 PM
its the same thing as before i can’t enable it
only after enable the button shows up
Image
SkdSam — 7/6/2024 9:42 PM
Maybe that the code can not import as its not installed, should not be trying to import until you run the code so not sure why its trying to import at start
KiLLSHOT — 7/6/2024 9:43 PM
can i have the button show up along with the Remove part ?
SkdSam — 7/6/2024 9:43 PM
I did not get that error when I enabled your addon you sent me
KiLLSHOT — 7/6/2024 9:43 PM
I think because you already had it installed maybe
SkdSam — 7/6/2024 9:43 PM
maybe
Is this for local mysql database?
If it is just use the sqlite3
My nodes let you make/edit/delete so on in the database
KiLLSHOT — 7/6/2024 9:48 PM
i had already that main code with mysql …so didn’t try it
i am not that good at this will have to spend a lot time trying to figure other out🥲
SkdSam — 7/6/2024 9:50 PM
Image
My nodes make it easy they even let you create the db file and setup what you need as a table then you can use different nodes to add items or update or delete them. the demo file has it all setup for you to test and play with
Just need to edit the asset settings so it goes to your desktop or folder and not reference mine
You will need to replace the snippet nodes also with your own that you install from my shared zip as they also will give errors as they are refencing a snippet based on my location
KiLLSHOT — 7/6/2024 9:55 PM
ahh yess…interesting, i will just spend some time analysing the node and setup my addon with this
SkdSam — 7/6/2024 9:56 PM
Image
Install the snippets and then replace the files in the demo with the same snippet nodes, once done then shift r to rebuild and it will remove the errors as snippets are pathways to a json file that will error as mine are in my onedrive and the file is referencing that location and not the one on your computer
Image
Also change this location for the asset so it is the folder you want to use to save your db file
KiLLSHOT — 7/6/2024 10:01 PM
ohh wait this is local?😭
SkdSam — 7/6/2024 10:03 PM
Yeah its a file on the users pc
Are you trying to use another location?
Just seen what you are trying to do
Link to an external location use the mac address as part of the key to then see if the users details are in the database and then activiate the adddon
KiLLSHOT — 7/6/2024 10:07 PM
yesss!
so you mentioned onedrive…so it can be maintained online to check and update ? 
SkdSam — 7/6/2024 10:08 PM
No one drive stores my snippets so I can use them on any PC without having to have them on that PC and transfering them to my other PC
KiLLSHOT — 7/6/2024 10:09 PM
oh so it won’t work at the scale i want here
SkdSam — 7/6/2024 10:11 PM
No, Where I use two machines I store files on OneDrive so I can have them on both PC's and dont need to share them to the other device
Personal work only
KiLLSHOT — 7/6/2024 10:12 PM
understood
KiLLSHOT — 7/16/2024 10:07 PM
hey how do screenrecord on pc as gif is there some program?
SkdSam — 7/16/2024 10:08 PM
LICEcap
KiLLSHOT — 7/16/2024 10:09 PM
thankyou 🙌🏻
KiLLSHOT — 7/16/2024 10:57 PM
what is this file operator called ?
Image
SkdSam — 7/16/2024 11:27 PM
It’s a string property set to directory
You can use the get property to get the file path for what you need when it’s set or set it using set property
KiLLSHOT — Yesterday at 5:00 PM
import bpy
import os
from bpy.types import Operator
from bpy.props import StringProperty
from bpy_extras.io_utils import ImportHelper
from bpy.utils import register_class
Expand
claudshader.py
13 KB
SkdSam — Yesterday at 9:22 PM
Image
{
  "material_schemes": [
    {
      "name": "scheme_0x51",
      "priority_semantic": "unk_semantic_0x51",
      "mappings": {
Expand
schemes.json
2 KB
import bpy
import os
import json
from bpy.types import Operator
from bpy.props import StringProperty
from bpy_extras.io_utils import ImportHelper
Expand
claudshader.py
7 KB
I got chat to update the code to take json, this may work, you will need to test it but if you are only going to update the schemes then this will let you replace just the json file and not have to update the addon.
Image should be the json file as a asset
KiLLSHOT — Yesterday at 9:35 PM
thankyou so much ! this for sure helps
SkdSam — Yesterday at 9:37 PM
Just working on a node to read json and save it to another file. This may work with online json also so like a github link
SkdSam — Yesterday at 9:54 PM
OK, just made a node that will let you copy the https://gitlab.com/skdsam/serpens-packages/-/raw/main/package_info.json data and then save it into the json file on a device
Will try to upload it soon to my packages
Image
import bpy
import sys
import site
import os
import requests
import json
Expand
save JSON Data.py
3 KB
Add this file into my packages inside the SKD_json folder 
Image
KiLLSHOT — Yesterday at 9:57 PM
ohh wow.. on it
SkdSam — Yesterday at 9:58 PM
Now you can save your json file to gitlab or github make it public then choose how and when to copy the json content to the json asset file
KiLLSHOT — Yesterday at 9:58 PM
truly goated🫡
SkdSam — Yesterday at 9:59 PM
Delete that one and use this
import bpy
import sys
import site
import os
import requests
import json
Expand
save JSON Data.py
3 KB
I made a change and when I update you will need to change so its best to use this one for now
KiLLSHOT — Yesterday at 10:00 PM
yessir
SkdSam — Yesterday at 10:01 PM
You can use onload node to make it save the data on Blender start
KiLLSHOT — Yesterday at 10:02 PM
yea so no need to like have an update button at all
SkdSam — Yesterday at 10:04 PM
yeah
SkdSam — Yesterday at 10:55 PM
Uploaded it to my packages so now the addon will have an update and install any changes I make to it
KiLLSHOT — Yesterday at 10:56 PM
i was trying to figure out why the nodes don't show up , even after restart😅
KiLLSHOT — Yesterday at 11:17 PM
It shows up in blender version 4.4 but not in 3.6
SkdSam — Yesterday at 11:21 PM
What do you mean?
I have not tested but in Blender 3.6 did you download my packages addon and install it to Blender 3.6?
https://design-demo.co.uk/scripting/

Go here and download the addon using the download button, in blender 4.2 or above you can drag the box into Blender to install
Blender and coding
Serpens – Blender and coding
Design Demo
KiLLSHOT — Yesterday at 11:23 PM
no this was first time
SkdSam — Yesterday at 11:24 PM
Once you have the addon installed go to the preference and then inside the Serpens packages addon click install packages then after it has done restart Blender
When you update packages you have to restart Blender for it to use them as Blender loads nodes on start up only and not in realtime
KiLLSHOT — Yesterday at 11:25 PM
i did , even  the update you pushed....it showed update . Restarted still nothing there
but showed of first try in 4.4
SkdSam — Yesterday at 11:26 PM
I changed the node name to copy jason data
Might be the reason you dont see the node as save json data was the last name of the node
KiLLSHOT — Yesterday at 11:28 PM
should i continue in 4.4 or like download 4.2. might be time say goodbye to 3.6😂
SkdSam — Yesterday at 11:29 PM
Up to you, the packages should work in 3.6
Can you share a screen grab of what is missing?
KiLLSHOT — Yesterday at 11:31 PM
the install and everything seems to work , just the Skd package nodes dont show up  in the list
SkdSam — Yesterday at 11:31 PM
OK
So the addon installed, and you went into preferences an then used the install packages button. Closed and restarted Blender? 
KiLLSHOT — Yesterday at 11:33 PM
Yes and no SKD Packages in the list.
one sec i will start up pc
SkdSam — Yesterday at 11:33 PM
Wait
Attachment file type: archive
Skd_Packages.zip
285.98 KB
Go to blender addons folder then find blender_visual_scripting_addon
inside the folder is nodes folder unpack this zip into that folder and restart Blender it should then have the nodes
KiLLSHOT — Yesterday at 11:35 PM
on it
yoooooooooooooooooo
Image
Image
its here🥳
SkdSam — Yesterday at 11:40 PM
I would delete the other folders that it has such as _main and the zip file and the other 2 folders so you only have Skd_Packages
Image
KiLLSHOT — Yesterday at 11:41 PM
🫡🫡
SkdSam — Yesterday at 11:41 PM
Not sure what the one with the arrow is but again if it has my packages delete it 
KiLLSHOT — Yesterday at 11:43 PM
yess those 4 look like older ones
Sorted now works👌🏻
SkdSam — Yesterday at 11:44 PM
Maybe it was clashing with them so should update as normal now
KiLLSHOT — Yesterday at 11:45 PM
Thankyou for all the help♥️
SkdSam — Yesterday at 11:47 PM
No problem, if the code works with the json file then your golden.. I use gitkraken to push my stuff to github as it sees the change file and just uploads it.. Its free this way you just open the app edit the file press commit and then it sends it to Github for you. Also it stores the history of the file so you can revert back if needed
https://www.gitkraken.com/
GitKraken
GitKraken Legendary Git Tools | GitKraken
Meet GitKraken, the creator of legendary Git tools for developers and teams - like the GitKraken Desktop, with Git GUI and CLI, Git Integration for Jira, and GitLens for VS Code.
GitKraken Legendary Git Tools | GitKraken
Image
KiLLSHOT — Yesterday at 11:51 PM
That's really cool , i was confused my addon has some 300mb blend file in as asset so like just having to update small part would be a better way
SkdSam — Yesterday at 11:52 PM
Should not be that large if it is just nodes and code
Go orphan files and purge unused items
KiLLSHOT — Yesterday at 11:53 PM
Been messing around with a lot of cloud stuff and every bit of data makes me feel thats going to cost😂😭
SkdSam — Yesterday at 11:53 PM
How many Serpens properties does your addon have?
KiLLSHOT — Yesterday at 11:54 PM
properties as in
SkdSam — Yesterday at 11:54 PM
Image
KiLLSHOT — Yesterday at 11:55 PM
4
SkdSam — Yesterday at 11:55 PM
OK
Lets try this
Open a new blender file
KiLLSHOT — Yesterday at 11:55 PM
in
SkdSam — Yesterday at 11:56 PM
Create them properties in the new file so they have same names and settings
KiLLSHOT — Yesterday at 11:57 PM
done
SkdSam — Yesterday at 11:57 PM
After you done this, append node trees from your addon Blender .. This should import the nodes and use the same properties it had and then save it .. It should pull any scripts so on..
Now you should have your Blender addon in the new Blender file and a smaller file size
You might have to also add the assets up again if you had any assets
KiLLSHOT — Yesterday at 11:59 PM
yeaa the assets
SkdSam — 12:01 AM
You just need to add them links in the new Blender file and it should reduce your Blender file size
KiLLSHOT — 12:01 AM
yup the blend size is way smaller now
also seems it had some of the textures from testing
SkdSam — 12:03 AM
Keep your other file but if it is all working once you have it all set with assets then you have a smaller addon file now
Add that new Blender file to the same folder as your larger one and work in that file then you have a quicker loading file.. You may have to delete the node tree that was default in the new Blend file
Visual Scripting Editor if you have Visual Scripting Editor.001 or if you had named the node trees to new names then just remove the one you are not using and your all set
KiLLSHOT — 12:05 AM
yup removed the default one 🫡
SkdSam — 12:06 AM
Just check your nodes that are referencing the properties are not in red colour and are seeing the correct node tree and property
I think it ports over variables but check they are in the file also if you had any
KiLLSHOT — 12:07 AM
Yup no red colors 👌🏻
will work on this one from now
SkdSam — 12:07 AM
Perfect , shift r to compile and it should show the UI correct and have no errors if all worked
Now you most likely have 10mb file 🤣
🏅
KiLLSHOT — 12:08 AM
Image
all set
KiLLSHOT — 12:09 AM
the assets are gonna add up🤣
SkdSam — 12:09 AM
O, its for call of duty
KiLLSHOT — 12:09 AM
yess😛
SkdSam — 12:09 AM
Yeah assets will get packed into the addon but wont be in the main addon Blender file so it should stay small
By the way whats it do?
KiLLSHOT — 12:10 AM
thats barely 4mbs
KiLLSHOT — 12:10 AM
sets up material for cod assets
hold on i will show
SkdSam — 12:11 AM
Sure
KiLLSHOT — 12:14 AM
Image
also like apply camos for weapon and some rigging stuff
SkdSam — 12:15 AM
Nice, so ripping the models out and then using them to animate inside Blender?
KiLLSHOT — 12:17 AM
yes for ripping is a different tool, mines just for in blender
SkdSam — 12:18 AM
Yeah, It would need to be a C coding tool to rip the data..
KiLLSHOT — 12:18 AM
https://youtu.be/G3rPV80fkd8?si=Kfp3iHXicTvh-HIY
YouTube
killshotttttt
COD AUTO-SHADER TUTORIAL  | FPP RIG + CAMO SHADER | BLENDER ADD-ON
Image
SkdSam — 12:18 AM
Might be a good tool for streamers to make their Youtube intro vids
KiLLSHOT — 12:18 AM
i could have just sent the whole video instead of this 🤣😭
KiLLSHOT — 12:19 AM
mostly thumbnails
Image
Image
Image
a few i made
last one was actually a custom model , got a 3d scan made a meta human out of it and put the head on a cod model with some custom textures
SkdSam — 12:23 AM
You could simulate the setting of the size of the model on import to 0.011 or what ever it was in the video
KiLLSHOT — 12:25 AM
yea i did that before but removed it , many used some tool to connect the body and head before importing and that would mess things up
so left it unchanged
SkdSam — 12:26 AM
Well now if the stuff we did worked the updating of the json file will be good for quick updates and not having to role out a new version
KiLLSHOT — 12:27 AM
yup , with new models those mapping would change every now and then so it will definitely be great
will continue working on that tomorrow
again thanks for all the help
SkdSam — 12:31 AM
Welcome
﻿
SkdSam
skdsam
 
import bpy
import os
from bpy.types import Operator
from bpy.props import StringProperty
from bpy_extras.io_utils import ImportHelper
from bpy.utils import register_class

# Define all your material schemes here - ORDER MATTERS! (Priority from top to bottom)
MATERIAL_SCHEMES = [
    # Scheme 1: 0x51 primary (HIGHEST PRIORITY)
    {
        "name": "scheme_0x51",
        "priority_semantic": "unk_semantic_0x51",
        "mappings": {
            "unk_semantic_0x51": {"inputs": [0, 1], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
            "unk_semantic_0x52": {"inputs": [2, 3], "colorspace": "Non-Color", "alpha_mode": None},
            "unk_semantic_0x53": {"inputs": [10], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
            "unk_semantic_0x54": {"inputs": [12], "colorspace": "Non-Color", "alpha_mode": None},
        }
    },
    
    # Scheme 2: 0x55 primary
    {
        "name": "scheme_0x55",
        "priority_semantic": "unk_semantic_0x55",
        "mappings": {
            "unk_semantic_0x55": {"inputs": [0, 1], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
            "unk_semantic_0x56": {"inputs": [2, 3], "colorspace": "Non-Color", "alpha_mode": None},
            "unk_semantic_0x58": {"inputs": [12], "colorspace": "Non-Color", "alpha_mode": None},
            "unk_semantic_0x5C": {"inputs": [15], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
        }
    },
    
    # Scheme 3: 0x56 primary
    {
        "name": "scheme_0x56",
        "priority_semantic": "unk_semantic_0x56",
        "mappings": {
            "unk_semantic_0x56": {"inputs": [0, 1], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
            "unk_semantic_0x57": {"inputs": [2, 3], "colorspace": "Non-Color", "alpha_mode": None},
            "unk_semantic_0x59": {"inputs": [12], "colorspace": "Non-Color", "alpha_mode": None},
            "unk_semantic_0x58": {"inputs": [10], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
            "unk_semantic_0x5D": {"inputs": [15, 14], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
        }
    },
    
    # Scheme 4: 0x57 primary
    {
        "name": "scheme_0x57",
        "priority_semantic": "unk_semantic_0x57",
        "mappings": {
            "unk_semantic_0x57": {"inputs": [0, 1], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
            "unk_semantic_0x58": {"inputs": [2, 3], "colorspace": "Non-Color", "alpha_mode": None},
            "unk_semantic_0x5A": {"inputs": [12], "colorspace": "Non-Color", "alpha_mode": None},
            "unk_semantic_0x5E": {"inputs": [15, 14], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
            "unk_semantic_0x59": {"inputs": [10], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
        }
    },
    
    # Scheme 5: 0x3 primary (basic)
    {
        "name": "scheme_0x3_basic",
        "priority_semantic": "unk_semantic_0x3",
        "mappings": {
            "unk_semantic_0x3": {"inputs": [0, 1], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
            "unk_semantic_0x4": {"inputs": [2, 3], "colorspace": "Non-Color", "alpha_mode": None},
            "unk_semantic_0x5": {"inputs": [12], "colorspace": "Non-Color", "alpha_mode": None},
        }
    },
    
    # Scheme 6: 0x4 primary
    {
        "name": "scheme_0x4",
        "priority_semantic": "unk_semantic_0x4",
        "mappings": {
            "unk_semantic_0x4": {"inputs": [0, 1], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
            "unk_semantic_0x5": {"inputs": [2, 3], "colorspace": "Non-Color", "alpha_mode": None},
            "unk_semantic_0x6": {"inputs": [12], "colorspace": "Non-Color", "alpha_mode": None},
        }
    },
    
    # Scheme 7: 0x6 primary
    {
        "name": "scheme_0x6",
        "priority_semantic": "unk_semantic_0x6",
        "mappings": {
            "unk_semantic_0x6": {"inputs": [0, 1], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
            "unk_semantic_0x7": {"inputs": [2, 3], "colorspace": "Non-Color", "alpha_mode": None},
            "unk_semantic_0x8": {"inputs": [15, 14], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
        }
    },
    
    # Scheme 8: 0xA primary
    {
        "name": "scheme_0xA",
        "priority_semantic": "unk_semantic_0xA",
        "mappings": {
            "unk_semantic_0x4": {"inputs": [0, 1], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
            "unk_semantic_0x5": {"inputs": [2, 3], "colorspace": "Non-Color", "alpha_mode": None},
            "unk_semantic_0x8": {"inputs": [15], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
            "unk_semantic_0x6": {"inputs": [12], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
        }
    }
]

# Default fallback scheme
DEFAULT_SCHEME = {
    "name": "default",
    "priority_semantic": "unk_semantic_0x3",
    "mappings": {
        "unk_semantic_0x3": {"inputs": [0, 1], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
        "unk_semantic_0x4": {"inputs": [2, 3], "colorspace": "Non-Color", "alpha_mode": None},
    }
}

def detect_material_scheme(nodes):
    """Detect which scheme to use based on available image nodes - PRIORITY ORDER MATTERS!"""
    available_semantics = set()
    for node in nodes:
        if node.type == 'TEX_IMAGE' and node.label:
            available_semantics.add(node.label)
    
    # Check schemes in PRIORITY ORDER (first match wins, like original code)
    for scheme in MATERIAL_SCHEMES:
        priority_semantic = scheme["priority_semantic"]
        if priority_semantic in available_semantics:
            print(f"Selected scheme: {scheme['name']} (priority: {priority_semantic})")
            return scheme
    
    # Fallback to default
    print("Using default scheme")
    return DEFAULT_SCHEME

def connect_image_nodes_to_cod(material, cod_node):
    """Connect image nodes to the COD node based on detected scheme."""
    node_tree = material.node_tree
    nodes = node_tree.nodes
    links = node_tree.links
    
    # Detect which scheme to use
    scheme = detect_material_scheme(nodes)
    
    # Apply the scheme
    for node in nodes:
        if node.type == 'TEX_IMAGE' and node.label in scheme["mappings"]:
            mapping = scheme["mappings"][node.label]
            
            # Connect to specified inputs
            inputs = mapping["inputs"]
            if len(inputs) >= 1:
                links.new(node.outputs["Color"], cod_node.inputs[inputs[0]])
            if len(inputs) >= 2:
                links.new(node.outputs["Alpha"], cod_node.inputs[inputs[1]])
            
            # Set colorspace
            if mapping["colorspace"]:
                node.image.colorspace_settings.name = mapping["colorspace"]
            
            # Set alpha mode
            if mapping["alpha_mode"]:
                node.image.alpha_mode = mapping["alpha_mode"]
            
            print(f"Connected {node.label} to COD inputs {inputs}")

def ensure_cod_node_group():
    """Creates a COD node group if it doesn't already exist."""
    if "COD" not in bpy.data.node_groups:
        cod_group = bpy.data.node_groups.new("COD", 'ShaderNodeTree')
        cod_group.inputs.new("NodeSocketShader", "Shader Input")
        cod_group.outputs.new("NodeSocketShader", "Shader Output")
        
        output_node = cod_group.nodes.new("NodeGroupOutput")
        output_node.location = (300, 0)
        
        input_node = cod_group.nodes.new("NodeGroupInput")
        input_node.location = (-300, 0)
        
        cod_group.links.new(input_node.outputs[0], output_node.inputs[0])
    
    return bpy.data.node_groups["COD"]

def add_cod_node_to_material_with_images(filepath):
    """Process a material file and set up the node system."""
    material_name = bpy.path.display_name_from_filepath(filepath)[:-7]
    
    # Get or create the material
    material = bpy.data.materials.get(material_name)
    if not material:
        material = bpy.data.materials.new(name=material_name)
        material.use_nodes = True

    node_tree = material.node_tree
    nodes = node_tree.nodes
    links = node_tree.links

    cod_group = ensure_cod_node_group()

    # Check if the COD node is already added to avoid duplicates
    cod_node = next((node for node in nodes if node.type == 'GROUP' and node.node_tree == cod_group), None)
    if not cod_node:
        cod_node = nodes.new(type="ShaderNodeGroup")
        cod_node.node_tree = cod_group
        cod_node.location = (-200, 600)
        
        # Connect COD node to Material Output
        material_output = next((node for node in nodes if node.type == 'OUTPUT_MATERIAL'), None)
        if material_output:
            for link in material_output.inputs['Surface'].links:
                links.remove(link)
            links.new(cod_node.outputs[0], material_output.inputs["Surface"])
            print(f"Connected COD node to Material Output for material '{material_name}'.")

    # Process the material file
    with open(filepath, 'r') as f:
        lines = f.readlines()
        row, column = 0, 0

        for line in lines:
            shader_input, image_name = map(str.strip, line.split(','))

            image_path = find_image_path(os.path.dirname(filepath), material_name, image_name)
            if image_path:
                image = bpy.data.images.load(image_path, check_existing=True)
                
                # Check if a node with the same label already exists
                existing_image_node = next((node for node in nodes if node.type == 'TEX_IMAGE' and node.label == shader_input), None)
                if existing_image_node:
                    print(f"Image node '{shader_input}' already exists in material '{material_name}', skipping.")
                    continue

                image_node = nodes.new(type='ShaderNodeTexImage')
                image_node.image = image
                image_node.label = shader_input
                image_node.location = (-600 - column * 250, 300 - row * 300)

                column += 1
                if column >= 4:
                    column = 0
                    row += 1
            else:
                print(f"Image '{image_name}' not found for '{shader_input}' in material '{material_name}'.")

    # Connect nodes using the appropriate scheme
    connect_image_nodes_to_cod(material, cod_node)

def find_image_path(file_path, material_name, image_name):
    """Searches for an image file in the specified directories and returns the path if found."""
    possible_paths = [
        os.path.join(file_path, "_images", material_name, image_name + '.dds'),
        os.path.join(file_path, "_images", material_name, image_name + '.png'),
        os.path.join(file_path, "_images", image_name + '.dds'),
        os.path.join(file_path, "_images", image_name + '.png')
    ]
    for path in possible_paths:
        if os.path.isfile(path):
            return path
    
    return None

# Utility function to add new schemes easily
def add_custom_scheme(scheme_name, priority_semantic, mappings):
    """Add a new custom scheme to the system."""
    MATERIAL_SCHEMES[scheme_name] = {
        "priority_semantic": priority_semantic,
        "mappings": mappings
    }
    print(f"Added custom scheme: {scheme_name}")

class TEST_OT_invoke_file_chooser(Operator, ImportHelper):
    bl_idname = "test.invoke_file_chooser"
    bl_label = "Select Mtl File"
    directory: StringProperty(subtype='DIR_PATH')
    
    def execute(self, context):
        dir_path = bpy.path.abspath(self.directory)
        if not os.path.isdir(dir_path):
            self.report({'ERROR'}, "Invalid directory path")
            return {'CANCELLED'}
        
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    add_cod_node_to_material_with_images(file_path)
                    
        return {'FINISHED'}

# Example of how to add a new scheme:
# add_custom_scheme("my_custom_scheme", "unk_semantic_0x99", {
#     "unk_semantic_0x99": {"inputs": [0, 1], "colorspace": "sRGB", "alpha_mode": "CHANNEL_PACKED"},
#     "unk_semantic_0x9A": {"inputs": [2, 3], "colorspace": "Non-Color", "alpha_mode": None},
# })

register_class(TEST_OT_invoke_file_chooser)
bpy.ops.test.invoke_file_chooser('INVOKE_DEFAULT')
claudshader.py
13 KB
