from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import AuthenticationFailed
from .serializers import PartnershipSerializer, ManagerSerializer
from .serializers import PartnerSerializer
from .models import Partnership, Partner, Manager
import jwt
from django.http import JsonResponse


# Create your views here.
class PartnershipView(APIView):
    '''Class View Partnership'''

    def post(self, request):
        '''Create a new partnership'''

        serializer = PartnershipSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        '''Get all partnership'''

        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        partnership = get_object_or_404(
            Partnership.objects.all(),
            name=request.data.get('name', '')
        )
        serializer = PartnershipSerializer(partnership)
        return Response(serializer.data)

    def put(self, request, pk):
        '''Update an partnership'''

        saved_Partnership = get_object_or_404(Partnership.objects.all(), pk=pk)
        data = request.data
        serializer = PartnershipSerializer(
            instance=saved_Partnership,
            data=data,
            partial=True
        )
        if serializer.is_valid(raise_exception=True):
            p_saved = serializer.save()

        return Response(
            {"success": f"Card '{p_saved.name}' updated successfully"}
        )

    def delete(self, request, pk=None):
        '''Delete an patnership'''

        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        partnership = get_object_or_404(
            Partnership.objects.all(),
            pk=pk
        )
        partnership.delete()

        return Response(
            {"message": f"Partnership with id `{pk}` has been deleted."},
            status=204,
        )


class CreateManagerView(APIView):
    '''Class View Manager'''

    def post(self, request, pk=None):
        '''Create a new Manager'''

        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        payload = request.data
        payload.update('partnership_id', pk)
        serializer = ManagerSerializer(data=payload)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request, pk=None):
        '''Get all Manager'''

        manager = get_object_or_404(
            Manager.objects.all(),
            partnership_id=pk
        )
        serializer = ManagerSerializer(manager)
        return Response(serializer.data)

    def put(self, request, pk=None):
        '''Update an Manager'''

        return Response(
            {"message": "Method not allowed."},
            status=405
        )

    def delete(self, request, pk=None):
        '''Delete an object'''

        return Response(
            {"message": "Method not allowed."},
            status=405
        )


class CreatePartnerView(APIView):
    '''Class View Partner'''

    def post(self, request, pk):
        '''Create a new Partner'''

        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        payload = request.data
        payload.update('partnership_id', pk)
        serializer = PartnerSerializer(data=payload)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request, pk):
        '''Get all Partner'''

        partner = get_object_or_404(
            Partner.objects.all(),
            partnership_id=pk
        )
        serializer = PartnerSerializer(partner)
        return Response(serializer.data)

    def put(self, request, pk):
        '''Update an Partner'''

        return Response(
            {"message": "Method not allowed."},
            status=405
        )

    def delete(self, request, pk=None):
        '''Delete an partner'''

        return Response(
            {"message": "Method not allowed."},
            status=405
        )


def sociedad_by_rut(request):
    ''' Buscar sociedad por rut'''

    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        jwt.decode(token, 'secret', algorithm=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    rut = request.GET.get('rut')

    if not rut:
        return JsonResponse(
            {
                'error': 'Parameter "rut" is required'
            },
            status=400
        )

    sociedad = None
    if partner := get_object_or_404(Partner, rut=rut):
        sociedad = partner.partnership.first()

    # Si no se encontró en socios, buscar en administradores
    if not sociedad:
        if manager := get_object_or_404(Manager, rut=rut):
            sociedad = manager.partnership.first()

    if sociedad:
        data = {'nombre_sociedad': sociedad.name}
    else:
        data = {'mensaje': 'No se encontró ninguna sociedad asociada al RUT'}
    return JsonResponse(data)
