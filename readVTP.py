import vtk
import os

def main():
    colors = vtk.vtkNamedColors()

    filename = '/home/jsl19/data/exampledata2/MaxScar3D.vtp'

    reader = vtk.vtkXMLPolyDataReader()
    reader.SetFileName(filename)
    reader.Update()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('Tan'))

    # Create a rendering window and renderer
    ren = vtk.vtkRenderer()
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    ren.SetBackground(colors.GetColor3d('AliceBlue'))

    # Create a renderwindowinteractor
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Assign actor to the renderer
    ren.AddActor(actor)

    # Enable user interface interactor
    iren.Initialize()
    renWin.Render()
    ren.GetActiveCamera().SetPosition(-0.5, 0.1, 0.0)
    ren.GetActiveCamera().SetViewUp(0.1, 0.0, 1.0)
    renWin.Render()
    iren.Start()


if __name__ == '__main__':
    main()
