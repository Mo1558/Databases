from rest_framework.decorators import api_view, permission_classes
from helper.mainFunc import createItem, deleteItem, getAllItems, getItem, updateItem
from clients.models import Client,Country
from clients.api.serializers import ClientSerializer,CountrySerializer,ClientViewSerializer


@api_view(['GET'])
def clients(request):
    '''
    this is function for display all clients as api or json data ,
    (getAllItems) it is function from helper app 
    '''
    return getAllItems(request=request,model=Client,serializer=ClientViewSerializer)


@api_view(['POST'])
def createclient(request):
    '''
    this is function for create client as api or json data ,
    (createItem) it is function from helper app Enter country ID 
    not details
    '''
    return createItem(request=request,serializer=ClientSerializer)


@api_view(['PUT'])
def updateclient(request,id):
    '''
    this is function for update  specific client as api or json data ,
    (updateItem) it is function from helper app country ID 
    not details
    '''
    return updateItem(request=request,model=Client,serializer=ClientSerializer,id=id)


@api_view(['GET'])
def getclient(request,id):
    '''
    this is function for display  specific client as api or json data ,
    (getItem) it is function from helper app 
    '''
    return getItem(request=request,model=Client,serializer=ClientViewSerializer,id=id)


@api_view(['DELETE'])
def deleteclient(request,id):
    '''
    this is function for delete  specific client as api or json data ,
    (getItem) it is function from helper app 
    '''
    return deleteItem(request=request,model=Client,id=id)