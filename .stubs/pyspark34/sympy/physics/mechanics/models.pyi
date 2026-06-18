def multi_mass_spring_damper(n: int = 1, apply_gravity: bool = False, apply_external_forces: bool = False):
    """Returns a system containing the symbolic equations of motion and
    associated variables for a simple multi-degree of freedom point mass,
    spring, damper system with optional gravitational and external
    specified forces. For example, a two mass system under the influence of
    gravity and external forces looks like:

    ::

        ----------------
         |     |     |   | g
         \\    | |    |   V
      k0 /    --- c0 |
         |     |     | x0, v0
        ---------    V
        |  m0   | -----
        ---------    |
         | |   |     |
         \\ v  | |    |
      k1 / f0 --- c1 |
         |     |     | x1, v1
        ---------    V
        |  m1   | -----
        ---------
           | f1
           V

    Parameters
    ==========

    n : integer
        The number of masses in the serial chain.
    apply_gravity : boolean
        If true, gravity will be applied to each mass.
    apply_external_forces : boolean
        If true, a time varying external force will be applied to each mass.

    Returns
    =======

    kane : sympy.physics.mechanics.kane.KanesMethod
        A KanesMethod object.

    """
def n_link_pendulum_on_cart(n: int = 1, cart_force: bool = True, joint_torques: bool = False):
    """Returns the system containing the symbolic first order equations of
    motion for a 2D n-link pendulum on a sliding cart under the influence of
    gravity.

    ::

                  |
         o    y   v
          \\ 0 ^   g
           \\  |
          --\\-|----
          |  \\|   |
      F-> |   o --|---> x
          |       |
          ---------
           o     o

    Parameters
    ==========

    n : integer
        The number of links in the pendulum.
    cart_force : boolean, default=True
        If true an external specified lateral force is applied to the cart.
    joint_torques : boolean, default=False
        If true joint torques will be added as specified inputs at each
        joint.

    Returns
    =======

    kane : sympy.physics.mechanics.kane.KanesMethod
        A KanesMethod object.

    Notes
    =====

    The degrees of freedom of the system are n + 1, i.e. one for each
    pendulum link and one for the lateral motion of the cart.

    M x' = F, where x = [u0, ..., un+1, q0, ..., qn+1]

    The joint angles are all defined relative to the ground where the x axis
    defines the ground line and the y axis points up. The joint torques are
    applied between each adjacent link and the between the cart and the
    lower link where a positive torque corresponds to positive angle.

    """
