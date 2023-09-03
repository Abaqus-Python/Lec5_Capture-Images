from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=118.108345031738, 
    height=106.093742370605)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
# from caeModules import *
# from driverUtils import executeOnCaeStartup
# executeOnCaeStartup()

# opened the ODB
o1 = session.openOdb(
    name='E:/AbaPy/channel/Lec5 - Capture Images/aba_data/odb_files/Stand_wcontact.odb')

# displayed the ODB onto viewport
session.viewports['Viewport: 1'].setValues(displayedObject=o1)

# showing the entities in the viewport
import displayGroupOdbToolset as dgo
leaf = dgo.LeafFromElementSets(elementSets=('BOTTOM_FACE', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)

leaf = dgo.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)

# changing to thte deformed shape
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF, ))

# shoiwing the contour
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )

# changing the views
session.viewports['Viewport: 1'].view.setValues(nearPlane=65.9343, 
    farPlane=122.292, width=67.0401, height=30.1699, cameraPosition=(15.2399, 
    32.6932, 94.1444), cameraUpVector=(0.0399467, 0.894883, -0.44451), 
    cameraTarget=(19.4514, -9.20232, 10.1795), viewOffsetX=0.101782, 
    viewOffsetY=0.296659)

session.viewports['Viewport: 1'].view.setValues(session.views['Front'])

node = o1.rootAssembly.instances['STAND-1'].getNodeFromLabel(label=10)

highlight(node)

# saving the image file
session.printToFile(fileName='highlight_node_v2', format=PNG, canvasObjects=(
    session.viewports['Viewport: 1'], ))






