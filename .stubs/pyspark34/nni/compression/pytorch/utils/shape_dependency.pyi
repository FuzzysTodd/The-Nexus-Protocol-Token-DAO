from _typeshed import Incomplete

__all__ = ['ChannelDependency', 'GroupDependency', 'ReshapeDependency', 'InputChannelDependency', 'AttentionWeightDependency']

class Dependency:
    graph: Incomplete
    model: Incomplete
    dependency: Incomplete
    def __init__(self, model: Incomplete | None = None, dummy_input: Incomplete | None = None, traced_model: Incomplete | None = None) -> None:
        """
        Build the graph for the model.
        """
    def build_dependency(self) -> None: ...
    def export(self, filepath) -> None: ...

class ChannelDependency(Dependency):
    """
    This model analyze the channel dependencies between the conv
    layers in a model.

    Parameters
    ----------
    model : torch.nn.Module
        The model to be analyzed.
    data : torch.Tensor
        The example input data to trace the network architecture.
    traced_model : torch._C.Graph
        if we alreay has the traced graph of the target model, we donnot
        need to trace the model again.
    prune_type: str
        This parameter indicates the channel pruning type: 1) `Filter`
        prune the filter of the convolution layer to prune the corresponding
        channels 2) `Batchnorm`: prune the channel in the batchnorm layer
    """
    prune_type: Incomplete
    target_types: Incomplete
    dependency: Incomplete
    def __init__(self, model, dummy_input, traced_model: Incomplete | None = None, prune_type: str = 'Filter') -> None: ...
    def build_dependency(self) -> None:
        """
        Build the channel dependency for the conv layers
        in the model.
        """
    def export(self, filepath) -> None:
        """
        export the channel dependencies as a csv file.
        The layers at the same line have output channel
        dependencies with each other. For example,
        layer1.1.conv2, conv1, and layer1.0.conv2 have
        output channel dependencies with each other, which
        means the output channel(filters) numbers of these
        three layers should be same with each other, otherwise
        the model may has shape conflict.
        Output example:
        Dependency Set,Convolutional Layers
        Set 1,layer1.1.conv2,layer1.0.conv2,conv1
        Set 2,layer1.0.conv1
        Set 3,layer1.1.conv1
        """
    @property
    def dependency_sets(self):
        """
        Get the list of the dependency set.

        Returns
        -------
        dependency_sets : list
            list of the dependency sets. For example,
            [set(['conv1', 'conv2']), set(['conv3', 'conv4'])]
        """

class InputChannelDependency(ChannelDependency):
    """
    Some pruners may prune the input channel of the convolutional
    layers. While pruning the input channel of the convolutional layers,
    the layers that share the same input tensor should prune the same
    channels, and we say these layers that share the same input tensor/channel
    has the input channel dependency. If we only prune the input channel of one
    layer in the dependency set, there will be a shape conflict for the other
    layers in the same dependency set, which may trigger a runtime error.
    Here we judge whether the application will truncate the dependency by analyzing
    whether the number of channels before and after the operation has changed.
    If not, the input channel dependency will be passed to the following nodes.
    """
    def __init__(self, model, dummy_input, traced_model: Incomplete | None = None) -> None:
        """
        This model analyze the input channel dependencies between the conv
        layers in a model.

        Parameters
        ----------
        model : torch.nn.Module
            The model to be analyzed.
        data : torch.Tensor
            The example input data to trace the network architecture.
        traced_model : torch._C.Graph
            if we alreay has the traced graph of the target model, we donnot
            need to trace the model again.
        """
    def build_dependency(self) -> None:
        """
        Build the input channel dependencies.
        The `InputChannelDependency` indicates the layers that have
        dependencies when pruning the input channel of the conv layers.
        In contrast, `ChannelDependency` indicates the dependent layers
        when pruning the output channles of conv layers (for example, L1FilterPruner).
        """

class GroupDependency(Dependency):
    """
    This model analyze the group dependencis between the conv
    layers in a model.

    Parameters
    ----------
    model : torch.nn.Module
        The model to be analyzed.
    dummy_input : torch.Tensor
        The example input data to trace the network architecture.
    traced_model : torch._C.Graph
        if we alreay has the traced graph of the target model, we donnot
        need to trace the model again.
    """
    min_groups: Incomplete
    def __init__(self, model, dummy_input, traced_model: Incomplete | None = None) -> None: ...
    groups: Incomplete
    def build_dependency(self):
        """
        Build the channel dependency for the conv layers
        in the model. This function return the group number
        of each conv layers. Note that, here, the group count
        of conv layers may be larger than their originl groups.
        This is because that the input channel will also be grouped
        for the group conv layers. To make this clear, assume we
        have two group conv layers: conv1(group=2), conv2(group=4).
        conv2 takes the output features of conv1 as input.
        Then we have to the filters of conv1 can still be
        divided into 4 groups after filter pruning, because
        the input channels of conv2 should be divided into
        4 groups.

        Returns
        -------
        self.dependency : dict
            key: the name of conv layers, value: the minimum value that the number of
            filters should be divisible to.
        """
    def export(self, filepath) -> None:
        """
        export the group dependency to a csv file.
        Each line describes a convolution layer, the
        first part of each line is the Pytorch module
        name of the conv layer. The second part of each
        line is the group count of the filters in this layer.
        Note that, the group count may be larger than this
        layers original group number.
        output example:
        Conv layer, Groups
        Conv1, 1
        Conv2, 2
        Conv3, 4
        """
    @property
    def dependency_sets(self): ...

class ReshapeDependency(Dependency):
    def __init__(self, model: Incomplete | None = None, dummy_input: Incomplete | None = None, traced_model: Incomplete | None = None) -> None:
        """
        Some model may have the view/reshape functions, such functions may have fixed parameters
        and cannot be replaced at all. Therefore, these functions may have some constraints on
        their input shapes. In this class, we find the direct input conv/linear layers of these
        reshape functions. If you get the shape conflict when run the forward inference on the
        speeduped model, please try remove these layers from the pruner config list and try again.

        Parameters
        ----------
        model : torch.nn.Module
            The model to be analyzed.
        data : torch.Tensor
            The example input data to trace the network architecture.
        traced_model : torch._C.Graph
            if we alreay has the traced graph of the target model, we donnot
            need to trace the model again.
        """
    def build_dependency(self) -> None:
        """
        Build the channel dependency for the conv layers
        in the model.
        """
    def export(self, filepath) -> None:
        """
        export the reshape dependencies as a csv file.

        Output example:
        Reshape OP, Dependent Layers
        model.view.1,layer1.1.conv2,layer1.0.conv2,conv1
        model.mean.1,layer1.0.conv1
        model.reshape.1,layer1.1.conv1
        """
    @property
    def dependency_sets(self):
        """
        Get the list of the dependency set.

        Returns
        -------
        dependency_sets : list
            list of the dependency sets. For example,
            [set(['conv1', 'conv2']), set(['conv3', 'conv4'])]

        """

class AttentionWeightDependency(Dependency):
    def __init__(self, model: Incomplete | None = None, dummy_input: Incomplete | None = None, traced_model: Incomplete | None = None) -> None:
        """
        Groups the linear layers belonging to the same attention layer in a model.
        Currently, we only capture weights in attention layers with forward computations written
        as four Linear layers (projections for Q, K, V, and output) and two matmul operations.
        The method implemented here can work for Huggingface transformers but may not correctly
        capture transformers written in other fashions (e.g., torch.nn.Transformer).

        Parameters
        ----------
        model : torch.nn.Module
            The model to be analyzed.
        dummy_input : torch.Tensor
            The example input data to trace the network architecture.
        traced_model : torch._C.Graph
            if we already have the traced graph of the target model, we do not
            need to trace the model again.
        """
    def build_dependency(self) -> None:
        """
        For every matmul operation, find the immediate parent and children Linear operations.
        If we get three parents and one children, add these four weights as a dependecy group.
        """
    @property
    def dependency_sets(self):
        """
        Get the list of the dependency set.

        Returns
        -------
        dependency_sets : list
            list of the dependency sets.
            Each dependency set is a 4-element list of module names, with the first three elements being the projection
            matrices for Q, K, V (in any order), and the last element being the dense matrix.
        """
    def export(self, filepath) -> None:
        """
        Export the group dependency to a csv file. Each line describes an attention layer.

        Output example:
        Attention layer matmul op, Group
        """
