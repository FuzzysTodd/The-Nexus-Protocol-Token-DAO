from _typeshed import Incomplete

class Pca:
    """
    A basic class for Principal Component Analysis (PCA).

    p is the number of dimensions, while N is the number of data points
    """
    A: Incomplete
    names: Incomplete
    def __init__(self, data, names: Incomplete | None = None) -> None:
        """
        p X N matrix input
        """
    def getCovarianceMatrix(self):
        """
        returns the covariance matrix for the dataset
        """
    def getEigensystem(self):
        """
        returns a tuple of (eigenvalues,eigenvectors) for the data set.
        """
    def getEigenvalues(self): ...
    def getEigenvectors(self): ...
    def getEnergies(self):
        '''
        "energies" are just normalized eigenvectors
        '''
    def plot2d(self, ix: int = 0, iy: int = 1, clf: bool = True) -> None:
        """
        Generates a 2-dimensional plot of the data set and principle components
        using matplotlib.

        ix specifies which p-dimension to put on the x-axis of the plot
        and iy specifies which to put on the y-axis (0-indexed)
        """
    def plot3d(self, ix: int = 0, iy: int = 1, iz: int = 2, clf: bool = True) -> None:
        """
        Generates a 3-dimensional plot of the data set and principle components
        using mayavi.

        ix, iy, and iz specify which of the input p-dimensions to place on each of
        the x,y,z axes, respectively (0-indexed).
        """
    def sigclip(self, sigs):
        """
        clips out all data points that are more than a certain number
        of standard deviations from the mean.

        sigs can be either a single value or a length-p sequence that
        specifies the number of standard deviations along each of the
        p dimensions.
        """
    def reset(self) -> None: ...
    def project(self, vals: Incomplete | None = None, enthresh: Incomplete | None = None, nPCs: Incomplete | None = None, cumen: Incomplete | None = None):
        """
        projects the normalized values onto the components

        enthresh, nPCs, and cumen determine how many PCs to use

        if vals is None, the normalized data vectors are the values to project.
        Otherwise, it should be convertable to a p x N array

        returns n,p(>threshold) dimension array
        """
    def deproject(self, A, normed: bool = True):
        """
        input is an n X q array, where q <= p

        output is p X n
        """
    def subtractPC(self, pc, vals: Incomplete | None = None):
        """
        pc can be a scalar or any sequence of pc indecies

        if vals is None, the source data is self.A, else whatever is in vals
        (which must be p x m)
        """
