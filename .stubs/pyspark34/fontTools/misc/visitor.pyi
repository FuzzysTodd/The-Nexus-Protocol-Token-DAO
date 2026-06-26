class Visitor:
    defaultStop: bool
    @classmethod
    def register(celf, clazzes): ...
    @classmethod
    def register_attr(celf, clazzes, attrs): ...
    @classmethod
    def register_attrs(celf, clazzes_attrs): ...
    def visitObject(self, obj, *args, **kwargs) -> None:
        """Called to visit an object. This function loops over all non-private
        attributes of the objects and calls any user-registered (via
        @register_attr() or @register_attrs()) visit() functions.

        If there is no user-registered visit function, of if there is and it
        returns True, or it returns None (or doesn't return anything) and
        visitor.defaultStop is False (default), then the visitor will proceed
        to call self.visitAttr()"""
    def visitAttr(self, obj, attr, value, *args, **kwargs) -> None:
        """Called to visit an attribute of an object."""
    def visitList(self, obj, *args, **kwargs) -> None:
        """Called to visit any value that is a list."""
    def visitDict(self, obj, *args, **kwargs) -> None:
        """Called to visit any value that is a dictionary."""
    def visitLeaf(self, obj, *args, **kwargs) -> None:
        """Called to visit any value that is not an object, list,
        or dictionary."""
    def visit(self, obj, *args, **kwargs) -> None:
        """This is the main entry to the visitor. The visitor will visit object
        obj.

        The visitor will first determine if there is a registered (via
        @register()) visit function for the type of object. If there is, it
        will be called, and (visitor, obj, *args, **kwargs) will be passed to
        the user visit function.

        If there is no user-registered visit function, of if there is and it
        returns True, or it returns None (or doesn't return anything) and
        visitor.defaultStop is False (default), then the visitor will proceed
        to dispatch to one of self.visitObject(), self.visitList(),
        self.visitDict(), or self.visitLeaf() (any of which can be overriden in
        a subclass)."""
