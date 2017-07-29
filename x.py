import dicom
import pylab
ds=dicom.read_file("000000.dcm")
pylab.imshow(ds.pixel_array, cmap=pylab.cm.bone)
pylab.show()
