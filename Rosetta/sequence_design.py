import pyrosetta
from pyrosetta import rosetta

# Initialize PyRosetta
pyrosetta.init()

# Load your RNA structure into a pose
pose = rosetta.core.import_pose.pose_from_file("raw_test/1YLS_1_B.pdb")

# Create a TaskFactory object
task_factory = rosetta.core.pack.task.TaskFactory()

# Create a TaskOperation to allow redesign of all residues
from pyrosetta.rosetta.core.pack.task.operation import DesignRestrictions
design_selector = DesignRestrictions()
task_factory.push_back(design_selector)

# Create the PackerTask object using the TaskFactory
packer_task = rosetta.core.pack.task.PackerTask(pose)
packer_task.set_task_factory(task_factory)

# Now, pack and design the pose
from pyrosetta.rosetta.core.pack import PackRotamersMover
pack_mover = PackRotamersMover()
pack_mover.task_factory(task_factory)
pack_mover.apply(pose)

# Print the redesigned sequence
print("Redesigned sequence:", pose.sequence())

