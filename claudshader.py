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