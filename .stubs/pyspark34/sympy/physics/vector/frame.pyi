from _typeshed import Incomplete
from sympy.core.symbol import Symbol

__all__ = ['CoordinateSym', 'ReferenceFrame']

class CoordinateSym(Symbol):
    """
    A coordinate symbol/base scalar associated wrt a Reference Frame.

    Ideally, users should not instantiate this class. Instances of
    this class must only be accessed through the corresponding frame
    as 'frame[index]'.

    CoordinateSyms having the same frame and index parameters are equal
    (even though they may be instantiated separately).

    Parameters
    ==========

    name : string
        The display name of the CoordinateSym

    frame : ReferenceFrame
        The reference frame this base scalar belongs to

    index : 0, 1 or 2
        The index of the dimension denoted by this coordinate variable

    Examples
    ========

    >>> from sympy.physics.vector import ReferenceFrame, CoordinateSym
    >>> A = ReferenceFrame('A')
    >>> A[1]
    A_y
    >>> type(A[0])
    <class 'sympy.physics.vector.frame.CoordinateSym'>
    >>> a_y = CoordinateSym('a_y', A, 1)
    >>> a_y == A[1]
    True

    """
    def __new__(cls, name, frame, index): ...
    @property
    def frame(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...

class ReferenceFrame:
    """A reference frame in classical mechanics.

    ReferenceFrame is a class used to represent a reference frame in classical
    mechanics. It has a standard basis of three unit vectors in the frame's
    x, y, and z directions.

    It also can have a rotation relative to a parent frame; this rotation is
    defined by a direction cosine matrix relating this frame's basis vectors to
    the parent frame's basis vectors.  It can also have an angular velocity
    vector, defined in another frame.

    """
    str_vecs: Incomplete
    pretty_vecs: Incomplete
    latex_vecs: Incomplete
    indices: Incomplete
    name: Incomplete
    varlist: Incomplete
    index: Incomplete
    def __init__(self, name, indices: Incomplete | None = None, latexs: Incomplete | None = None, variables: Incomplete | None = None) -> None:
        """ReferenceFrame initialization method.

        A ReferenceFrame has a set of orthonormal basis vectors, along with
        orientations relative to other ReferenceFrames and angular velocities
        relative to other ReferenceFrames.

        Parameters
        ==========

        indices : tuple of str
            Enables the reference frame's basis unit vectors to be accessed by
            Python's square bracket indexing notation using the provided three
            indice strings and alters the printing of the unit vectors to
            reflect this choice.
        latexs : tuple of str
            Alters the LaTeX printing of the reference frame's basis unit
            vectors to the provided three valid LaTeX strings.

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame, vlatex
        >>> N = ReferenceFrame('N')
        >>> N.x
        N.x
        >>> O = ReferenceFrame('O', indices=('1', '2', '3'))
        >>> O.x
        O['1']
        >>> O['1']
        O['1']
        >>> P = ReferenceFrame('P', latexs=('A1', 'A2', 'A3'))
        >>> vlatex(P.x)
        'A1'

        ``symbols()`` can be used to create multiple Reference Frames in one
        step, for example:

        >>> from sympy.physics.vector import ReferenceFrame
        >>> from sympy import symbols
        >>> A, B, C = symbols('A B C', cls=ReferenceFrame)
        >>> D, E = symbols('D E', cls=ReferenceFrame, indices=('1', '2', '3'))
        >>> A[0]
        A_x
        >>> D.x
        D['1']
        >>> E.y
        E['2']
        >>> type(A) == type(D)
        True

        """
    def __getitem__(self, ind):
        """
        Returns basis vector for the provided index, if the index is a string.

        If the index is a number, returns the coordinate variable correspon-
        -ding to that index.
        """
    def __iter__(self): ...
    def variable_map(self, otherframe):
        """
        Returns a dictionary which expresses the coordinate variables
        of this frame in terms of the variables of otherframe.

        If Vector.simp is True, returns a simplified version of the mapped
        values. Else, returns them without simplification.

        Simplification of the expressions may take time.

        Parameters
        ==========

        otherframe : ReferenceFrame
            The other frame to map the variables to

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame, dynamicsymbols
        >>> A = ReferenceFrame('A')
        >>> q = dynamicsymbols('q')
        >>> B = A.orientnew('B', 'Axis', [q, A.z])
        >>> A.variable_map(B)
        {A_x: B_x*cos(q(t)) - B_y*sin(q(t)), A_y: B_x*sin(q(t)) + B_y*cos(q(t)), A_z: B_z}

        """
    def ang_acc_in(self, otherframe):
        """Returns the angular acceleration Vector of the ReferenceFrame.

        Effectively returns the Vector:

        ``N_alpha_B``

        which represent the angular acceleration of B in N, where B is self,
        and N is otherframe.

        Parameters
        ==========

        otherframe : ReferenceFrame
            The ReferenceFrame which the angular acceleration is returned in.

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame
        >>> N = ReferenceFrame('N')
        >>> A = ReferenceFrame('A')
        >>> V = 10 * N.x
        >>> A.set_ang_acc(N, V)
        >>> A.ang_acc_in(N)
        10*N.x

        """
    def ang_vel_in(self, otherframe):
        """Returns the angular velocity Vector of the ReferenceFrame.

        Effectively returns the Vector:

        ^N omega ^B

        which represent the angular velocity of B in N, where B is self, and
        N is otherframe.

        Parameters
        ==========

        otherframe : ReferenceFrame
            The ReferenceFrame which the angular velocity is returned in.

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame
        >>> N = ReferenceFrame('N')
        >>> A = ReferenceFrame('A')
        >>> V = 10 * N.x
        >>> A.set_ang_vel(N, V)
        >>> A.ang_vel_in(N)
        10*N.x

        """
    def dcm(self, otherframe):
        '''Returns the direction cosine matrix of this reference frame
        relative to the provided reference frame.

        The returned matrix can be used to express the orthogonal unit vectors
        of this frame in terms of the orthogonal unit vectors of
        ``otherframe``.

        Parameters
        ==========

        otherframe : ReferenceFrame
            The reference frame which the direction cosine matrix of this frame
            is formed relative to.

        Examples
        ========

        The following example rotates the reference frame A relative to N by a
        simple rotation and then calculates the direction cosine matrix of N
        relative to A.

        >>> from sympy import symbols, sin, cos
        >>> from sympy.physics.vector import ReferenceFrame
        >>> q1 = symbols(\'q1\')
        >>> N = ReferenceFrame(\'N\')
        >>> A = ReferenceFrame(\'A\')
        >>> A.orient_axis(N, q1, N.x)
        >>> N.dcm(A)
        Matrix([
        [1,       0,        0],
        [0, cos(q1), -sin(q1)],
        [0, sin(q1),  cos(q1)]])

        The second row of the above direction cosine matrix represents the
        ``N.y`` unit vector in N expressed in A. Like so:

        >>> Ny = 0*A.x + cos(q1)*A.y - sin(q1)*A.z

        Thus, expressing ``N.y`` in A should return the same result:

        >>> N.y.express(A)
        cos(q1)*A.y - sin(q1)*A.z

        Notes
        =====

        It is important to know what form of the direction cosine matrix is
        returned. If ``B.dcm(A)`` is called, it means the "direction cosine
        matrix of B rotated relative to A". This is the matrix
        :math:`{}^B\\mathbf{C}^A` shown in the following relationship:

        .. math::

           \\begin{bmatrix}
             \\hat{\\mathbf{b}}_1 \\\\\n             \\hat{\\mathbf{b}}_2 \\\\\n             \\hat{\\mathbf{b}}_3
           \\end{bmatrix}
           =
           {}^B\\mathbf{C}^A
           \\begin{bmatrix}
             \\hat{\\mathbf{a}}_1 \\\\\n             \\hat{\\mathbf{a}}_2 \\\\\n             \\hat{\\mathbf{a}}_3
           \\end{bmatrix}.

        :math:`{}^B\\mathbf{C}^A` is the matrix that expresses the B unit
        vectors in terms of the A unit vectors.

        '''
    def orient_axis(self, parent, axis, angle) -> None:
        """Sets the orientation of this reference frame with respect to a
        parent reference frame by rotating through an angle about an axis fixed
        in the parent reference frame.

        Parameters
        ==========

        parent : ReferenceFrame
            Reference frame that this reference frame will be rotated relative
            to.
        axis : Vector
            Vector fixed in the parent frame about about which this frame is
            rotated. It need not be a unit vector and the rotation follows the
            right hand rule.
        angle : sympifiable
            Angle in radians by which it the frame is to be rotated.

        Warns
        ======

        UserWarning
            If the orientation creates a kinematic loop.

        Examples
        ========

        Setup variables for the examples:

        >>> from sympy import symbols
        >>> from sympy.physics.vector import ReferenceFrame
        >>> q1 = symbols('q1')
        >>> N = ReferenceFrame('N')
        >>> B = ReferenceFrame('B')
        >>> B.orient_axis(N, N.x, q1)

        The ``orient_axis()`` method generates a direction cosine matrix and
        its transpose which defines the orientation of B relative to N and vice
        versa. Once orient is called, ``dcm()`` outputs the appropriate
        direction cosine matrix:

        >>> B.dcm(N)
        Matrix([
        [1,       0,      0],
        [0,  cos(q1), sin(q1)],
        [0, -sin(q1), cos(q1)]])
        >>> N.dcm(B)
        Matrix([
        [1,       0,        0],
        [0, cos(q1), -sin(q1)],
        [0, sin(q1),  cos(q1)]])

        The following two lines show that the sense of the rotation can be
        defined by negating the vector direction or the angle. Both lines
        produce the same result.

        >>> B.orient_axis(N, -N.x, q1)
        >>> B.orient_axis(N, N.x, -q1)

        """
    def orient_explicit(self, parent, dcm) -> None:
        """Sets the orientation of this reference frame relative to a parent
        reference frame by explicitly setting the direction cosine matrix.

        Parameters
        ==========

        parent : ReferenceFrame
            Reference frame that this reference frame will be rotated relative
            to.
        dcm : Matrix, shape(3, 3)
            Direction cosine matrix that specifies the relative rotation
            between the two reference frames.

        Warns
        ======

        UserWarning
            If the orientation creates a kinematic loop.

        Examples
        ========

        Setup variables for the examples:

        >>> from sympy import symbols, Matrix, sin, cos
        >>> from sympy.physics.vector import ReferenceFrame
        >>> q1 = symbols('q1')
        >>> A = ReferenceFrame('A')
        >>> B = ReferenceFrame('B')
        >>> N = ReferenceFrame('N')

        A simple rotation of ``A`` relative to ``N`` about ``N.x`` is defined
        by the following direction cosine matrix:

        >>> dcm = Matrix([[1, 0, 0],
        ...               [0, cos(q1), -sin(q1)],
        ...               [0, sin(q1), cos(q1)]])
        >>> A.orient_explicit(N, dcm)
        >>> A.dcm(N)
        Matrix([
        [1,       0,      0],
        [0,  cos(q1), sin(q1)],
        [0, -sin(q1), cos(q1)]])

        This is equivalent to using ``orient_axis()``:

        >>> B.orient_axis(N, N.x, q1)
        >>> B.dcm(N)
        Matrix([
        [1,       0,      0],
        [0,  cos(q1), sin(q1)],
        [0, -sin(q1), cos(q1)]])

        **Note carefully that** ``N.dcm(B)`` **(the transpose) would be passed
        into** ``orient_explicit()`` **for** ``A.dcm(N)`` **to match**
        ``B.dcm(N)``:

        >>> A.orient_explicit(N, N.dcm(B))
        >>> A.dcm(N)
        Matrix([
        [1,       0,      0],
        [0,  cos(q1), sin(q1)],
        [0, -sin(q1), cos(q1)]])

        """
    def orient_body_fixed(self, parent, angles, rotation_order) -> None:
        '''Rotates this reference frame relative to the parent reference frame
        by right hand rotating through three successive body fixed simple axis
        rotations. Each subsequent axis of rotation is about the "body fixed"
        unit vectors of a new intermediate reference frame. This type of
        rotation is also referred to rotating through the `Euler and Tait-Bryan
        Angles`_.

        .. _Euler and Tait-Bryan Angles: https://en.wikipedia.org/wiki/Euler_angles

        The computed angular velocity in this method is by default expressed in
        the child\'s frame, so it is most preferable to use ``u1 * child.x + u2 *
        child.y + u3 * child.z`` as generalized speeds.

        Parameters
        ==========

        parent : ReferenceFrame
            Reference frame that this reference frame will be rotated relative
            to.
        angles : 3-tuple of sympifiable
            Three angles in radians used for the successive rotations.
        rotation_order : 3 character string or 3 digit integer
            Order of the rotations about each intermediate reference frames\'
            unit vectors. The Euler rotation about the X, Z\', X\'\' axes can be
            specified by the strings ``\'XZX\'``, ``\'131\'``, or the integer
            ``131``. There are 12 unique valid rotation orders (6 Euler and 6
            Tait-Bryan): zxz, xyx, yzy, zyz, xzx, yxy, xyz, yzx, zxy, xzy, zyx,
            and yxz.

        Warns
        ======

        UserWarning
            If the orientation creates a kinematic loop.

        Examples
        ========

        Setup variables for the examples:

        >>> from sympy import symbols
        >>> from sympy.physics.vector import ReferenceFrame
        >>> q1, q2, q3 = symbols(\'q1, q2, q3\')
        >>> N = ReferenceFrame(\'N\')
        >>> B = ReferenceFrame(\'B\')
        >>> B1 = ReferenceFrame(\'B1\')
        >>> B2 = ReferenceFrame(\'B2\')
        >>> B3 = ReferenceFrame(\'B3\')

        For example, a classic Euler Angle rotation can be done by:

        >>> B.orient_body_fixed(N, (q1, q2, q3), \'XYX\')
        >>> B.dcm(N)
        Matrix([
        [        cos(q2),                            sin(q1)*sin(q2),                           -sin(q2)*cos(q1)],
        [sin(q2)*sin(q3), -sin(q1)*sin(q3)*cos(q2) + cos(q1)*cos(q3),  sin(q1)*cos(q3) + sin(q3)*cos(q1)*cos(q2)],
        [sin(q2)*cos(q3), -sin(q1)*cos(q2)*cos(q3) - sin(q3)*cos(q1), -sin(q1)*sin(q3) + cos(q1)*cos(q2)*cos(q3)]])

        This rotates reference frame B relative to reference frame N through
        ``q1`` about ``N.x``, then rotates B again through ``q2`` about
        ``B.y``, and finally through ``q3`` about ``B.x``. It is equivalent to
        three successive ``orient_axis()`` calls:

        >>> B1.orient_axis(N, N.x, q1)
        >>> B2.orient_axis(B1, B1.y, q2)
        >>> B3.orient_axis(B2, B2.x, q3)
        >>> B3.dcm(N)
        Matrix([
        [        cos(q2),                            sin(q1)*sin(q2),                           -sin(q2)*cos(q1)],
        [sin(q2)*sin(q3), -sin(q1)*sin(q3)*cos(q2) + cos(q1)*cos(q3),  sin(q1)*cos(q3) + sin(q3)*cos(q1)*cos(q2)],
        [sin(q2)*cos(q3), -sin(q1)*cos(q2)*cos(q3) - sin(q3)*cos(q1), -sin(q1)*sin(q3) + cos(q1)*cos(q2)*cos(q3)]])

        Acceptable rotation orders are of length 3, expressed in as a string
        ``\'XYZ\'`` or ``\'123\'`` or integer ``123``. Rotations about an axis
        twice in a row are prohibited.

        >>> B.orient_body_fixed(N, (q1, q2, 0), \'ZXZ\')
        >>> B.orient_body_fixed(N, (q1, q2, 0), \'121\')
        >>> B.orient_body_fixed(N, (q1, q2, q3), 123)

        '''
    def orient_space_fixed(self, parent, angles, rotation_order) -> None:
        '''Rotates this reference frame relative to the parent reference frame
        by right hand rotating through three successive space fixed simple axis
        rotations. Each subsequent axis of rotation is about the "space fixed"
        unit vectors of the parent reference frame.

        The computed angular velocity in this method is by default expressed in
        the child\'s frame, so it is most preferable to use ``u1 * child.x + u2 *
        child.y + u3 * child.z`` as generalized speeds.

        Parameters
        ==========
        parent : ReferenceFrame
            Reference frame that this reference frame will be rotated relative
            to.
        angles : 3-tuple of sympifiable
            Three angles in radians used for the successive rotations.
        rotation_order : 3 character string or 3 digit integer
            Order of the rotations about the parent reference frame\'s unit
            vectors. The order can be specified by the strings ``\'XZX\'``,
            ``\'131\'``, or the integer ``131``. There are 12 unique valid
            rotation orders.

        Warns
        ======

        UserWarning
            If the orientation creates a kinematic loop.

        Examples
        ========

        Setup variables for the examples:

        >>> from sympy import symbols
        >>> from sympy.physics.vector import ReferenceFrame
        >>> q1, q2, q3 = symbols(\'q1, q2, q3\')
        >>> N = ReferenceFrame(\'N\')
        >>> B = ReferenceFrame(\'B\')
        >>> B1 = ReferenceFrame(\'B1\')
        >>> B2 = ReferenceFrame(\'B2\')
        >>> B3 = ReferenceFrame(\'B3\')

        >>> B.orient_space_fixed(N, (q1, q2, q3), \'312\')
        >>> B.dcm(N)
        Matrix([
        [ sin(q1)*sin(q2)*sin(q3) + cos(q1)*cos(q3), sin(q1)*cos(q2), sin(q1)*sin(q2)*cos(q3) - sin(q3)*cos(q1)],
        [-sin(q1)*cos(q3) + sin(q2)*sin(q3)*cos(q1), cos(q1)*cos(q2), sin(q1)*sin(q3) + sin(q2)*cos(q1)*cos(q3)],
        [                           sin(q3)*cos(q2),        -sin(q2),                           cos(q2)*cos(q3)]])

        is equivalent to:

        >>> B1.orient_axis(N, N.z, q1)
        >>> B2.orient_axis(B1, N.x, q2)
        >>> B3.orient_axis(B2, N.y, q3)
        >>> B3.dcm(N).simplify()
        Matrix([
        [ sin(q1)*sin(q2)*sin(q3) + cos(q1)*cos(q3), sin(q1)*cos(q2), sin(q1)*sin(q2)*cos(q3) - sin(q3)*cos(q1)],
        [-sin(q1)*cos(q3) + sin(q2)*sin(q3)*cos(q1), cos(q1)*cos(q2), sin(q1)*sin(q3) + sin(q2)*cos(q1)*cos(q3)],
        [                           sin(q3)*cos(q2),        -sin(q2),                           cos(q2)*cos(q3)]])

        It is worth noting that space-fixed and body-fixed rotations are
        related by the order of the rotations, i.e. the reverse order of body
        fixed will give space fixed and vice versa.

        >>> B.orient_space_fixed(N, (q1, q2, q3), \'231\')
        >>> B.dcm(N)
        Matrix([
        [cos(q1)*cos(q2), sin(q1)*sin(q3) + sin(q2)*cos(q1)*cos(q3), -sin(q1)*cos(q3) + sin(q2)*sin(q3)*cos(q1)],
        [       -sin(q2),                           cos(q2)*cos(q3),                            sin(q3)*cos(q2)],
        [sin(q1)*cos(q2), sin(q1)*sin(q2)*cos(q3) - sin(q3)*cos(q1),  sin(q1)*sin(q2)*sin(q3) + cos(q1)*cos(q3)]])

        >>> B.orient_body_fixed(N, (q3, q2, q1), \'132\')
        >>> B.dcm(N)
        Matrix([
        [cos(q1)*cos(q2), sin(q1)*sin(q3) + sin(q2)*cos(q1)*cos(q3), -sin(q1)*cos(q3) + sin(q2)*sin(q3)*cos(q1)],
        [       -sin(q2),                           cos(q2)*cos(q3),                            sin(q3)*cos(q2)],
        [sin(q1)*cos(q2), sin(q1)*sin(q2)*cos(q3) - sin(q3)*cos(q1),  sin(q1)*sin(q2)*sin(q3) + cos(q1)*cos(q3)]])

        '''
    def orient_quaternion(self, parent, numbers) -> None:
        """Sets the orientation of this reference frame relative to a parent
        reference frame via an orientation quaternion. An orientation
        quaternion is defined as a finite rotation a unit vector, ``(lambda_x,
        lambda_y, lambda_z)``, by an angle ``theta``. The orientation
        quaternion is described by four parameters:

        - ``q0 = cos(theta/2)``
        - ``q1 = lambda_x*sin(theta/2)``
        - ``q2 = lambda_y*sin(theta/2)``
        - ``q3 = lambda_z*sin(theta/2)``

        See `Quaternions and Spatial Rotation
        <https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation>`_ on
        Wikipedia for more information.

        Parameters
        ==========
        parent : ReferenceFrame
            Reference frame that this reference frame will be rotated relative
            to.
        numbers : 4-tuple of sympifiable
            The four quaternion scalar numbers as defined above: ``q0``,
            ``q1``, ``q2``, ``q3``.

        Warns
        ======

        UserWarning
            If the orientation creates a kinematic loop.

        Examples
        ========

        Setup variables for the examples:

        >>> from sympy import symbols
        >>> from sympy.physics.vector import ReferenceFrame
        >>> q0, q1, q2, q3 = symbols('q0 q1 q2 q3')
        >>> N = ReferenceFrame('N')
        >>> B = ReferenceFrame('B')

        Set the orientation:

        >>> B.orient_quaternion(N, (q0, q1, q2, q3))
        >>> B.dcm(N)
        Matrix([
        [q0**2 + q1**2 - q2**2 - q3**2,             2*q0*q3 + 2*q1*q2,            -2*q0*q2 + 2*q1*q3],
        [           -2*q0*q3 + 2*q1*q2, q0**2 - q1**2 + q2**2 - q3**2,             2*q0*q1 + 2*q2*q3],
        [            2*q0*q2 + 2*q1*q3,            -2*q0*q1 + 2*q2*q3, q0**2 - q1**2 - q2**2 + q3**2]])

        """
    def orient(self, parent, rot_type, amounts, rot_order: str = '') -> None:
        '''Sets the orientation of this reference frame relative to another
        (parent) reference frame.

        .. note:: It is now recommended to use the ``.orient_axis,
           .orient_body_fixed, .orient_space_fixed, .orient_quaternion``
           methods for the different rotation types.

        Parameters
        ==========

        parent : ReferenceFrame
            Reference frame that this reference frame will be rotated relative
            to.
        rot_type : str
            The method used to generate the direction cosine matrix. Supported
            methods are:

            - ``\'Axis\'``: simple rotations about a single common axis
            - ``\'DCM\'``: for setting the direction cosine matrix directly
            - ``\'Body\'``: three successive rotations about new intermediate
              axes, also called "Euler and Tait-Bryan angles"
            - ``\'Space\'``: three successive rotations about the parent
              frames\' unit vectors
            - ``\'Quaternion\'``: rotations defined by four parameters which
              result in a singularity free direction cosine matrix

        amounts :
            Expressions defining the rotation angles or direction cosine
            matrix. These must match the ``rot_type``. See examples below for
            details. The input types are:

            - ``\'Axis\'``: 2-tuple (expr/sym/func, Vector)
            - ``\'DCM\'``: Matrix, shape(3,3)
            - ``\'Body\'``: 3-tuple of expressions, symbols, or functions
            - ``\'Space\'``: 3-tuple of expressions, symbols, or functions
            - ``\'Quaternion\'``: 4-tuple of expressions, symbols, or
              functions

        rot_order : str or int, optional
            If applicable, the order of the successive of rotations. The string
            ``\'123\'`` and integer ``123`` are equivalent, for example. Required
            for ``\'Body\'`` and ``\'Space\'``.

        Warns
        ======

        UserWarning
            If the orientation creates a kinematic loop.

        '''
    def orientnew(self, newname, rot_type, amounts, rot_order: str = '', variables: Incomplete | None = None, indices: Incomplete | None = None, latexs: Incomplete | None = None):
        '''Returns a new reference frame oriented with respect to this
        reference frame.

        See ``ReferenceFrame.orient()`` for detailed examples of how to orient
        reference frames.

        Parameters
        ==========

        newname : str
            Name for the new reference frame.
        rot_type : str
            The method used to generate the direction cosine matrix. Supported
            methods are:

            - ``\'Axis\'``: simple rotations about a single common axis
            - ``\'DCM\'``: for setting the direction cosine matrix directly
            - ``\'Body\'``: three successive rotations about new intermediate
              axes, also called "Euler and Tait-Bryan angles"
            - ``\'Space\'``: three successive rotations about the parent
              frames\' unit vectors
            - ``\'Quaternion\'``: rotations defined by four parameters which
              result in a singularity free direction cosine matrix

        amounts :
            Expressions defining the rotation angles or direction cosine
            matrix. These must match the ``rot_type``. See examples below for
            details. The input types are:

            - ``\'Axis\'``: 2-tuple (expr/sym/func, Vector)
            - ``\'DCM\'``: Matrix, shape(3,3)
            - ``\'Body\'``: 3-tuple of expressions, symbols, or functions
            - ``\'Space\'``: 3-tuple of expressions, symbols, or functions
            - ``\'Quaternion\'``: 4-tuple of expressions, symbols, or
              functions

        rot_order : str or int, optional
            If applicable, the order of the successive of rotations. The string
            ``\'123\'`` and integer ``123`` are equivalent, for example. Required
            for ``\'Body\'`` and ``\'Space\'``.
        indices : tuple of str
            Enables the reference frame\'s basis unit vectors to be accessed by
            Python\'s square bracket indexing notation using the provided three
            indice strings and alters the printing of the unit vectors to
            reflect this choice.
        latexs : tuple of str
            Alters the LaTeX printing of the reference frame\'s basis unit
            vectors to the provided three valid LaTeX strings.

        Examples
        ========

        >>> from sympy import symbols
        >>> from sympy.physics.vector import ReferenceFrame, vlatex
        >>> q0, q1, q2, q3 = symbols(\'q0 q1 q2 q3\')
        >>> N = ReferenceFrame(\'N\')

        Create a new reference frame A rotated relative to N through a simple
        rotation.

        >>> A = N.orientnew(\'A\', \'Axis\', (q0, N.x))

        Create a new reference frame B rotated relative to N through body-fixed
        rotations.

        >>> B = N.orientnew(\'B\', \'Body\', (q1, q2, q3), \'123\')

        Create a new reference frame C rotated relative to N through a simple
        rotation with unique indices and LaTeX printing.

        >>> C = N.orientnew(\'C\', \'Axis\', (q0, N.x), indices=(\'1\', \'2\', \'3\'),
        ... latexs=(r\'\\hat{\\mathbf{c}}_1\',r\'\\hat{\\mathbf{c}}_2\',
        ... r\'\\hat{\\mathbf{c}}_3\'))
        >>> C[\'1\']
        C[\'1\']
        >>> print(vlatex(C[\'1\']))
        \\hat{\\mathbf{c}}_1

        '''
    def set_ang_acc(self, otherframe, value) -> None:
        """Define the angular acceleration Vector in a ReferenceFrame.

        Defines the angular acceleration of this ReferenceFrame, in another.
        Angular acceleration can be defined with respect to multiple different
        ReferenceFrames. Care must be taken to not create loops which are
        inconsistent.

        Parameters
        ==========

        otherframe : ReferenceFrame
            A ReferenceFrame to define the angular acceleration in
        value : Vector
            The Vector representing angular acceleration

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame
        >>> N = ReferenceFrame('N')
        >>> A = ReferenceFrame('A')
        >>> V = 10 * N.x
        >>> A.set_ang_acc(N, V)
        >>> A.ang_acc_in(N)
        10*N.x

        """
    def set_ang_vel(self, otherframe, value) -> None:
        """Define the angular velocity vector in a ReferenceFrame.

        Defines the angular velocity of this ReferenceFrame, in another.
        Angular velocity can be defined with respect to multiple different
        ReferenceFrames. Care must be taken to not create loops which are
        inconsistent.

        Parameters
        ==========

        otherframe : ReferenceFrame
            A ReferenceFrame to define the angular velocity in
        value : Vector
            The Vector representing angular velocity

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame
        >>> N = ReferenceFrame('N')
        >>> A = ReferenceFrame('A')
        >>> V = 10 * N.x
        >>> A.set_ang_vel(N, V)
        >>> A.ang_vel_in(N)
        10*N.x

        """
    @property
    def x(self):
        """The basis Vector for the ReferenceFrame, in the x direction. """
    @property
    def y(self):
        """The basis Vector for the ReferenceFrame, in the y direction. """
    @property
    def z(self):
        """The basis Vector for the ReferenceFrame, in the z direction. """
    def partial_velocity(self, frame, *gen_speeds):
        """Returns the partial angular velocities of this frame in the given
        frame with respect to one or more provided generalized speeds.

        Parameters
        ==========
        frame : ReferenceFrame
            The frame with which the angular velocity is defined in.
        gen_speeds : functions of time
            The generalized speeds.

        Returns
        =======
        partial_velocities : tuple of Vector
            The partial angular velocity vectors corresponding to the provided
            generalized speeds.

        Examples
        ========

        >>> from sympy.physics.vector import ReferenceFrame, dynamicsymbols
        >>> N = ReferenceFrame('N')
        >>> A = ReferenceFrame('A')
        >>> u1, u2 = dynamicsymbols('u1, u2')
        >>> A.set_ang_vel(N, u1 * A.x + u2 * N.y)
        >>> A.partial_velocity(N, u1)
        A.x
        >>> A.partial_velocity(N, u1, u2)
        (A.x, N.y)

        """
