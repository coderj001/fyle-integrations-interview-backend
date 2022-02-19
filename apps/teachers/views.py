import json

from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from apps.students.models import Assignment
from apps.teachers.models import Teacher
from apps.teachers.serializers import TeacherAssignmentSerializer

class AssignmentsView(ListCreateAPIView):
    serializer_class = TeacherAssignmentSerializer

    def get(self, request, *args, **kwargs):
        teacher_id = json.loads(request.headers.get("X-Principal", '{}')).get("teacher_id", None)
        user_id = json.loads(request.headers.get("X-Principal", '{}')).get("user_id", None)
        teacher = Teacher.objects.get(pk=teacher_id, user=user_id)
        assignments = Assignment.objects.filter(teacher__user=teacher.user)

        return Response(
            data=self.serializer_class(assignments, many=True).data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, *args, **kwargs):
        teacher_id = json.loads(request.headers.get("X-Principal", '{}')).get("teacher_id", None)
        # user_id = json.loads(request.headers.get("X-Principal", '{}')).get("user_id", None)

        teacher = Teacher.objects.get(pk=teacher_id)
        request.data['teacher'] = teacher.id
        request.data['state'] = "GRADED"

        try:
            assignment = Assignment.objects.get(pk=request.data['id'])
        except Assignment.DoesNotExist:
            return Response(
                data={'error': 'Assignment does not exist/permission denied'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.serializer_class(assignment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
