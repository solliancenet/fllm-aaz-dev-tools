# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from foundationallm.cli.core.aaz import *


@register_command(
    "network vnet show",
)
class Show(AAZCommand):
    """Get the details of a virtual network.

    To learn more about Virtual Networks visit
    https://docs.microsoft.com/azure/virtual-network/virtual-network-manage-network.

    :example: Get details for MyVNet.
        az group create -n MyResourceGroup -l westus
        az network vnet show -g MyResourceGroup -n MyVNet

    :example: Get details by Id
        az group create -n MyResourceGroup -l westus
        az network vnet show --ids /subscription/sub/resourceGroup/mygroup
    """
    pass


__all__ = ["Show"]
